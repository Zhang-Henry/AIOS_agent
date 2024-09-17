import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import numpy as np
class PerplexityFilter:
    """
    Perplexity filter using Hugging Face models, such as Vicuna-7B-v1.3.
    """
    def __init__(self, model, tokenizer, threshold, window_size='all'):
        self.tokenizer = tokenizer
        self.model = model.cuda()  # Ensure the model runs on GPU
        self.threshold = threshold
        self.window_threshold = threshold
        self.window_size = window_size
        self.cn_loss = torch.nn.CrossEntropyLoss(reduction='none')

    def detect(self, sequence):
        if self.window_size == 'all':
            return (not self.filter([sequence])[-1][0])
        elif self.window_size <= 0 or type(self.window_size) != int:
            raise ValueError(f"ERROR: window_size={self.window_size}. window_size must be a positive integer.")
        return (not self.filter_window([sequence])[-1][0])

    def get_log_prob(self, sequence):
        input_ids = self.tokenizer.encode(sequence, return_tensors='pt').cuda()
        with torch.no_grad():
            logits = self.model(input_ids, labels=input_ids).logits
        logits = logits[:, :-1, :].contiguous()
        input_ids = input_ids[:, 1:].contiguous()
        log_probs = self.cn_loss(logits.view(-1, logits.size(-1)), input_ids.view(-1))
        return log_probs

    def filter(self, sequences):
        filtered_log_ppl = []
        passed_filter = []
        for sequence in sequences:
            log_probs = self.get_log_prob(sequence)
            NLL_by_token = log_probs
            if NLL_by_token.mean() <= self.threshold:
                passed_filter.append(True)
                filtered_log_ppl.append(NLL_by_token.mean().item())
            else:
                passed_filter.append(False)
                filtered_log_ppl.append(NLL_by_token.mean().item())
        print(filtered_log_ppl, passed_filter)
        return filtered_log_ppl, passed_filter

    def filter_window(self, sequences, reverse=False):
        filtered_log_ppl_by_window = []
        passed_filter_by_window = []
        passed = []
        for sequence in sequences:
            sequence_window_scores = []
            passed_window_filter = []
            log_probs = self.get_log_prob(sequence)
            NLL_by_token = log_probs
            for i in np.arange(0, len(NLL_by_token), self.window_size):
                if not reverse:
                    window = NLL_by_token[i:i+self.window_size]
                else:
                    if i == 0:
                        window = NLL_by_token[-self.window_size:]
                    elif -(-i-self.window_size) > len(NLL_by_token) and i != 0:
                        window = NLL_by_token[:-i]
                    else:
                        window = NLL_by_token[-i-self.window_size:-i]
                if window.mean() <= self.window_threshold:
                    passed_window_filter.append(True)
                    sequence_window_scores.append(window.mean().item())
                else:
                    passed_window_filter.append(False)
                    sequence_window_scores.append(window.mean().item())
            if all(passed_window_filter):
                passed.append(True)
            else:
                passed.append(False)
            passed_filter_by_window.append(passed_window_filter)
            filtered_log_ppl_by_window.append(sequence_window_scores)
        return filtered_log_ppl_by_window, passed_filter_by_window, passed



import os
os.environ['MASTER_ADDR'] = 'localhost'
os.environ['MASTER_PORT'] = '12355'

import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch.distributed as dist
import torch.multiprocessing as mp

# 用于分布式模型加载和推理
def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'  # 或者设置为主机 IP 地址
    os.environ['MASTER_PORT'] = '12355'      # 设置一个未被占用的端口

    dist.init_process_group("gloo", rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()

def load_model(rank, world_size, model_name, perplexity_threshold, window_size):
    setup(rank, world_size)

    # 在指定的 GPU 上加载模型
    model = AutoModelForCausalLM.from_pretrained(model_name).cuda(rank)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # 使用 DistributedDataParallel 包装模型
    model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[rank])

    # 定义 PerplexityFilter
    filter = PerplexityFilter(model=model, tokenizer=tokenizer, threshold=perplexity_threshold, window_size=window_size)

    # 测试文本
    test_sequence = "This is a test sentence to check perplexity using vicuna-7b-v1.3."

    # 检测 perplexity
    passed_filter = filter.detect(test_sequence)
    print(f"Passed Filter: {passed_filter}")

    cleanup()

def run_model_parallel(model_name, perplexity_threshold=2.0, window_size=10):
    world_size = torch.cuda.device_count()  # 获取可用的 GPU 数量
    mp.spawn(load_model, args=(world_size, model_name, perplexity_threshold, window_size), nprocs=world_size, join=True)

# 确保多进程代码只在主进程中执行
if __name__ == "__main__":
    model_name = 'EleutherAI/gpt-neo-1.3B'

    run_model_parallel(model_name)
