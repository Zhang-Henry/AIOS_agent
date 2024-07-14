from ...react_agent import ReactAgent

class SportAgent(ReactAgent):
    def __init__(self,
                 agent_name,
                 task_input,
                 llm,
                 agent_process_queue,
                 agent_process_factory,
                 log_mode: str,
                 args
        ):
        SportAgent.__init__(self, agent_name, task_input, llm, agent_process_queue, agent_process_factory, log_mode)
        self.workflow_mode = args.workflow_mode

    def manual_workflow(self):
        workflow = [
            {
                "message": "try to understand the user's requirements",
                "tool_use": None
            },
            {
                "message": "pick up the leagues that the players pay attentions to",
                "tool_use": None
            },
            {
                "message": "use the sportmonks tool to gather data from those leagues",
                "tool_use": ["sportmonks"]
            },
            {
                "message": "postprocess gathered information to fulfill the user's requrements",
                "tool_use": ["sportmonks"]
            }
        ]
        return workflow

    def run(self):
        return super().run()
