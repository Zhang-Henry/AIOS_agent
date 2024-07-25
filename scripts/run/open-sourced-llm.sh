export HF_AUTH_TOKENS=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
#  --attacker_tools_path data/test.jsonl --tasks_path data/agent_tasks/example/academic_agent_task_test.txt

#####################################################################################
#################################### ollama/llama3:8b ####################################
#####################################################################################
########## observation_prompt_injection ##########
# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode manual --observation_prompt_injection --attack_type naive  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7" > logs/observation_prompt_injection/llama3:8b-manual-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode manual --observation_prompt_injection --attack_type context_ignoring  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:6" > logs/observation_prompt_injection/llama3:8b-manual-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode manual --observation_prompt_injection --attack_type fake_completion  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:5"  > logs/observation_prompt_injection/llama3:8b-manual-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode manual --observation_prompt_injection --attack_type escape_characters  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:4"  > logs/observation_prompt_injection/llama3:8b-manual-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode manual --observation_prompt_injection --attack_type combined_attack  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:3"  > logs/observation_prompt_injection/llama3:8b-manual-combined_attack.log 2>&1 &

# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode automatic --observation_prompt_injection --attack_type naive --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:2"  > logs/observation_prompt_injection/llama3:8b-automatic-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode automatic --observation_prompt_injection --attack_type context_ignoring --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:1"  > logs/observation_prompt_injection/llama3:8b-automatic-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode automatic --observation_prompt_injection --attack_type fake_completion --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:2"  > logs/observation_prompt_injection/llama3:8b-automatic-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode automatic --observation_prompt_injection --attack_type escape_characters --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:3"  > logs/observation_prompt_injection/llama3:8b-automatic-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:8b --workflow_mode automatic --observation_prompt_injection --attack_type combined_attack --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:4"  > logs/observation_prompt_injection/llama3:8b-automatic-combined_attack.log 2>&1 &

#####################################################################################
#################################### ollama/llama3.1:8b ####################################
#####################################################################################
########## observation_prompt_injection ##########
# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode manual --observation_prompt_injection --attack_type naive  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7" > logs/observation_prompt_injection/llama3.1:8b-manual-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode manual --observation_prompt_injection --attack_type context_ignoring  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:6" > logs/observation_prompt_injection/llama3.1:8b-manual-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode manual --observation_prompt_injection --attack_type fake_completion  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:5"  > logs/observation_prompt_injection/llama3.1:8b-manual-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode manual --observation_prompt_injection --attack_type escape_characters  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:4"  > logs/observation_prompt_injection/llama3.1:8b-manual-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode manual --observation_prompt_injection --attack_type combined_attack  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:3"  > logs/observation_prompt_injection/llama3.1:8b-manual-combined_attack.log 2>&1 &

# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode automatic --observation_prompt_injection --attack_type naive --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:2"  > logs/observation_prompt_injection/llama3.1:8b-automatic-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode automatic --observation_prompt_injection --attack_type context_ignoring --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:1"  > logs/observation_prompt_injection/llama3.1:8b-automatic-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode automatic --observation_prompt_injection --attack_type fake_completion --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:2"  > logs/observation_prompt_injection/llama3.1:8b-automatic-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode automatic --observation_prompt_injection --attack_type escape_characters --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:3"  > logs/observation_prompt_injection/llama3.1:8b-automatic-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode automatic --observation_prompt_injection --attack_type combined_attack --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:4"  > logs/observation_prompt_injection/llama3.1:8b-automatic-combined_attack.log 2>&1 &

#####################################################################################
####################################  Trelis/Meta-Llama-3-8B-Instruct-function-calling ####################################
#####################################################################################
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode manual --observation_prompt_injection --attack_type naive  --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:4" > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-manual-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode manual --observation_prompt_injection --attack_type context_ignoring  --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:3" > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-manual-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode manual --observation_prompt_injection --attack_type fake_completion  --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-manual-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode manual --observation_prompt_injection --attack_type escape_characters  --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-manual-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode manual --observation_prompt_injection --attack_type combined_attack  --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-manual-combined_attack.log 2>&1 &

# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode automatic --observation_prompt_injection --attack_type naive --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-automatic-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode automatic --observation_prompt_injection --attack_type context_ignoring --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-automatic-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode automatic --observation_prompt_injection --attack_type fake_completion --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-automatic-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode automatic --observation_prompt_injection --attack_type escape_characters --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-automatic-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name Trelis/Meta-Llama-3-8B-Instruct-function-calling --workflow_mode automatic --observation_prompt_injection --attack_type combined_attack --max_gpu_memory '{"0": "44GB", "1": "44GB","2": "44GB", "3": "44GB", "4": "44GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/Trelis-Llama-3-8B-Instruct-automatic-combined_attack.log 2>&1 &


#####################################################################################
#################################### llama3:70b ####################################
#####################################################################################
########## observation_prompt_injection ##########
# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode manual --observation_prompt_injection --attack_type naive  --max_gpu_memory '{"1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7" > logs/observation_prompt_injection/llama3:70b-manual-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode manual --observation_prompt_injection --attack_type context_ignoring  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7" > logs/observation_prompt_injection/llama3:70b-manual-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode manual --observation_prompt_injection --attack_type fake_completion  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/llama3:70b-manual-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode manual --observation_prompt_injection --attack_type escape_characters  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/llama3:70b-manual-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode manual --observation_prompt_injection --attack_type combined_attack  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/llama3:70b-manual-combined_attack.log 2>&1 &

# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode automatic --observation_prompt_injection --attack_type naive --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/llama3:70b-automatic-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode automatic --observation_prompt_injection --attack_type context_ignoring --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/llama3:70b-automatic-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode automatic --observation_prompt_injection --attack_type fake_completion --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/llama3:70b-automatic-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode automatic --observation_prompt_injection --attack_type escape_characters --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/llama3:70b-automatic-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name ollama/llama3:70b --workflow_mode automatic --observation_prompt_injection --attack_type combined_attack --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/llama3:70b-automatic-combined_attack.log 2>&1 &

#####################################################################################
#################################### gemma2:9b ####################################
#####################################################################################
########## observation_prompt_injection ##########
nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode manual --observation_prompt_injection --attack_type naive  --max_gpu_memory '{"1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7" > logs/observation_prompt_injection/gemma2:9b-manual-naive.log 2>&1 &
nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode manual --observation_prompt_injection --attack_type context_ignoring  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7" > logs/observation_prompt_injection/gemma2:9b-manual-context_ignoring.log 2>&1 &
nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode manual --observation_prompt_injection --attack_type fake_completion  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/gemma2:9b-manual-fake_completion.log 2>&1 &
nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode manual --observation_prompt_injection --attack_type escape_characters  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/gemma2:9b-manual-escape_characters.log 2>&1 &
nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode manual --observation_prompt_injection --attack_type combined_attack  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/gemma2:9b-manual-combined_attack.log 2>&1 &

nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode automatic --observation_prompt_injection --attack_type naive --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/gemma2:9b-automatic-naive.log 2>&1 &
nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode automatic --observation_prompt_injection --attack_type context_ignoring --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/gemma2:9b-automatic-context_ignoring.log 2>&1 &
nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode automatic --observation_prompt_injection --attack_type fake_completion --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/gemma2:9b-automatic-fake_completion.log 2>&1 &
nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode automatic --observation_prompt_injection --attack_type escape_characters --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/gemma2:9b-automatic-escape_characters.log 2>&1 &
nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode automatic --observation_prompt_injection --attack_type combined_attack --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}' --eval_device "cuda:7"  > logs/observation_prompt_injection/gemma2:9b-automatic-combined_attack.log 2>&1 &





# nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode automatic > logs/gemma2:9b-automatic.log
# nohup python main_attacker.py --llm_name ollama/gemma2:9b --workflow_mode manual > logs/gemma2:9b-manual.log


# nohup python main_attacker.py --llm_name ollama/gemma2:27b --workflow_mode automatic > logs/gemma2:27b-automatic.log
# nohup python main_attacker.py --llm_name ollama/gemma2:27b --workflow_mode manual > logs/gemma2:27b-manual.log

# nohup python main_attacker.py --llm_name ollama/llama2  --workflow_mode automatic > logs/ollama_llama2-automatic.log
# nohup python main_attacker.py --llm_name ollama/llama2  --workflow_mode manual > logs/ollama_llama2-manual.log



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

# nohup python main_attacker.py --llm_name microsoft/Phi-3-small-128k-instruct --workflow_mode manual --max_gpu_memory '{"3": "44GB", "4": "44GB", "0": "43GB", "1": "35GB", "1": "35GB"}' --eval_device "cuda:3"    > logs/Phi-3-small-128k-instruct-manual.log  2>&1 &

# nohup python main_attacker.py --llm_name apple/DCLM-7B --workflow_mode automatic --observation_prompt_injection --attack_type naive  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB"}' --eval_device "cuda:0" --attacker_tools_path data/test.jsonl  > logs/observation_prompt_injection/apple-DCLM-7B-automatic-naive.log
# nohup python main_attacker.py --llm_name mistralai/Mistral-7B-Instruct-v0.3 --workflow_mode automatic --observation_prompt_injection --attack_type naive  --max_gpu_memory '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB"}' --eval_device "cuda:0" --attacker_tools_path data/test.jsonl  > logs/observation_prompt_injection/Mistral-7B-Instruct-v0.3-automatic-naive.log
