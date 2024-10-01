# AIOS Agent


The AIOS Agent aims to systematically formalize and comprehensively evaluate a broad spectrum of adversarial attacks and defensive strategies tailored to LLM-based agents across 10 diverse scenarios, including but not limited to academic advising, counseling, investment, and legal advice.

## ⚔️ LLM Agent Attacking Framework
<p align="center">
<img src="images/LLM Agent Attack.jpg">
</p>

The LLM Agent Attacking Framework includes **DPI**, **OPI**, **Plan-of-Thought (PoT) Backdoor**, and **Memory Poisoning Attacks**, which can compromise the user query, observations, system prompts, and memory retrieval of the agent during action planning and execution.

## ✈️ Getting Started

The development of AIOS Agent Bench is based on [AIOS](https://github.com/agiresearch/AIOS).

### Environment Installation

Git clone AIOS Agent
```bash
git clone https://github.com/Zhang-Henry/AIOS_agent.git
```
```bash
conda create -n AIOS python=3.11
source activate AIOS
cd AIOS
```
If you have GPU environments, you can install the dependencies using
```bash
pip install -r requirements-cuda.txt
```
or else you can install the dependencies using
```bash
pip install -r requirements.txt
```

### Use with ollama
You need to download ollama from from https://ollama.com/.

Then you need to start the ollama server either from ollama app

or using the following command in the terminal

```bash
ollama serve
```

To use models provided by ollama, you need to pull the available models from https://ollama.com/library

```bash
ollama pull llama3:8b # use llama3:8b for example
```

ollama can support CPU-only environment, so if you do not have CUDA environment

You can run aios with ollama models by

```python
python main.py --llm_name ollama/llama3:8b --use_backend ollama # use ollama/llama3:8b for example
```

However, if you have the GPU environment, you can also pass GPU-related parameters to speed up
using the following command

```python
python main.py --llm_name ollama/llama3:8b --use_backend ollama --max_gpu_memory '{"0": "24GB"}' --eval_device "cuda:0" --max_new_tokens 256
```


### Quickstart

For details on how to execute each attack method, please consult the `scripts/run.sh` file. The `config/` directory contains YAML files that outline the specific argument settings for each configuration.

```python
python scripts/agent_attack.py --cfg_path config/DPI.yml # Direct Prompt Injection
python scripts/agent_attack.py --cfg_path config/OPI.yml # Observation Prompt Injection
python scripts/agent_attack.py --cfg_path config/MP.yml # Memory Poisoning attack
python scripts/agent_attack.py --cfg_path config/mixed.yml # Mixed attack
python scripts/agent_attack_pot.py # PoT backdoor attack
```

### Customizable Arguments

The customizable arguments are stored in YAML files in `config/`.
Please list the arguments you want to evaluate in a run. For example, if you want to run **GPT-4o** and **LLaMA3.1-70B** at the same time, you should set llms in the following format in YAML files.
```
llms:
  - gpt-4o-2024-08-06
  - ollama/llama3.1:70b
```

### Available LLMs in AIOS Agent
Here are the open-source and closed-source LLMs we used in AIOS agent.

| **LLM**               |**YAML Argument**| **Source**| **#Parameters** | **Provider**   |
|-----------------------|----|-------------|---------|-------|
|  <div align="center">**Gemma2-9B**</div>| <div align="center">ollama/gemma2:9b</div>   | <div align="center">Open</div>   | <div align="center">9B</div>              | <div align="center"><img src="./images/google.svg" width="100"/></div>         |
| <div align="center">**Gemma2-27B** | <div align="center">ollama/gemma2:27b</div>   | <div align="center">Open</div>    | <div align="center">27B</div>             | <div align="center"><img src="./images/google.svg" width="100"/></div>         |
| <div align="center">**LLaMA3-8B**   | <div align="center">ollama/llama3:8b</div>  | <div align="center">Open</div>    | <div align="center">8B</div>              | <div align="center"><img src="./images/meta.svg" width="100"/></div>           |
| <div align="center">**LLaMA3-70B**  | <div align="center">ollama/llama3:70b</div>  | <div align="center">Open</div>    | <div align="center">70B</div>             | <div align="center"><img src="./images/meta.svg" width="100"/></div>           |
| <div align="center">**LLaMA3.1-8B**  | <div align="center">ollama/llama3.1:8b</div> | <div align="center">Open</div>    | <div align="center">8B</div>              | <div align="center"><img src="./images/meta.svg" width="100"/></div>           |
| <div align="center">**LLaMA3.1-70B** | <div align="center">ollama/llama3.1:70b</div> | <div align="center">Open</div>    | <div align="center">70B</div>             | <div align="center"><img src="./images/meta.svg" width="100"/></div>           |
| <div align="center">**Mixtral-8x7B**</div>   |<div align="center">ollama/mixtral:8x7b</div>  | <div align="center">Open</div>    | <div align="center">56B</div>             | <div align="center"><img src="./images/mistral.webp" width="100"/></div>     |
| <div align="center">**Qwen2-7B**</div>   | <div align="center">ollama/qwen2:7b</div>   | <div align="center">Open</div>    | <div align="center">7B</div>              | <div align="center"><img src="./images/alibaba.svg" width="100"/></div>        |
| <div align="center">**Qwen2-72B**</div>   | <div align="center">ollama/qwen2:72b</div>  | <div align="center">Open</div>    | <div align="center">72B</div>             | <div align="center"><img src="./images/alibaba.svg" width="100"/></div>        |
| <div align="center">**Claude-3.5 Sonnet**</div> |<div align="center">claude-3-5-sonnet-20240620</div> |  <div align="center">Closed</div>  | <div align="center">180B</div>            | <div align="center"><img src="./images/anthropic.svg" width="300"/></div>      |
| <div align="center">**GPT-3.5 Turbo**</div> | <div align="center">gpt-3.5-turbo</div>  |  Closed  | <div align="center">154B</div>            | <div align="center"><img src="./images/openai.svg" width="100"/></div>         |
| <div align="center">**GPT-4o**</div>   | <div align="center">gpt-4o-2024-08-06</div>      |  <div align="center">Closed</div>   | <div align="center">8T</div>            | <div align="center"><img src="./images/openai.svg" width="100"/></div>         |
| <div align="center">**GPT-4o-mini**</div>  | <div align="center">gpt-4o-mini</div>   |  <div align="center">Closed</div>   | <div align="center">8B</div>              | <div align="center"><img src="./images/openai.svg" width="100"/></div>         |

### Agent Attacks
<p align="center">
<img src="images/Agent Attacks.png">
</p>

DPI tampers with the user prompt, OPI alters observation data to disrupt subsequent actions, PoT Backdoor Attack triggers concealed actions upon encountering specific inputs, and Memory Poisoning Attack injects malicious plans into the agent’s memory, thereby compelling the agent to employ attacker-specified tools.

Here are the yaml arguments representation for the agent attacks and corresponding defenses. **The attack method in parentheses in the last column indicates the corresponding defense's target attack method.**
| **Attacks**      | **YAML Argument**               | **Defenses**              | **YAML Argument**                                                                                          |
|------------------|---------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------|
| <div align="center">**DPI**</div>          | <div align="center">direct_prompt_injection</div>         | <div align="center">**Delimiters**</div>             | <div align="center">delimiters_defense (DPI, OPI)</div>                                                                               |
| <div align="center">**OPI**</div>          | <div align="center">observation_prompt_injection</div>    | <div align="center">**Sandwich Prevention**</div>    | <div align="center">ob_sandwich_defense (OPI)</div>                                                                                   |
| <div align="center">**Memory Poisoning**</div> | <div align="center">memory_attack               | <div align="center">**Instructional Prevention**</div> | <div align="center">instructional_prevention (DPI, OPI)</div>                                                                         |
| <div align="center">**PoT Backdoor**</div> | <div align="center">pot_backdoor                    | <div align="center">**Paraphrasing**</div>           | <div align="center">direct_paraphrase_defense (DPI) pot_paraphrase_defense (PoT)</div>                                                |
| <div align="center">**PoT Clean**</div>    | <div align="center">pot_clean                      | <div align="center">**Shuffle**</div>                | <div align="center">pot_shuffling_defense (PoT)</div>                                                                                 


### Other Customizable Agruments
```
================Attacks & Defenses================
attack_tool: Tools to attack the target agent.
  - agg: run with aggressive attack tools
  - non-agg: run with non-aggressive attack tools
  - all: run with both tools.

llms: The LLMs to use in the evaluation. Please add "ollama/" for open-source LLMs.

attack_types: The attack types of prompt injection.

defense_type: The defense types of corresponding attacks. 
Please note that a defense type only corresponds to some attacks types, not all.

================Database Read and Write================
read_db: whether to read the database.

write_db: whether to write the database.

================PoT Backdoor Triggers================
triggers: PoT triggers to use.

================Log Saving================
suffix: To distinguish between different runs, append a unique identifier to the end of the log file name (in logs/).
```

## 📊 Experimental Result

### Agent Attack
| **LLM**            |       | **DPI** ASR | **DPI** RR |       | **OPI** ASR | **OPI** RR |       | **Memory Poisoning** ASR | **Memory Poisoning** RR |       | **Mixed Attack** ASR | **Mixed Attack** RR |       | **PoT Backdoor** ASR | **PoT Backdoor** RR |       | **Average** ASR | **Average** RR |
|--------------------|-------|-------------|------------|-------|-------------|------------|-------|--------------------------|-------------------------|-------|----------------------|---------------------|-------|-----------------------|----------------------|-------|----------------|----------------|
| **Gemma2-9B**      |       | 87.10%      | 4.30%      |       | 14.20%      | 15.00%     |       | 6.85%                    | 9.85%                   |       | 92.17%                | 1.33%               |       | 39.75%                | 5.25%                |       | 48.01%         | 7.15%          |
| **Gemma2-27B**     |       | 96.75%      | 0.90%      |       | 14.20%      | 3.90%      |       | 6.25%                    | 5.45%                   |       | **100.00%**           | 0.50%               |       | 54.50%                | 3.50%                |       | 54.34%         | 2.85%          |
| **LLaMA3-8B**      |       | 25.20%      | 7.45%      |       | 10.55%      | 3.00%      |       | 3.30%                    | 5.45%                   |       | 40.75%                | 5.75%               |       | 21.50%                | 2.50%                |       | 20.26%         | 4.83%          |
| **LLaMA3-70B**     |       | 86.15%      | 7.80%      |       | 43.70%      | 3.00%      |       | 1.85%                    | 1.80%                   |       | 85.50%                | 6.50%               |       | 57.00%                | 2.00%                |       | 54.84%         | 4.22%          |
| **LLaMA3.1-8B**    |       | 51.10%      | 5.20%      |       | 6.40%       | 1.85%      |       | **25.65%**               | 6.75%                   |       | 73.50%                | 3.50%               |       | 19.00%                | 5.75%                |       | 35.13%         | 4.61%          |
| **LLaMA3.1-70B**   |       | 85.65%      | 5.30%      |       | 12.10%      | 4.95%      |       | 2.85%                    | 2.20%                   |       | 94.50%                | 1.25%               |       | 59.75%                | 6.25%                |       | 50.97%         | 3.99%          |
| **Mixtral-8x7B**   |       | 25.85%      | 9.55%      |       | 4.80%       | 8.55%      |       | 4.90%                    | 1.35%                   |       | 54.75%                | **6.75%**           |       | 4.75%                 | **13.25%**           |       | 19.01%         | 7.89%          |
| **Qwen2-7B**       |       | 55.20%      | 7.70%      |       | 9.00%       | 6.00%      |       | 2.85%                    | 4.95%                   |       | 76.00%                | 2.50%               |       | 12.25%                | 4.50%                |       | 31.06%         | 5.13%          |
| **Qwen2-72B**      |       | 86.95%      | 4.20%      |       | 21.35%      | 16.55%     |       | 3.95%                    | 5.45%                   |       | 98.50%                | 0.75%               |       | 57.75%                | 4.75%                |       | 53.70%         | 6.34%          |
| **Claude3.5 Sonnet**|      | 90.75%      | 7.65%      |       | 59.70%      | **25.50%** |       | 19.75%                   | 1.20%                   |       | 94.50%                | 6.25%               |       | 17.50%                | 11.75%               |       | 56.44%         | **10.47%**     |
| **GPT-3.5 Turbo**  |       | **98.40%**  | 3.00%      |       | 55.10%      | 16.85%     |       | 9.30%                    | 0.30%                   |       | 99.75%                | 0.00%               |       | 8.25%                 | 10.75%               |       | 54.16%         | 6.18%          |
| **GPT-4o**         |       | 60.35%      | **20.05%** |       | **62.45%**  | 6.50%      |       | 10.00%                   | **11.75%**              |       | 89.25%                | 5.50%               |       | **100.00%**           | 0.25%                |       | 64.41%         | 8.81%          |
| **GPT-4o-mini**    |       | 95.45%      | 1.85%      |       | 44.55%      | 0.25%      |       | 5.50%                    | 3.65%                   |       | 96.75%                | 1.25%               |       | 95.50%                | 0.00%                |       | **67.55%**     | 1.40%          |
| **Average**        |       | 72.68%      | 6.53%      |       | 27.55%      | 8.61%      |       | 7.92%                    | 4.63%                   |       | **84.30%**            | 3.22%               |       | 42.12%                | 5.42%                |       | 46.91%         | 5.68%          |


### Agent Defense


### LLM Capability vs ASR

## ⚖️ Ethics Statement

This research advances the development of secure and trustworthy AI systems by investigating adversarial attacks and defensive strategies on language models (LLMs). By identifying and addressing vulnerabilities, we aim to enhance the robustness and safety of AI systems, facilitating their responsible deployment in critical applications. No human subjects were involved in this study, and all datasets used comply with privacy and ethical standards. Our work is committed to advancing AI technology in a manner that ensures fairness, security, and societal benefit.


## 💻 Reproducibility Statement

We have implemented the following measures to ensure the reproducibility of our work on the AIOS Agent framework:

+ **Code Availability**: The source code for the AIOS Agent, including all scripts, configuration files, and Docker setup for executing LLM agent attacks, is available on the project's GitHub repository. The repository contains scripts for adversarial attacks such as Direct Prompt Injection (DPI), Observation Prompt Injection (OPI), Memory Poisoning attacks, and PoT Backdoor attacks.

+ **Dependencies**: The environment setup is streamlined through both `requirements.txt` and `requirements-cuda.txt` for systems with or without GPU support. Installation instructions using Conda or Docker (for containerized environments) are provided to ensure consistency across different hardware configurations.

+ **Experimental Configurations**: All experimental configurations, including LLM models and attack types, are defined in YAML files within the `config/` directory. These configurations can be modified to test different models such as GPT-4, LLaMA, and other open-source models through Ollama and HuggingFace integrations.

+ **External Tools**: The AIOS Agent supports multiple LLM backends (OpenAI, Gemini, HuggingFace), and instructions for obtaining necessary API keys and setting up the environment are documented.

+ **Reproducibility of Results**: To facilitate easy replication of the experiments, we provide predefined attack scripts (e.g., `scripts/agent_attack.py`) that allow for direct execution of various adversarial attacks under different configurations.