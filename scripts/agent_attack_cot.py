import os

if __name__ == '__main__':
    suffix=''
    agg = [True,False]
    trigger = ''
    defense_type=None

    #######################################################################################################################
    # llms = ['gpt-4o-mini','gpt-3.5-turbo', 'gpt-4o-2024-08-06','claude-3-5-sonnet-20240620']
    # llms = ['ollama/qwen2:72b', 'ollama/gemma2:9b','ollama/qwen2:7b']
    # llms = ['ollama/gemma2:27b','ollama/llama3:70b', 'ollama/llama3.1:70b']

    #######################################################################################################################
    # # COT backdoor/clean; test clean acc: only add attacker tool to toolkit; no any malicious attack
    # llms = ['ollama/mixtral:8x7b','ollama/llama3:8b', 'ollama/llama3.1:8b','ollama/qwen2:72b']
    llms = ['ollama/gemma2:27b']
    injection_methods = ['cot_backdoor', 'cot_clean'] #'cot_backdoor', 'cot_clean', 'clean'
    # triggers = ['through a prism of insight', 'with perspicacious discernment', 'conducting a comprehensive elucidation', ':)', '@_@']
    triggers = ['with perspicacious discernment']
    defense_type = 'cot_paraphrase_defense' # cot_paraphrase_defense, cot_shuffling_defense


    attack_types = ['naive']
    tasks_path = 'data/cot_data/agent_task_cot.jsonl'
    task_num = 2


    #######################################################################################################################

    for aggressive in agg:
        for injection_method in injection_methods:
            for trigger in triggers:
                for llm in llms:
                    for attack_type in attack_types:
                        if llm.startswith('gpt') or llm.startswith('gemini') or llm.startswith('claude'):
                            llm_name = llm
                            backend=None
                        elif llm.startswith('ollama'):
                            llm_name = llm.split('/')[-1]
                            backend='ollama'
                        else:
                            llm_name = llm.split('/')[-1]
                            backend='vllm'

                        log_path = f'logs/{injection_method}/{llm_name}'

                        database = f'memory_db/direct_prompt_injection/{attack_type}_gpt-4o-mini'

                        if trigger == ':)':
                            suffix = 'smile'
                        else:
                            suffix = trigger.replace(' ', '_')

                        attacker_tools_path = 'data/all_attack_tools_aggressive.jsonl' if aggressive else 'data/all_attack_tools_non_aggressive.jsonl'
                        log_memory_type = 'no_memory'
                        aggression_type = 'aggressive' if aggressive else 'non-aggressive'
                        log_file = f'{log_path}/{defense_type}/{attack_type}-{aggression_type}' if defense_type else f'{log_path}/{log_memory_type}/{attack_type}-{aggression_type}'
                        os.makedirs(os.path.dirname(log_file), exist_ok=True)
                        print(log_file)


                        if injection_method in ['cot_backdoor','cot_clean','clean']:
                            cmd = f'''nohup python main_attacker.py --llm_name {llm} --attack_type {attack_type} --use_backend {backend} --attacker_tools_path {attacker_tools_path} \
                                --{injection_method} \
                                --defense_type {defense_type} \
                                --tasks_path {tasks_path} \
                                --trigger '{trigger}' \
                                --task_num {task_num} \
                                > {log_file}_{suffix}.log 2>&1 &'''

                        os.system(cmd)