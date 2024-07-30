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
from datetime import datetime

def clean_cache(root_directory):
    targets = {
        ".ipynb_checkpoints",
        "__pycache__",
        ".pytest_cache",
        "context_restoration",
    }
    delete_directories(root_directory, targets)


class Args:
    def __init__(self, attacker_tool, attacker_instruction, expected_achievements, args):
        self.attacker_tool = attacker_tool
        self.attacker_instruction = attacker_instruction
        self.expected_achievements = expected_achievements
        self.workflow_mode = args.workflow_mode
        self.observation_prompt_injection = args.observation_prompt_injection
        self.plan_attack = args.plan_attack
        self.action_attack = args.action_attack
        self.direct_prompt_injection = args.direct_prompt_injection
        self.attack_type = args.attack_type
        self.cot_backdoor= args.cot_backdoor
        self.tools_info_path = args.tools_info_path

    def __str__(self):
        # 打印所有变量
        return str(self.__dict__)

def main():
    start_time = datetime.now()  # 记录开始时间
    print(f"Attack started at: {start_time.strftime('%Y-%m-%d %H:%M')}")

    # parse arguments and set configuration for this run accordingly
    warnings.filterwarnings("ignore")
    parser = parse_global_args()
    args = parser.parse_args()
    print(args)
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
        agent_process_queue=scheduler.agent_process_queue,
        agent_process_factory=agent_process_factory,
        agent_log_mode=agent_log_mode,
    )

    agent_thread_pool = ThreadPoolExecutor(max_workers=5000)

    scheduler.start()

    agent_tasks = list()


    attacker_tools_all = pd.read_json(args.attacker_tools_path, lines=True)

    tasks_path = pd.read_json(args.tasks_path, lines=True)

    for _, agent_info in tasks_path.iterrows(): # iterate over each agent
        agent_name = agent_info["agent_name"]
        agent_path = agent_info["agent_path"]
        tasks = agent_info["tasks"]
        attacker_tools = attacker_tools_all[attacker_tools_all["Corresponding Agent"] == agent_name]

        for i, task in enumerate(tasks): # iterate over each task
            if i >= 1:
                break
            for _, tool in attacker_tools.iterrows(): # iterate over each attacker tool
                print(f'Running agent: {agent_name} with the task: {task} and the attacker tool: {tool["Attacker Tools"]}')
                attacker_tool_args = Args(
                    attacker_tool=tool["Attacker Tools"],
                    attacker_instruction=tool["Attacker Instruction"],
                    expected_achievements=tool["Description"],
                    args=args
                )
                # print("Current task: ", task)
                agent_attack = agent_thread_pool.submit(
                    agent_factory.run_agent,
                    agent_path,
                    task,
                    attacker_tool_args
                )

                agent_tasks.append(agent_attack)

    attack_succ = 0
    workflow_failure = 0
    tool_call_success = 0
    for r in as_completed(agent_tasks):
        _res = r.result()
        print("**********************************")
        if _res["succ"]:
            attack_succ += 1

        print(f"Attack successful.") if _res["succ"] else print(f"Attack failed.")

        if _res['tool_call_success']:
            tool_call_success += 1
            print('Tool calling success.')
        if not _res["succ"]:
            if _res['workflow_failure']:
                workflow_failure += 1
                print('Workflow generation failed.')

        for message in _res["messages"]:
            print(message)

        print("**********************************")

    print(f"Total number of attacks: {len(agent_tasks)}")
    print(f"Number of successful attacks: {attack_succ}")
    print(f'Number of workflow generation failures: {workflow_failure}')
    # print(f'Number of tool calling success: {tool_call_success}')
    print(f"Attack success rate: {attack_succ/len(agent_tasks)}")
    print(f"Attack success rate excluding workflow failure cases: {attack_succ/(len(agent_tasks)-workflow_failure)}")

    scheduler.stop()

    clean_cache(root_directory="./")

    end_time = datetime.now()  # 记录结束时间
    print(f"Attack ended at: {end_time.strftime('%Y-%m-%d %H:%M')}")
    print(f"Total duration: {end_time - start_time}")

if __name__ == "__main__":
    main()
