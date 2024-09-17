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
            logits = self.model(input_ids, labels=input_ids, use_cache=False).logits
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


# 加载 vicuna-7b-v1.3 模型和 tokenizer
model_name = 'EleutherAI/gpt-neo-1.3B'

model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name,clean_up_tokenization_spaces=False)

# 定义 perplexity filter 的阈值和窗口大小
perplexity_threshold = 2.0  # 可根据任务调整
window_size = 10  # 可选，用于滑动窗口过滤，或者使用 'all'

# 实例化 PerplexityFilter
filter = PerplexityFilter(model=model, tokenizer=tokenizer, threshold=perplexity_threshold, window_size=window_size)

# 测试序列
test_sequence = "This is a test sentence to check perplexity using vicuna-7b-v1.3."

# 检测序列是否通过过滤
passed_filter = filter.detect(test_sequence)
print(f"Passed Filter: {passed_filter}")

# 获取 perplexity 详情
log_ppl, passed_filter_list = filter.filter([test_sequence])
print(f"Log Perplexity: {log_ppl}")
print(f"Passed Filter: {passed_filter_list}")

# 使用窗口过滤 perplexity
windowed_ppl, windowed_filter_passes, passed = filter.filter_window([test_sequence])
print(f"Windowed Perplexity: {windowed_ppl}")
print(f"Windowed Filter Results: {windowed_filter_passes}")
