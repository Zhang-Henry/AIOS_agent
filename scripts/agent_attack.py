import os

if __name__ == '__main__':
    eval_devices = '["cuda:7", "cuda:6", "cuda:5", "cuda:4", "cuda:3", "cuda:2", "cuda:1", "cuda:0"]'
    max_gpu_memory = '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB","7": "24GB"}'
    test=False
    suffix=''
    agg = [True,False]
    write_db=False
    read_db=False
    trigger = ''

    #######################################################################################################################
    # llms = ['gpt-4o-mini','gpt-3.5-turbo', 'gpt-4','gemini-1.5-pro','gemini-1.5-flash','claude-3-5-sonnet-20240620','bedrock/anthropic.claude-3-haiku-20240307-v1:0']
    # llms = ['ollama/qwen2:72b', 'ollama/gemma2:9b','ollama/qwen2:7b']
    # llms = ['ollama/gemma2:27b','ollama/llama3:70b', 'ollama/llama3.1:70b']
    # llms = ['ollama/mixtral:8x7b','ollama/llama3:8b', 'ollama/llama3.1:8b']

    # attack_types = ['naive', 'context_ignoring', 'fake_completion', 'escape_characters', 'combined_attack']
    # injection_method = 'direct_prompt_injection', 'observation_prompt_injection', 'plan_attack', 'action_attack', 'cot_backdoor','memory_attack', 'cot_clean'

    #######################################################################################################################
    # run direct_prompt_injection, observation_prompt_injection

    # llms = ['ollama/llama3.1:70b']

    # injection_method = 'direct_prompt_injection'
    # # injection_method = 'observation_prompt_injection'
    # # injection_method = 'memory_attack'

    # read_db = True
    # suffix = 'full_tools'
    # attack_types = ['combined_attack']
    # #attack_types = ['naive', 'context_ignoring', 'fake_completion', 'escape_characters', 'combined_attack']
    # #write_db = True

    #######################################################################################################################
    # # COT backdoor/clean; test clean acc: only add attacker tool to toolkit; no any malicious attack

    llms = ['gpt-4o-mini']

    # injection_method = 'cot_backdoor'
    # injection_method = 'cot_clean'
    injection_method = 'clean'
    trigger = 'with perspicacious discernment'

    # trigger = ['through a prism of insight', 'with perspicacious discernment', 'conducting a comprehensive elucidation', ':)', '@_@']
    attack_types = ['naive']
    tasks_path = 'data/cot_data/agent_task_cot.jsonl'
    task_num = 2


    #######################################################################################################################
    # jailbreak
    # agg = [True, False]
    # llms = ['gpt-4o-mini','ollama/llama3:70b','ollama/llama3.1:70b']
    # # llms = ['ollama/llama3:70b','ollama/llama3.1:70b']
    # injection_method = 'jailbreak'
    # suffix = 'absolute'

    # attack_types = ['absolute']
    #######################################################################################################################

    for aggressive in agg:
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

                result_file = f'{log_path}/result_statistics_.log'
                database = f'memory_db/direct_prompt_injection/{attack_type}_gpt-4o-mini'

                if aggressive:
                    attacker_tools_path = 'data/all_attack_tools_aggressive.jsonl'
                    log_file = f'{log_path}/no_memory/{attack_type}-aggressive'
                    if read_db:
                        log_file = f'{log_path}/memory_enhanced/{attack_type}-aggressive'
                else:
                    attacker_tools_path = 'data/all_attack_tools_non_aggressive.jsonl'
                    log_file = f'{log_path}/no_memory/{attack_type}-non-aggressive'
                    if read_db:
                        log_file = f'{log_path}/memory_enhanced/{attack_type}-non-aggressive'
                if test:
                    attacker_tools_path = 'data/attack_tools_test_nonagg.jsonl'
                    log_file = f'{log_path}/{attack_type}-test'

                os.makedirs(os.path.dirname(log_file), exist_ok=True)
                print(log_file)

                if injection_method in ['direct_prompt_injection','plan_attack','memory_attack','observation_prompt_injection']:
                    cmd = f'''nohup python main_attacker.py --llm_name {llm} --attack_type {attack_type} --use_backend {backend} --result_file {result_file} --attacker_tools_path {attacker_tools_path} \
                        {f'--{injection_method}' if injection_method else ''} \
                        {f'--database {database}' if database else ''} \
                        {'--write_db' if write_db else ''} \
                        {'--read_db' if read_db else ''} \
                        > {log_file}_{suffix}.log 2>&1 &'''
                elif injection_method in ['cot_backdoor','cot_clean','clean']:
                    cmd = f'''nohup python main_attacker.py --llm_name {llm} --attack_type {attack_type} --use_backend {backend} --result_file {result_file} --attacker_tools_path {attacker_tools_path} \
                        --{injection_method} \
                        --tasks_path {tasks_path} \
                        --trigger '{trigger}' \
                        --task_num {task_num} \
                        > {log_file}_{suffix}.log 2>&1 &'''
                elif injection_method == 'jailbreak':
                    cmd = f'''nohup python main_attacker.py --llm_name {llm} --attack_type {attack_type} --use_backend {backend} --result_file {result_file} --attacker_tools_path {attacker_tools_path} \
                        --{injection_method} \
                        > {log_file}_{suffix}.log 2>&1 &'''
                else:
                    cmd = f'''nohup python main_attacker.py --llm_name {llm} --attack_type {attack_type} --use_backend {backend} --result_file {result_file} --attacker_tools_path {attacker_tools_path} \
                        --{injection_method} \
                        --max_gpu_memory '{max_gpu_memory}' \
                        --eval_device '{eval_devices}' \
                        > {log_file}.log 2>&1 &'''
                # print(cmd)
                os.system(cmd)