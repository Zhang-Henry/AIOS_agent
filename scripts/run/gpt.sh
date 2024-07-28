#####################################################################################
#################################### gpt-3.5 ####################################
#####################################################################################

# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode automatic --observation_prompt_injection > logs/observation_prompt_injection/gpt-3.5-automatic.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode manual --observation_prompt_injection > logs/observation_prompt_injection/gpt-3.5-manual.log
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode manual --plan_attack > logs/plan_attack/gpt-3.5-manual.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode manual --action_attack --attacker_tools_path data/test.jsonl > logs/action_attack/gpt-3.5-manual.log 2>&1 &

########## observation_prompt_injection ##########
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode manual --observation_prompt_injection --attack_type naive > logs/observation_prompt_injection/gpt-3.5-turbo-manual-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode manual --observation_prompt_injection --attack_type context_ignoring > logs/observation_prompt_injection/gpt-3.5-turbo-manual-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode manual --observation_prompt_injection --attack_type fake_completion > logs/observation_prompt_injection/gpt-3.5-turbo-manual-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode manual --observation_prompt_injection --attack_type escape_characters > logs/observation_prompt_injection/gpt-3.5-turbo-manual-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode manual --observation_prompt_injection --attack_type combined_attack > logs/observation_prompt_injection/gpt-3.5-turbo-manual-combined_attack.log 2>&1 &

# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode automatic --observation_prompt_injection --attack_type naive > logs/observation_prompt_injection/gpt-3.5-turbo-automatic-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode automatic --observation_prompt_injection --attack_type context_ignoring > logs/observation_prompt_injection/gpt-3.5-turbo-automatic-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode automatic --observation_prompt_injection --attack_type fake_completion > logs/observation_prompt_injection/gpt-3.5-turbo-automatic-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode automatic --observation_prompt_injection --attack_type escape_characters > logs/observation_prompt_injection/gpt-3.5-turbo-automatic-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-3.5-turbo --workflow_mode automatic --observation_prompt_injection --attack_type combined_attack > logs/observation_prompt_injection/gpt-3.5-turbo-automatic-combined_attack.log 2>&1 &

#####################################################################################
#################################### gpt-4o-mini ####################################
#####################################################################################
#  --attacker_tools_path data/attack_tools_test.jsonl --tasks_path data/agent_task_test.jsonl

########## cot_backdoor ##########
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --cot_backdoor --attack_type naive --attacker_tools_path data/test.jsonl --tasks_path data/agent_tasks/example/academic_agent_task_test.txt > logs/cot_backdoor/gpt-4o-mini-automatic-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --cot_backdoor --attack_type context_ignoring > logs/cot_backdoor/gpt-4o-mini-automatic-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --cot_backdoor --attack_type fake_completion > logs/cot_backdoor/gpt-4o-mini-automatic-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --cot_backdoor --attack_type escape_characters > logs/cot_backdoor/gpt-4o-mini-automatic-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --cot_backdoor --attack_type combined_attack > logs/cot_backdoor/gpt-4o-mini-automatic-combined_attack.log 2>&1 &


########## observation_prompt_injection ##########
nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --observation_prompt_injection --attack_type naive --attacker_tools_path data/attack_tools_test.jsonl --tasks_path data/agent_task_test.jsonl > logs/observation_prompt_injection/gpt-4o-mini-manual-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --observation_prompt_injection --attack_type context_ignoring > logs/observation_prompt_injection/gpt-4o-mini-manual-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --observation_prompt_injection --attack_type fake_completion > logs/observation_prompt_injection/gpt-4o-mini-manual-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --observation_prompt_injection --attack_type escape_characters > logs/observation_prompt_injection/gpt-4o-mini-manual-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --observation_prompt_injection --attack_type combined_attack > logs/observation_prompt_injection/gpt-4o-mini-manual-combined_attack.log 2>&1 &

# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --observation_prompt_injection --attack_type naive > logs/observation_prompt_injection/gpt-4o-mini-automatic-naive-new.log
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --observation_prompt_injection --attack_type naive > logs/observation_prompt_injection/gpt-4o-mini-automatic-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --observation_prompt_injection --attack_type context_ignoring > logs/observation_prompt_injection/gpt-4o-mini-automatic-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --observation_prompt_injection --attack_type fake_completion > logs/observation_prompt_injection/gpt-4o-mini-automatic-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --observation_prompt_injection --attack_type escape_characters > logs/observation_prompt_injection/gpt-4o-mini-automatic-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --observation_prompt_injection --attack_type combined_attack > logs/observation_prompt_injection/gpt-4o-mini-automatic-combined_attack.log 2>&1 &

########## direct_prompt_injection ##########
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --direct_prompt_injection --attack_type naive > logs/direct_prompt_injection/gpt-4o-mini-automatic-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --direct_prompt_injection --attack_type context_ignoring > logs/direct_prompt_injection/gpt-4o-mini-automatic-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --direct_prompt_injection --attack_type fake_completion > logs/direct_prompt_injection/gpt-4o-mini-automatic-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --direct_prompt_injection --attack_type escape_characters > logs/direct_prompt_injection/gpt-4o-mini-automatic-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode automatic --direct_prompt_injection --attack_type combined_attack > logs/direct_prompt_injection/gpt-4o-mini-automatic-combined_attack.log 2>&1 &

# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --direct_prompt_injection --attack_type naive > logs/direct_prompt_injection/gpt-4o-mini-manual-naive.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --direct_prompt_injection --attack_type context_ignoring > logs/direct_prompt_injection/gpt-4o-mini-manual-context_ignoring.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --direct_prompt_injection --attack_type fake_completion > logs/direct_prompt_injection/gpt-4o-mini-manual-fake_completion.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --direct_prompt_injection --attack_type escape_characters > logs/direct_prompt_injection/gpt-4o-mini-manual-escape_characters.log 2>&1 &
# nohup python main_attacker.py --llm_name gpt-4o-mini --workflow_mode manual --direct_prompt_injection --attack_type combined_attack > logs/direct_prompt_injection/gpt-4o-mini-manual-combined_attack.log 2>&1 &




#####################################################################################
#################################### gpt-4 ####################################
#####################################################################################

# nohup python main_attacker.py --llm_name gpt-4 --workflow_mode automatic --observation_prompt_injection > logs/gpt-4-automatic.log
# nohup python main_attacker.py --llm_name gpt-4 --observation_prompt_injection > logs/gpt-4-manual.log
# nohup python main.py --llm_name gpt-4 > logs/gpt-4-manual-07151441.log
#nohup python main.py --llm_name gpt-4