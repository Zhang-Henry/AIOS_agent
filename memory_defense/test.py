import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import numpy as np

class PerplexityFilter:
    """
    Perplexity filter using Hugging Face models, such as GPT-Neo or similar models.
    """
    def __init__(self, model, tokenizer, threshold, window_size='all'):
        self.tokenizer = tokenizer
        self.model = model.cuda()  # Ensure the model runs on GPU
        self.threshold = threshold
        self.window_threshold = threshold
        self.window_size = window_size
        self.cn_loss = torch.nn.CrossEntropyLoss(reduction='none')

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
        return filtered_log_ppl, passed_filter

def load_model_and_tokenizer(model_name):
    """
    加载指定名称的模型和 tokenizer。

    参数：
    - model_name: 模型的名称（例如 'EleutherAI/gpt-neo-1.3B'）

    返回：
    - model: 加载的模型实例
    - tokenizer: 与模型对应的 tokenizer 实例
    """
    print(f"Loading model: {model_name}")
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name, clean_up_tokenization_spaces=False)
    return model, tokenizer

def evaluate_workflow(workflow_sentence, perplexity_threshold, model, tokenizer, window_size='all'):
    """
    评估工作流句子的困惑度，并判断是否超过阈值。

    参数：
    - workflow_sentence: 输入的工作流句子。
    - perplexity_threshold: 困惑度阈值，超过该阈值即为 'poisoned workflow'。
    - model: 已加载的语言模型。
    - tokenizer: 与模型对应的 tokenizer。
    - window_size: 滑动窗口大小，默认 'all'。

    返回：
    - perplexity: 计算出的困惑度。
    - is_poisoned: 如果困惑度超过阈值，则判定为 'poisoned workflow'，返回 True，否则返回 False。
    """
    # 实例化 PerplexityFilter
    filter = PerplexityFilter(model=model, tokenizer=tokenizer, threshold=perplexity_threshold, window_size=window_size)

    # 计算困惑度
    log_ppl, passed_filter_list = filter.filter([workflow_sentence])
    nll = log_ppl[0]
    # 将 NLL 转换为困惑度
    perplexity = torch.exp(torch.tensor(nll)).item()

    # 判断是否为 'poisoned workflow'
    is_poisoned = perplexity > perplexity_threshold

    # 输出困惑度和判断结果
    return perplexity, is_poisoned

def main():
    """
    主函数，执行加载模型、评估工作流并输出结果。
    """
    # 模型名称
    model_name = 'EleutherAI/gpt-neo-1.3B'

    # 加载模型和 tokenizer
    model, tokenizer = load_model_and_tokenizer(model_name)

    # 定义困惑度阈值
    perplexity_threshold = 2.0  # 可根据任务调整

    # 测试工作流句子
    workflow_sentence = "This is a test sentence to check perplexity using vicuna-7b-v1.3."

    # 调用 evaluate_workflow 函数
    perplexity, is_poisoned = evaluate_workflow(workflow_sentence, perplexity_threshold, model, tokenizer)

    # 输出结果
    print(f"Perplexity: {perplexity}")
    print(f"Is poisoned workflow: {is_poisoned}")

if __name__ == "__main__":
    main()
