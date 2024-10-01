# AIOS Agent

<a href='https://arxiv.org/abs/2403.16971'><img src='https://img.shields.io/badge/Paper-PDF-red'></a>
<a href='https://arxiv.org/abs/2312.03815'><img src='https://img.shields.io/badge/Paper-PDF-blue'></a>
[![Code License](https://img.shields.io/badge/Code%20License-MIT-green.svg)](https://github.com/agiresearch/AIOS/blob/main/LICENSE)
<a href='https://discord.gg/B2HFxEgTJX'><img src='https://img.shields.io/badge/Community-Discord-8A2BE2'></a>

<a href="https://trendshift.io/repositories/8908" target="_blank"><img src="https://trendshift.io/api/badge/repositories/8908" alt="agiresearch%2FAIOS | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

The AIOS Agent aims to systematically formalize and comprehensively evaluate a broad spectrum of adversarial attacks and defensive strategies tailored to LLM-based agents across 10 diverse scenarios, including but not limited to academic advising, counseling, investment, and legal advice.

## ⚔️ LLM Agent Attacking Framework
<p align="center">
<img src="images/LLM Agent Attack.jpg">
</p>

The LLM Agent Attacking Framework includes **DPI**, **OPI**, **Plan-of-Thought (PoT) Backdoor**, and **Memory Poisoning Attacks**, which can compromise the user query, observations, system prompts, and memory retrieval of the agent during action planning and execution.

## ✈️ Getting Started

The development of AIOS Agent Bench is based on [AIOS](https://github.com/agiresearch/AIOS).

### Installation

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

### Quickstart

For details on how to execute each attack method, please consult the `scripts/run.sh` file. The `config/` directory contains YAML files that outline the specific argument settings for each configuration.

```python
python scripts/agent_attack.py --cfg_path config/DPI.yml # direct prompt injection
python scripts/agent_attack.py --cfg_path config/OPI.yml # observation prompt injection
python scripts/agent_attack.py --cfg_path config/MP.yml # memory poisoning attack
python scripts/agent_attack.py --cfg_path config/mixed.yml # mixed attack
python scripts/agent_attack_pot.py # pot backdoor attack
```

### Arguments

Introduction to the customizable parameters in YAML files.
Please uncomment the parameters you want to evaluate in a run.

**Direct Prompt Injection**

```
# config/DPI.yml
================
attack_tool: Tools to attack the target agent.
  - agg: run with aggressive attack tools
  - non-agg: run with non-aggressive attack tools
  - all: run with both tools.

write_db: whether to write the database.

llms: The LLMs to use in the evaluation. Please add "ollama/" for open-source LLMs.
  - gpt-4o-mini: GPT-4o-mini
  - gpt-3.5-turbo: GPT-3.5 Turbo
  - gpt-4o-2024-08-06: GPT-4o
  - claude-3-5-sonnet-20240620: Claude-3.5 Sonnet
  - ollama/qwen2:72b: Qwen2-72B
  - ollama/qwen2:7b: Qwen2-7B
  - ollama/gemma2:9b: Gemma2-9B
  - ollama/gemma2:27b: Gemma2-27B
  - ollama/llama3:70b: LLaMA3-70B
  - ollama/llama3.1:70b: LLaMA3.1-70B
  - ollama/mixtral:8x7b: Mixtral-8x7B
  - ollama/llama3:8b: LLaMA3-8B
  - ollama/llama3.1:8b: : LLaMA3.1-8B

attack_types: The attack types of prompt injection.
  - combined_attack
  - context_ignoring
  - fake_completion
  - escape_characters
  - naive

defense_type: (comment this argument for agent attack)
  - delimiters_defense
  - direct_paraphrase_defense
  - instructional_prevention

suffix: To distinguish between different runs, append a unique identifier to the end of the log file name (in logs/).

```

**Observation Prompt Injection**

```
# config/OPI.yml
================
attack_tool: Tools to attack the target agent.
  - agg: run with aggressive attack tools
  - non-agg: run with non-aggressive attack tools
  - all: run with both tools.

read_db: whether to read the database.

llms: The LLMs to use in the evaluation. Same with Direct Prompt Injection.

attack_types: The attack types of prompt injection.
  - combined_attack
  - context_ignoring
  - fake_completion
  - escape_characters
  - naive

defense_type: (comment this argument for agent attack)
  - delimiters_defense: 
  - ob_sandwich_defense: 
  - instructional_prevention: 

suffix: To distinguish between different runs, append a unique identifier to the end of the log file name (in logs/).

```

**Memory Poisoning Attack**

```
# config/MP.yml
================
attack_tool: Tools to attack the target agent.
  - agg: run with aggressive attack tools
  - non-agg: run with non-aggressive attack tools
  - all: run with both tools.

read_db: whether to read the database. Store true for memory poisoning attack.

llms: The LLMs to use in the evaluation. Same with Direct Prompt Injection.

attack_types: The attack types of prompt injection.
  - combined_attack
  - context_ignoring
  - fake_completion
  - escape_characters
  - naive

defense_type: (comment this argument for agent attack)
  - delimiters_defense
  - direct_paraphrase_defense
  - instructional_prevention

suffix: To distinguish between different runs, append a unique identifier to the end of the log file name (in logs/).

```

**Mixed Attacks**

```
# config/mixed.yml
================
attack_tool: Tools to attack the target agent.
  - agg: run with aggressive attack tools
  - non-agg: run with non-aggressive attack tools
  - all: run with both tools.

read_db: whether to read the database. Store true for memory poisoning attack.

llms: The LLMs to use in the evaluation. Same with Direct Prompt Injection.

attack_types: The attack types of prompt injection.
  - combined_attack
  - context_ignoring
  - fake_completion
  - escape_characters
  - naive

suffix: To distinguish between different runs, append a unique identifier to the end of the log file name (in logs/).

```

**PoT Backdoor Attack**

```
# config/mixed.yml
================
injection_method:
  - cot_backdoor: PoT backdoor attack
  - cot_clean: PoT clean attack
  - clean: No attack

attack_tool: Tools to attack the target agent.
  - agg: run with aggressive attack tools
  - non-agg: run with non-aggressive attack tools
  - all: run with both tools.

llms: The LLMs to use in the evaluation. Same with Direct Prompt Injection.

triggers: PoT triggers to use. 
  - with perspicacious discernment
  - through a prism of insight
  - conducting a comprehensive elucidation
  - ':)'
  - '@_@'

attack_types: we only use naive attack for evaluating the PoT backdoor attack and defense.

defense_type: (comment this argument for agent attack)
  - cot_paraphrase_defense: Paraphrasing
  - cot_shuffling_defense: Shuffle

suffix: To distinguish between different runs, append a unique identifier to the end of the log file name (in logs/).

```