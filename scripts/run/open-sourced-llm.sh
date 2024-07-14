export HF_AUTH_TOKENS=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


# nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode automatic > logs/gemma2:9b-automatic.log
# nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode manual > logs/gemma2:9b-manual.log


# nohup python main_attacker.py --llm_name ollama/gemma2:27b --workflow_mode automatic > logs/gemma2:27b-automatic.log
# nohup python main_attacker.py --llm_name ollama/gemma2:27b --workflow_mode manual > logs/gemma2:27b-manual.log

# nohup python main_attacker.py --llm_name ollama/llama2  --workflow_mode automatic > logs/ollama_llama2-automatic.log
# nohup python main_attacker.py --llm_name ollama/llama2  --workflow_mode manual > logs/ollama_llama2-manual.log

# nohup python main_attacker.py --llm_name ollama/llama3:8b  --workflow_mode automatic > logs/ollama_llama3-automatic.log
# nohup python main_attacker.py --llm_name ollama/llama3:8b  --workflow_mode manual > logs/ollama_llama3-manual.log 2>&1

# nohup python main_attacker.py --llm_name ollama/llama3:70b --use_backend ollama --max_gpu_memory '{"4": "44GB", "0": "44GB"}' --eval_device "cuda:3"   > logs/ollama_llama3-70b-manual.log
# nohup python main_attacker.py --llm_name ollama/llama3:70b  --workflow_mode automatic > logs/ollama_llama3-70b-automatic.log


# nohup python main_attacker.py --llm_name meta-llama/Meta-Llama-3-8B-Instruct --workflow_mode automatic --max_gpu_memory '{"0": "24GB", "1": "24GB"}' --eval_device "cuda:0"   > logs/Meta-Llama-3-8B-Instruct-automatic.log
# nohup python main_attacker.py --llm_name meta-llama/Meta-Llama-3-8B-Instruct --max_gpu_memory '{"0": "24GB", "1": "24GB"}' --eval_device "cuda:0"  > logs/Meta-Llama-3-8B-Instruct-manual.log

# nohup python main_attacker.py --llm_name Trelis/Llama-2-7b-chat-hf-function-calling-v3 --workflow_mode automatic --max_gpu_memory '{"0": "24GB", "1": "24GB"}' --eval_device "cuda:0"   > logs/Llama-2-7b-chat-hf-function-calling-automatic.log
# nohup python main_attacker.py --llm_name Trelis/Llama-2-7b-chat-hf-function-calling-v3 --max_gpu_memory '{"0": "44GB", "1": "44GB"}' --eval_device "cuda:0"  > logs/Llama-2-7b-chat-hf-function-calling-manual.log


# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode automatic --max_gpu_memory '{"3": "44GB", "4": "44GB"}' --eval_device "cuda:3"   > logs/Meta-Llama-3-8B-Instruct-function-calling-automatic.log
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --max_gpu_memory '{"3": "44GB", "4": "44GB"}' --eval_device "cuda:3"  > logs/Meta-Llama-3-8B-Instruct-function-calling-manual.log

# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-70B-Instruct-function-calling --max_gpu_memory '{"3": "44GB", "4": "44GB"}' --eval_device "cuda:3"  > logs/Meta-Llama-3-70B-Instruct-function-calling-manual.log



# nohup python main_attacker.py --llm_name Qwen/Qwen2-72B-Instruct --workflow_mode automatic --max_gpu_memory '{"3": "44GB", "4": "44GB"}' --eval_device "cuda:3"    > logs/Qwen2-72B-Instruct-automatic.log  2>&1 &
# nohup python main_attacker.py --llm_name Qwen/Qwen2-72B-Instruct --workflow_mode manual --max_gpu_memory '{"3": "44GB", "4": "44GB", "0": "43GB", "1": "35GB", "1": "35GB"}' --eval_device "cuda:3"    > logs/Qwen2-72B-Instruct-manual.log  2>&1 &

# nohup python main_attacker.py --llm_name HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1 --workflow_mode automatic --max_gpu_memory '{"3": "44GB", "4": "44GB"}' --eval_device "cuda:3"    > logs/zephyr-orpo-141b-A35b-v0.1-automatic.log  2>&1 &
# nohup python main_attacker.py --llm_name HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1 --workflow_mode manual --max_gpu_memory '{"3": "44GB", "4": "44GB"}' --eval_device "cuda:3"    > logs/zephyr-orpo-141b-A35b-v0.1-manual.log  2>&1 &

nohup python main_attacker.py --llm_name microsoft/Phi-3-small-128k-instruct --workflow_mode manual --max_gpu_memory '{"3": "44GB", "4": "44GB", "0": "43GB", "1": "35GB", "1": "35GB"}' --eval_device "cuda:3"    > logs/Phi-3-small-128k-instruct-manual.log  2>&1 &
