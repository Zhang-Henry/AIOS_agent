from pathlib import Path
from tqdm.notebook import tqdm
import multiprocessing
import warnings
import gc
import torch
import os
import time
import random

# This is the script to run the OpenKE model in parallel;

script = "main_attacker.py"

parellel = 1

def run_model(task):
    task_id, model_name, data_name, quant, noise = task[0], task[1], task[2], task[3], task[4]
    print(f"Running {script}: Data: {data_name}, Model: {model_name}, Quantization: {quant}-bit")
    device = int(task_id % (torch.cuda.device_count()))
    device = f"cuda:{device}"
    
    time.sleep(random.randint(0, 5)) # sleep for a while to avoid CPU overload
    memory = '{"1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}'
    comment = f"python {script} --llm_name {model_name} --workflow_mode {quant} --observation_prompt_injection --attack_type {0} --max_gpu_memory {memory} --eval_device {device} --dataset {data_name} 2>&1 &"
    print(comment)
    os.system(comment)
    gc.collect()

"""
    Run LLM
"""
def run_LLM():
    task_id, tasks = 0, []
    data_name_list = ['StrategyQA','coinflip','cities','common','counterfact','STSA','IMDb','sarcasm','hateeval']
    
    model_name_list = ["ollama/llama3:8b", "ollama/llama3.1:8b", "ollama/gemma2:9b"]
    
    for model_name in model_name_list:
        tasks.append([task_id, model_name, data_name, quant, noise])
        task_id += 1

    with multiprocessing.Pool(parellel) as p:
        p.map(run_model, tasks)

def run_all_models():
    run_LLM()

run_all_models()