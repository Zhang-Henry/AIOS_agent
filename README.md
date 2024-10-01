# AIOS Agent

<a href='https://arxiv.org/abs/2403.16971'><img src='https://img.shields.io/badge/Paper-PDF-red'></a>
<a href='https://arxiv.org/abs/2312.03815'><img src='https://img.shields.io/badge/Paper-PDF-blue'></a>
[![Code License](https://img.shields.io/badge/Code%20License-MIT-green.svg)](https://github.com/agiresearch/AIOS/blob/main/LICENSE)
<a href='https://discord.gg/B2HFxEgTJX'><img src='https://img.shields.io/badge/Community-Discord-8A2BE2'></a>

<a href="https://trendshift.io/repositories/8908" target="_blank"><img src="https://trendshift.io/api/badge/repositories/8908" alt="agiresearch%2FAIOS | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

The goal of AIOS is to build a large language model (LLM) agent operating system, which intends to embed large language model into the operating system as the brain of the OS. AIOS is designed to address problems (e.g., scheduling, context switch, memory management, etc.) during the development and deployment of LLM-based agents, for a better ecosystem among agent developers and users.

## ⚔️ LLM Agent Attacking Framework
<p align="center">
<img src="images/LLM Agent Attack.jpg">
</p>

The LLM Agent Attacking Framework includes **DPI**, **OPI**, **Plan-of-Thought (PoT) Backdoor**, and **Memory Poisoning Attacks**, which can influence the user query, observations, system prompts, and memory retrieval of the agent during action planning and execution.

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

Introduction to the parameters in YAML files.

**Direct Prompt Injection**

```
# config/DPI.yml
================
attack_tool:

write_db:

llms:

attack_types:

defense_type:

suffix: 

```

**Observation Prompt Injection**

```
# config/OPI.yml
================
attack_tool:

llms:

attack_types:

defense_type:

suffix: 

```

**Memory Poisoning Attack**

```
# config/MP.yml
================
attack_tool:

llms:

attack_types:

defense_type:

suffix: 

```

**Mixed Attacks**

```
# config/mixed.yml
================
attack_tool:

llms:

attack_types:

defense_type:

suffix: 

```

**PoT Backdoor Attack**

```
# config/mixed.yml
================
attack_tool:

llms:

attack_types:

defense_type:

suffix: 

```