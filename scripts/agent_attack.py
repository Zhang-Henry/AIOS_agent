import os


if __name__ == '__main__':
    # eval_devices = ["cuda:7", "cuda:6", "cuda:5", "cuda:4", "cuda:3", "cuda:2", "cuda:1", "cuda:0"]
    # max_gpu_memory = '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB","7": "24GB"}'
    aggressive = False
    test=False

    #######################################################################################################################
    # llm_close_source = ['gpt-4o-mini','gpt-3.5-turbo', 'gpt-4','gemini-1.5-pro','gemini-1.5-flash','claude-3-5-sonnet-20240620','bedrock/anthropic.claude-3-haiku-20240307-v1:0']
    # llm_open_source = ['ollama/llama3:8b', 'ollama/llama3.1:8b','ollama/llama3:70b', 'ollama/llama3.1:70b', \
    #     'ollama/gemma2:9b', 'ollama/gemma2:27b' \
    #     'ollama/mistral-nemo', 'ollama/mixtral:8x7b' \
    #     'ollama/qwen2:7b','ollama/qwen2:72b' \
    #     'ollama/deepseek-coder-v2:16b', \
    #     'ollama/phi3:14b']
    # llms = llm_open_source + llm_close_source
    # attack_types = ['naive', 'context_ignoring', 'fake_completion', 'escape_characters', 'combined_attack']
    # injection_methods = ['direct_prompt_injection', 'observation_prompt_injection']
    # workflow_modes = ['automatic','manual']
    # tasks_path = 'data/agent_task.jsonl'

    #######################################################################################################################

    #######################################################################################################################
    # test
    # test=True
    # aggressive = True
    # llms = ['ollama/llama3.1:70b']
    # attack_types = ['naive']
    # injection_methods = ['direct_prompt_injection']
    # workflow_modes = ['automatic']
    # tasks_path = 'data/agent_task_test.jsonl'
    #######################################################################################################################

    #######################################################################################################################
    # run
    aggressive = False
    llms = ['ollama/deepseek-coder-v2:16b']
    attack_types = ['naive', 'context_ignoring', 'fake_completion', 'escape_characters', 'combined_attack']
    injection_methods = ['direct_prompt_injection', 'observation_prompt_injection']
    workflow_modes = ['automatic']
    tasks_path = 'data/agent_task.jsonl'
    #######################################################################################################################
    for llm in llms:
        for workflow_mode in workflow_modes:
            for attack_type in attack_types:
                for injection_method in injection_methods:
                    # eval_device = eval_devices[attack_types.index(attack_type)]

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
                    os.makedirs(log_path, exist_ok=True)

                    result_file = f'{log_path}/result_statistics.log'

                    if aggressive:
                        attacker_tools_path = 'data/all_attack_tools_aggressive.jsonl'
                        log_file = f'{log_path}/{workflow_mode}-{attack_type}-aggressive.log'
                    else:
                        attacker_tools_path = 'data/all_attack_tools_non_aggressive.jsonl'
                        log_file = f'{log_path}/{workflow_mode}-{attack_type}-non-aggressive.log'

                    if test:
                        attacker_tools_path = 'data/attack_tools_test.jsonl'
                        log_file = f'{log_path}/{workflow_mode}-{attack_type}-test.log'

                    cmd = f'''nohup python main_attacker.py \
                        --llm_name {llm} \
                        --workflow_mode {workflow_mode} \
                        --attack_type {attack_type} \
                        --{injection_method} \
                        --use_backend {backend} \
                        --attacker_tools_path {attacker_tools_path} \
                        --tasks_path {tasks_path} \
                        --result_file {result_file} \
                        > {log_file} 2>&1 &'''
                    # print(cmd)
                    os.system(cmd)