# python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode automatic --observation_prompt_injection --attack_type naive --attacker_tools_path data/injecAgent_test.jsonl --tasks_path data/agent_task_test.jsonl > logs/attacker_test2.log

# python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode automatic --observation_prompt_injection --attack_type naive --attacker_tools_path data/attack_tools_test.jsonl --tasks_path data/agent_task_test.jsonl > logs/attacker_test.log

# python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode automatic --observation_prompt_injection --attack_type naive --attacker_tools_path data/attack_tools_test.jsonl --tasks_path data/agent_task_test.jsonl > logs/attacker_test_gpt3.5.log
python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --observation_prompt_injection --attack_type naive --attacker_tools_path data/attack_tools_test.jsonl --tasks_path data/agent_task_test.jsonl > logs/attacker_test_gpt-4o-mini.log

# python main_attacker.py --llm_name ollama/llama3.1:8b --workflow_mode automatic --observation_prompt_injection --attack_type naive --attacker_tools_path data/attack_tools_test.jsonl --tasks_path data/agent_task_test.jsonl > logs/attacker_test_llama3.1:8b.log