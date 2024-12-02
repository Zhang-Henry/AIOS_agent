import pandas,re
import csv
import os
import sys
import traceback

prompt_injections=['direct_prompt_injection', "observation_prompt_injection", "memory_attack"] # 'direct_prompt_injection',"observation_prompt_injection",'mixed_attack',"memory_attack","clean",'DPI_MP','OPI_MP','DPI_OPI'
dirs = ['no_memory'] # new_memory, no_memory, direct_paraphrase_defense, instructional_prevention, delimiters_defense, ob_sandwich_defense, dynamic_prompt_rewriting
agg_result = []
non_agg_result = []

for prompt_injection in prompt_injections:
    if prompt_injection == "memory_attack":
        dirs = ["new_memory"]
    # else:
    #     dirs = ["no_memory"]
    for dir in dirs:
        model_list = ["gemma2:9b","gemma2:27b","llama3:8b","llama3:70b","llama3.1:8b","llama3.1:70b","mixtral:8x7b","qwen2:7b","qwen2:72b",'claude-3-5-sonnet-20240620','gpt-3.5-turbo',"gpt-4o-mini",'gpt-4o-2024-08-06']
        attack_methods = ["combined_attack", "context_ignoring", "escape_characters", "fake_completion", "naive"] # "combined_attack", "context_ignoring", "escape_characters", "fake_completion", "naive"
        # attack_methods = ["combined_attack"]
        agent_names = ['financial_analyst_agent']

        data_dict = {}
        for agent_name in agent_names:
            data_dict[agent_name] = {"Attack Num": 0, "Successful Attack Num": 0, "Refuse Number": 0, "ASR": 0, "Refuse rate": 0}

        def get_result(file_path):
            # Read CSV
            result = None
            df = pandas.read_csv(file_path)
            if len(df) < 400:
                print(file_path, len(df))

            for index, row in df.iterrows():
                agent_name = row["Agent Name"][8:]
                if agent_name not in agent_names:
                    continue
                data_dict[agent_name]["Attack Num"] += 1
                data_dict[agent_name]["Successful Attack Num"] += row["Attack Successful"]
                # print(type(row["Refuse Result"]), row["Refuse Result"])
                if isinstance(row["Refuse Result"], str):
                    numbers = re.findall(r'\d+', row["Refuse Result"])
                    data_dict[agent_name]["Refuse Number"] += int(numbers[0])
                else:
                    data_dict[agent_name]["Refuse Number"] += int(row["Refuse Result"])
            return result

        columns = ["Model", "Agent", "Attack Num", "Successful Attack Num", "Refuse Number", "ASR", "Refuse rate"]
        result_csv = pandas.DataFrame(columns = columns)

        for model in model_list:
            try:
                data_dict[agent_name] = {"Attack Num": 0, "Successful Attack Num": 0, "Refuse Number": 0, "ASR": 0, "Refuse rate": 0}
                for attack_method in attack_methods:
                    path = f"./logs/{prompt_injection}/{model}/{dir}/{attack_method}-all_.csv"
                    get_result(path)
                for agent_name in data_dict.keys():
                    data_dict[agent_name]["ASR"] = data_dict[agent_name]["Successful Attack Num"] / data_dict[agent_name]["Attack Num"]
                    if prompt_injection != "direct_prompt_injection":
                        data_dict[agent_name]["Refuse rate"] = 1-(data_dict[agent_name]["Refuse Number"] / data_dict[agent_name]["Attack Num"])
                    else:
                        data_dict[agent_name]["Refuse rate"] = (data_dict[agent_name]["Refuse Number"] / data_dict[agent_name]["Attack Num"])
                    result = [model, agent_name]
                    for column in columns[2:]:
                        result.append(data_dict[agent_name][column])
                    result_csv.loc[len(result_csv.index)] = result
            
            except Exception as e:  # 捕获所有异常
                print(f"{model} has not ready yet.")
                print("Error details:")
                traceback.print_exc()  # 打印完整的异常堆栈信息

        #print(data_dict)
        print(f'Saving to: ./result_csv/result-agent-1834-fin-{prompt_injection}.csv')
        result_csv.to_csv(f"./result_csv/result-agent-1834-fin-{prompt_injection}.csv", index = False)
