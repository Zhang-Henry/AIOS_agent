from ...react_agent import ReactAgent

class CatFactAgent(ReactAgent):
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
                "message": "use the cat_fact_tool to gather information about cat facts",
                "tool_use": ["cat_fact_tool"]
            },
            {
                "message": "analyze the gathered cat facts to determine the most interesting or unique fact",
                "tool_use": None
            }
        ]
        return workflow

    def analyze_facts(self, facts):
        # Example analysis: find the fact that mentions "heart attack"
        for fact in facts:
            if "heart attack" in fact['text']:
                return fact['text']
        return "No interesting fact found."

    def run(self):
        # Step 1: Use the tool to gather information
        tool_result = self.use_tool("cat_fact_tool")
        
        # Step 2: Analyze the gathered information
        analyzed_result = self.analyze_facts(tool_result)
        
        # Output the final result
        return analyzed_result
