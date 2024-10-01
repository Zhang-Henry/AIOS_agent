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
python scripts/agent_attack.py --cfg_path config/DPI.yml # direct prompt injection
python scripts/agent_attack.py --cfg_path config/OPI.yml # observation prompt injection
python scripts/agent_attack.py --cfg_path config/MP.yml # memory poisoning attack
python scripts/agent_attack.py --cfg_path config/mixed.yml # mixed attack
python scripts/agent_attack_pot.py # pot backdoor attack
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
| **Gemma2-9B**  | ollama/gemma2:9b   | Open   | 9B              | <div align="center"><img src="./images/google.svg" width="100"/></div>         |
| **Gemma2-27B** | ollama/gemma2:27b   | Open    | 27B             | <div align="center"><img src="./images/google.svg" width="100"/></div>         |
| **LLaMA3-8B**   |ollama/llama3:8b  | Open    | 8B              | <div align="center"><img src="./images/meta.svg" width="200"/></div>           |
| **LLaMA3-70B**  |ollama/llama3:70b  | Open    | 70B             | <div align="center"><img src="./images/meta.svg" width="200"/></div>           |
| **LLaMA3.1-8B**  |ollama/llama3.1:8b | Open    | 8B              | <div align="center"><img src="./images/meta.svg" width="200"/></div>           |
| **LLaMA3.1-70B** |ollama/llama3.1:70b | Open    | 70B             | <div align="center"><img src="./images/meta.svg" width="200"/></div>           |
| **Mixtral-8x7B**   |ollama/mixtral:8x7b  | Open    | 56B             | <div align="center"><img src="./images/mistral.webp" width="100"/></div>     |
| **Qwen2-7B**   |ollama/qwen2:7b   | Open    | 7B              | <div align="center"><img src="./images/alibaba.svg" width="100"/></div>        |
| **Qwen2-72B**   |ollama/qwen2:72b  | Open    | 72B             | <div align="center"><img src="./images/alibaba.svg" width="100"/></div>        |
| **Claude-3.5 Sonnet** |claude-3-5-sonnet-20240620 |  Closed  | 180B            | <div align="center"><img src="./images/anthropic.svg" width="100"/></div>      |
| **GPT-3.5 Turbo** |gpt-3.5-turbo  |  Closed  | 154B            | <div align="center"><img src="./images/openai.svg" width="100"/></div>         |
| **GPT-4o**   |gpt-4o-2024-08-06      |  Closed   | 1.8T            | <div align="center"><img src="./images/openai.svg" width="100"/></div>         |
| **GPT-4o-mini** |gpt-4o-mini   |  Closed   | 8B              | <div align="center"><img src="./images/openai.svg" width="100"/></div>         |

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

================Database Read and Write================
read_db: whether to read the database.

write_db: whether to write the database.

================PoT Backdoor Triggers================
triggers: PoT triggers to use.

================Log Saving================
suffix: To distinguish between different runs, append a unique identifier to the end of the log file name (in logs/).
```

## 📊 Experimental Result
### LLM Capability vs ASR
