import pandas
import csv
import os
import sys

prompt_injections=["direct_prompt_injection"]
# 'direct_prompt_injection',"observation_prompt_injection",'mixed_attack',"memory_attack","clean",'DPI_MP','OPI_MP','DPI_OPI'
dirs = ['dynamic_prompt_rewriting'] # new_memory, no_memory, direct_paraphrase_defense, instructional_prevention, delimiters_defense, ob_sandwich_defense
agg_result = []
non_agg_result = []

for prompt_injection in prompt_injections:
    for dir in dirs:
        model_list = ['gpt-3.5-turbo',"gpt-4o-mini","llama3:70b","llama3.1:70b","llama3:8b","llama3.1:8b","gemma2:27b","gemma2:9b","mixtral:8x7b","qwen2:7b","qwen2:72b",'gpt-4o-2024-08-06','claude-3-5-sonnet-20240620']
        #model_list = ["gemma2:9b"]

        data_dict = {"Attack Num": 0, "Successful Attack Num": 0, "Refuse Number": 0, "ASR": 0, "Refuse rate": 0}

        attack_methods = ["combined_attack", "context_ignoring", "escape_characters", "fake_completion", "naive"]
        agent_names = ['education_consultant_agent', 'system_admin_agent', 'ecommerce_manager_agent', 'psychological_counselor_agent', 'autonomous_driving_agent', 'legal_consultant_agent', 'aerospace_engineer_agent', 'academic_search_agent', 'medical_advisor_agent', 'financial_analyst_agent']

        def get_result(file_path):
            # Read CSV
            result = None
            #print(file_path)
            df = pandas.read_csv(file_path)
            for index, row in df.iterrows():
                data_dict["Attack Num"] += 1
                data_dict["Successful Attack Num"] += row["Attack Successful"]
                #data_dict[agent_name]["Refuse Number"] += row["Refuse Result"]
            return result

        columns = ["Model", "Attack Num", "Successful Attack Num", "Refuse Number", "ASR", "Refuse rate"]
        result_csv = pandas.DataFrame(columns = columns)

        for model in model_list:
            try:
                result = [model]
                data_dict = {"Attack Num": 0, "Successful Attack Num": 0, "Refuse Number": 0, "ASR": 0, "Refuse rate": 0}
                for attack_method in attack_methods:
                    path = f"./logs/{prompt_injection}/{model}/{dir}/{attack_method}-all_.csv"
                    #print(path)
                    get_result(path)
                
                data_dict["ASR"] = data_dict["Successful Attack Num"] / data_dict["Attack Num"]
                data_dict["Refuse rate"] = data_dict["Refuse Number"] / data_dict["Attack Num"]
                for column in columns[1:]:
                    result.append(data_dict[column])
                result_csv.loc[len(result_csv.index)] = result
            except:
                print(f"{model} has not ready yet.")
                pass

        result_csv.to_csv(f"./result_csv/result-agent-defense-0931-{dir}.csv", index = False)

        #print(data_dict)
