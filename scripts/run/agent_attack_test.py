import os

def run_main_attacker(llm_name, workflow_mode, attack_type, log_path, injection_method='direct_prompt_injection', max_gpu_memory=None, eval_device=None,backend=None):
    max_gpu_memory_str = f"--max_gpu_memory '{max_gpu_memory}'" if max_gpu_memory else ""
    eval_device_str = f"--eval_device {eval_device}" if eval_device else ""
    cmd = f'''nohup python main_attacker.py \
        --llm_name {llm_name} \
        --workflow_mode {workflow_mode} \
        --attack_type {attack_type} \
        --{injection_method} \
        --use_backend {backend} \
        {max_gpu_memory_str} {eval_device_str} > {log_path} 2>&1 &'''
    print(cmd)
    os.system(cmd)



if __name__ == '__main__':
    gpu_memory = '{"0": "24GB", "1": "24GB","2": "24GB", "3": "24GB", "4": "24GB", "5": "24GB","6": "24GB"}'
    eval_devices = ["cuda:7", "cuda:6", "cuda:5", "cuda:4", "cuda:3", "cuda:2", "cuda:1", "cuda:0"]

    #######################################################################################################################
    # llm_close_source = ['gpt-4o-mini','gpt-3.5-turbo', 'gpt-4','gemini-1.5-pro','gemini-1.5-flash','claude-3-5-sonnet-20240620','bedrock/anthropic.claude-3-haiku-20240307-v1:0']
    # llm_open_source = ['ollama/llama3:8b', 'ollama/llama3.1:8b','ollama/llama3:70b', 'ollama/llama3.1:70b', 'ollama/gemma2:9b', 'google/gemma-7b']
    # llms = llm_open_source + llm_close_source
    # attack_types = ['naive', 'context_ignoring', 'fake_completion', 'escape_characters', 'combined_attack']
    # injection_methods = ['direct_prompt_injection', 'observation_prompt_injection']
    # workflow_modes = ['automatic','manual']
    #######################################################################################################################

    #######################################################################################################################
    # test
    llms = ['google/gemma-7b']
    attack_types = ['naive']
    injection_methods = ['direct_prompt_injection']
    workflow_modes = ['automatic']

    #######################################################################################################################
    for llm in llms:
        for workflow_mode in workflow_modes:
            for attack_type in attack_types:
                for injection_method in injection_methods:
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
                    if not os.path.exists(log_path):
                        os.makedirs(log_path)

                    log_file = f'{log_path}/{workflow_mode}-{attack_type}.log'
                    eval_device = eval_devices[attack_types.index(attack_type)]

                    run_main_attacker(llm, workflow_mode, attack_type, log_file, injection_method, max_gpu_memory=gpu_memory, eval_device=eval_device,backend=backend)
