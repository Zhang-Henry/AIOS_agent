# This is a main script that tests the functionality of specific agents.
# It requires no user input.


from aios.scheduler.fifo_scheduler import FIFOScheduler


from aios.utils.utils import (
    parse_global_args,
)

from pyopenagi.agents.agent_factory import AgentFactory

from pyopenagi.agents.agent_process import AgentProcessFactory

import warnings

from aios.llm_core import llms

from concurrent.futures import ThreadPoolExecutor, as_completed


from aios.utils.utils import delete_directories
from dotenv import load_dotenv
import pandas as pd
from tqdm import tqdm

def clean_cache(root_directory):
    targets = {
        ".ipynb_checkpoints",
        "__pycache__",
        ".pytest_cache",
        "context_restoration",
    }
    delete_directories(root_directory, targets)

class Args:
    def __init__(self, attacker_tool=None, attacker_instruction=None, expected_achievements=None, workflow_mode=None, observation_prompt_injection=False):
        self.attacker_tool = attacker_tool
        self.attacker_instruction = attacker_instruction
        self.expected_achievements = expected_achievements
        self.workflow_mode = workflow_mode
        self.observation_prompt_injection = observation_prompt_injection


def main():
    # parse arguments and set configuration for this run accordingly
    warnings.filterwarnings("ignore")
    parser = parse_global_args()
    args = parser.parse_args()

    llm_name = args.llm_name
    max_gpu_memory = args.max_gpu_memory
    eval_device = args.eval_device
    max_new_tokens = args.max_new_tokens
    scheduler_log_mode = args.scheduler_log_mode
    agent_log_mode = args.agent_log_mode
    llm_kernel_log_mode = args.llm_kernel_log_mode
    use_backend = args.use_backend

    load_dotenv()

    llm = llms.LLMKernel(
        llm_name=llm_name,
        max_gpu_memory=max_gpu_memory,
        eval_device=eval_device,
        max_new_tokens=max_new_tokens,
        log_mode=llm_kernel_log_mode,
        use_backend=use_backend
    )

    # run agents concurrently for maximum efficiency using a scheduler

    scheduler = FIFOScheduler(llm=llm, log_mode=scheduler_log_mode)

    agent_process_factory = AgentProcessFactory()

    agent_factory = AgentFactory(
        llm=llm,
        agent_process_queue=scheduler.agent_process_queue,
        agent_process_factory=agent_process_factory,
        agent_log_mode=agent_log_mode,
    )

    agent_thread_pool = ThreadPoolExecutor(max_workers=500)

    scheduler.start()

    agent_tasks = list()
    attacker_tools = pd.read_json(args.attacker_tools_path, lines=True)

    with open('data/agent_tasks/example/academic_agent_task.txt', 'r') as file:
        agent_tasks = file.readlines()
    for task in agent_tasks:
        for _, attacker_tool_info in attacker_tools.iterrows():
            attacker_tool_args = Args(
                attacker_tool=attacker_tool_info["Attacker Tools"][0],
                attacker_instruction=attacker_tool_info["Attacker Instruction"],
                expected_achievements=attacker_tool_info["Expected Achievements"],
                workflow_mode=args.workflow_mode,
                observation_prompt_injection=args.observation_prompt_injection,
            )
            academic_agent_attack = agent_thread_pool.submit(
                agent_factory.run_agent,
                "example/academic_agent_attack",
                task,
                attacker_tool_args
            )

            agent_tasks.append(academic_agent_attack)

    attack_succ = 0
    for r in as_completed(agent_tasks):
        _res = r.result()
        print("**********************************")
        if _res["succ"]:
            attack_succ += 1
        print(f"Attack successful.") if _res["succ"] else print(f"Attack failed.")
        print(_res)
        print("**********************************")

    print(f"Total number of attacks: {len(agent_tasks)}")
    print(f"Number of successful attacks: {attack_succ}")
    print(f"Attack success rate: {attack_succ/len(agent_tasks)}")

    scheduler.stop()

    clean_cache(root_directory="./")


if __name__ == "__main__":
    main()
