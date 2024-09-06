import pandas
import csv
import os

prompt_injections = ["direct_prompt_injection", "observation_prompt_injection","memory_attack"]
memory_attacks = ["memory_enhanced"]

for prompt_injection in prompt_injections:
    for memory_attack in memory_attacks:
        model_list = ["gpt-4o-mini","llama3:70b","llama3.1:70b","llama3:8b","llama3.1:8b","gemma2:27b","gemma2:9b","mixtral:8x7b","qwen2:7b","qwen2:72b","vicuna:33b","deepseek-coder-v2:16b"]

        attack_methods = ["combined attack", "context ignoring", "escape characters", "fake completion", "naive"]

        def get_result(file_path, full_tools):
            
            with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
                content = f.readlines()
                f.close()
            
            result = []
            for line in content:
                line_end_num = line.split(' ')
                if len(line_end_num) == 0:
                    continue
                
                try:
                    line_end_num = float(line_end_num[-1])
                except:
                    continue
                
                #print(line_end_num)
                if "Total number of attacks: " in line:
                    result.append(int(line_end_num))
                elif "Number of successful attacks: " in line:
                    result.append(int(line_end_num))
                elif "Number of workflow generation failures: " in line:
                    result.append(int(line_end_num))
                elif "Attack success rate: " in line:
                    result.append("%.3f"%round(line_end_num,3))
                elif "Attack success rate excluding workflow failure cases: " in line:
                    result.append("%.3f"%round(line_end_num,3))
                elif "Number of original task success: " in line:
                    result.append("%.3f"%round(line_end_num,3))
                elif "Original task success rate: " in line:
                    result.append("%.3f"%round(line_end_num,3))
                elif "Refuse judge success number: " in line:
                    result.append(int(line_end_num))
                elif "Refuse judge success rate: " in line:
                    result.append("%.3f"%round(line_end_num,3))
                    if full_tools == "No":
                        result.extend([""] * 2)
                elif "Memory search success number: " in line:
                    result.append(int(line_end_num))
                elif "Memory search success rate: " in line:
                    result.append("%.3f"%round(line_end_num,3))

            return result


        result_csv = pandas.DataFrame(columns = ["LLM", "Attack", "Aggressive", "Attacks num", "Successful attack num", "Plan generation failures num", "ASR", "ASR - plan failure", "Original task success num", "Original task success rate", "Refuse number", "Refuse rate", "Memory search success num", "Memory search success rate", "Full Tools"])


        for model in model_list:
            path = f"./logs/{prompt_injection}/{model}/{memory_attack}"
            for root, dirs, files in os.walk(path, topdown=False):
                files = sorted(files)
                files_list = []
                for name in files:
                    if "-non-" in name:
                        files_list.append(name)
                for name in files:
                    if "-non-" not in name:
                        files_list.append(name)
                
                
                for name in files_list:
                    #print(path + '/' + name)
                    attack_method = name.split('-')[0].replace('_', ' ')
                    if "-non-" in name:
                        agg = 'No'
                    else:
                        agg = 'Yes'
                    
                    if "full_tools" in name:
                        full_tools = 'Yes'
                    else:
                        full_tools = 'No'
                    #print(path + '/' + name)
                    result = [model, attack_method, agg]
                    #print(result)
                    result.extend(get_result(path + '/' + name, full_tools))
                    #print(result)
                    if len(result) != 14:
                        continue
                    #print(result)
                    
                    result.append(full_tools)
                    result_csv.loc[len(result_csv.index)] = result

        result_csv.to_csv(f"./result_csv/result-{prompt_injection}+{memory_attack}.csv", index = False)
