
# export GEMINI_API_KEY=<YOUR GEMINI API KEY>

# nohup python main_attacker.py --llm_name gpt-4 --workflow_mode automatic --observation_prompt_injection > logs/gpt-4-automatic.log
# nohup python main_attacker.py --llm_name gpt-4 --observation_prompt_injection > logs/gpt-4-manual.log


# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode automatic --observation_prompt_injection > logs/gpt-3.5-automatic.log
nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode manual --observation_prompt_injection > logs/gpt-3.5-manual.log

# nohup python main.py --llm_name gpt-4 > logs/gpt-4-manual-07151441.log
#nohup python main.py --llm_name gpt-4
