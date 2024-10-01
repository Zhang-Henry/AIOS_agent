import os, yaml

if __name__ == '__main__':

    with open('config/DPI.yml', 'r') as file:
        cfg = yaml.safe_load(file)

    llms = cfg.get('llms', None)
    suffix = cfg.get('suffix', None)
    attack_tool_types = cfg.get('attack_tool', None)
    write_db = cfg.get('write_db', None)
    read_db = cfg.get('read_db', None)
    defense_type = cfg.get('defense_type', None)
    injection_method = cfg['injection_method'] # 'direct_prompt_injection', 'memory_attack', 'observation_prompt_injection', 'clean'
    attack_types = cfg.get('attack_types', None)


    for attack_tool_type in attack_tool_types:
        for llm in llms:
            for attack_type in attack_types:
                if llm.startswith('gpt') or llm.startswith('gemini') or llm.startswith('claude'):
                    llm_name = llm
                    backend=None
                elif llm.startswith('ollama'):
                    llm_name = llm.split('/')[-1]
                    backend='ollama'

                log_path = f'logs/{injection_method}/{llm_name}'
                database = f'memory_db/direct_prompt_injection/{attack_type}_gpt-4o-mini'



                log_memory_type = 'new_memory' if read_db else 'no_memory'
                log_file = f'{log_path}/{defense_type}/{attack_type}-{attack_tool_type}' if defense_type else f'{log_path}/{log_memory_type}/{attack_type}-{attack_tool_type}'
                os.makedirs(os.path.dirname(log_file), exist_ok=True)
                print(log_file)

                if injection_method in ['direct_prompt_injection','memory_attack','observation_prompt_injection','clean']:
                    cmd = f'''nohup python main_attacker.py --llm_name {llm} --attack_type {attack_type} --use_backend {backend} --attacker_tools_path {attacker_tools_path} \
                        {f'--{injection_method}' if injection_method else ''} \
                        {f'--database {database}' if database else ''} \
                        {f'--defense_type {defense_type}' if defense_type else ''} \
                        {'--write_db' if write_db else ''} \
                        {'--read_db' if read_db else ''} \
                        > {log_file}_{suffix}.log 2>&1 &'''
                elif injection_method in ['mixed_attack']:
                    cmd = f'''nohup python main_attacker.py --llm_name {llm} --attack_type {attack_type} --use_backend {backend} --attacker_tools_path {attacker_tools_path} \
                        --direct_prompt_injection \
                        --observation_prompt_injection \
                        {f'--database {database}' if database else ''} \
                        --read_db True \
                        > {log_file}_{suffix}.log 2>&1 &'''

                os.system(cmd)

