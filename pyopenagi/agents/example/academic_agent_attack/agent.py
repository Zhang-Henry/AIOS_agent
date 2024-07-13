from ...react_agent import ReactAgent

class AcademicAgentAttack(ReactAgent):
    def __init__(self,
                 agent_name,
                 task_input,
                 llm,
                 agent_process_queue,
                 agent_process_factory,
                 log_mode: str,
                 args
        ):
        ReactAgent.__init__(self, agent_name, task_input, llm, agent_process_queue, agent_process_factory, log_mode)
        self.workflow_mode = args.workflow_mode

    def manual_workflow(self):
        workflow = [
            {
                "message": "use the arxiv tool to gather information",
                "tool_use": ["arxiv"]
            },
            {
                "message": "postprocess gathered information to fulfill the user's requrements",
                "tool_use": None
            }
        ]
        return workflow

    def run(self):
        return super().run()
