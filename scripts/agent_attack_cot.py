import os

if __name__ == '__main__':
    suffix=''
    agg = [True,False]
    write_db=False
    read_db=False
    trigger = ''

    #######################################################################################################################
    # llms = ['gpt-4o-mini','gpt-3.5-turbo', 'gpt-4o-2024-08-06','gemini-1.5-pro','gemini-1.5-flash','claude-3-5-sonnet-20240620','bedrock/anthropic.claude-3-haiku-20240307-v1:0']
    #llms = ['ollama/qwen2:72b', 'ollama/gemma2:9b','ollama/qwen2:7b']
    # llms = ['ollama/gemma2:9b']
    #llms = ['ollama/gemma2:27b','ollama/llama3:70b', 'ollama/llama3.1:70b']
    # llms = ['ollama/mixtral:8x7b','ollama/llama3:8b', 'ollama/llama3.1:8b']

    # attack_types = ['naive', 'context_ignoring', 'fake_completion', 'escape_characters', 'combined_attack']

    #######################################################################################################################
    # # COT backdoor/clean; test clean acc: only add attacker tool to toolkit; no any malicious attack

    llms = ['gpt-3.5-turbo', 'gpt-4o-2024-08-06']
    injection_methods = ['cot_backdoor', 'cot_clean', 'clean']
    # triggers = ['through a prism of insight', 'with perspicacious discernment', 'conducting a comprehensive elucidation', ':)', '@_@']
    triggers = ['with perspicacious discernment']


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

                        if aggressive:
                            attacker_tools_path = 'data/all_attack_tools_aggressive.jsonl'
                            log_file = f'{log_path}/no_memory/{attack_type}-aggressive'
                            if read_db:
                                log_file = f'{log_path}/new_memory/{attack_type}-aggressive'
                        else:
                            attacker_tools_path = 'data/all_attack_tools_non_aggressive.jsonl'
                            log_file = f'{log_path}/no_memory/{attack_type}-non-aggressive'
                            if read_db:
                                log_file = f'{log_path}/new_memory/{attack_type}-non-aggressive'


                        os.makedirs(os.path.dirname(log_file), exist_ok=True)
                        print(f'{log_file}_{suffix}')

                        if injection_method in ['cot_backdoor','cot_clean','clean']:
                            cmd = f'''nohup python main_attacker.py --llm_name {llm} --attack_type {attack_type} --use_backend {backend} --attacker_tools_path {attacker_tools_path} \
                                --{injection_method} \
                                --tasks_path {tasks_path} \
                                --trigger '{trigger}' \
                                --task_num {task_num} \
                                > {log_file}_{suffix}.log 2>&1 &'''

                        os.system(cmd)