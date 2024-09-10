import pandas
import csv
import os

# prompt_injections = ["direct_prompt_injection", "observation_prompt_injection","memory_attack"]
prompt_injections = ["clean", "cot_backdoor","cot_clean"]
memory_attacks = ["no_memory"]
# memory_attacks = ["no_memory","memory_enhanced"]
agg_result = []
non_agg_result = []

for prompt_injection in prompt_injections:
    for memory_attack in memory_attacks:
        model_list = ["gpt-4o-mini","llama3:70b","llama3.1:70b","llama3:8b","llama3.1:8b","gemma2:27b","gemma2:9b","mixtral:8x7b","qwen2:7b","qwen2:72b"]

        attack_methods = ["combined attack", "context ignoring", "escape characters", "fake completion", "naive"]

        def get_result(file_path):

            with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
                content = f.readlines()

            result = []
            for line in content:
                line_end_num = line.split(' ')
                if len(line_end_num) == 0:
                    continue

                try:
                    line_end_num = float(line_end_num[-1])
                except:
                    continue

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
                elif "Memory search success number: " in line and memory_attack == 'memory_enhanced':
                    result.append(int(line_end_num))
                elif "Memory search success rate: " in line and memory_attack == 'memory_enhanced':
                    result.append("%.3f"%round(line_end_num,3))

            return result

        if memory_attack == 'memory_enhanced':
            result_csv = pandas.DataFrame(columns = ["LLM", "Attack", "Aggressive", "Attacks num", "Successful attack num", "Plan generation failures num", "ASR", "ASR - plan failure", "Original task success num", "Original task success rate", "Refuse number", "Refuse rate", "Memory search success num", "Memory search success rate"])
        elif memory_attack == 'no_memory':
            result_csv = pandas.DataFrame(columns = ["LLM", "Attack", "Aggressive", "Attacks num", "Successful attack num", "Plan generation failures num", "ASR", "ASR - plan failure", "Original task success num", "Original task success rate", "Refuse number", "Refuse rate"])

        for model in model_list:
            path = f"./logs/{prompt_injection}/{model}/{memory_attack}"
            agg_result = []
            non_agg_result = []
            for root, dirs, files in os.walk(path, topdown=False):
                files = sorted(files)
                files_list = []
                # Process only files with 'full_tools.log' suffix
                for name in files:
                    # print(name)
                    # if memory_attack == 'memory_enhanced':
                    # if name.endswith("full_tools.log"):
                    files_list.append(name)
                    # elif memory_attack == 'no_memory':
                    #     files_list.append(name)
                            # print(files_list)

                for name in files_list:
                    attack_method = name.split('-')[0].replace('_', ' ')
                    if "-non-" in name:
                        agg = 'No'
                    else:
                        agg = 'Yes'

                    result = [model, attack_method, agg]
                    result.extend(get_result(path + '/' + name))
                    #print(len(result))
                    # Ensure the correct length of result
                    if len(result) != 14 and memory_attack == 'memory_enhanced':
                        print(path + '/' + name)
                        continue
                    elif len(result) != 12 and memory_attack == 'no_memory':
                        print(path + '/' + name)
                        continue

                    if agg == "No":
                        non_agg_result.append(result)
                    else:
                        agg_result.append(result)

                    #result_csv.loc[len(result_csv.index)] = result
            for result in non_agg_result:
                result_csv.loc[len(result_csv.index)] = result
            for result in agg_result:
                result_csv.loc[len(result_csv.index)] = result

        result_csv.to_csv(f"./result_csv/result-{prompt_injection}+{memory_attack}.csv", index = False)
