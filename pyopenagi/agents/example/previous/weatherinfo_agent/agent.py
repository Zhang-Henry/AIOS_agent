from ...react_agent import ReactAgent

class WeatherAgent(ReactAgent):
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
                "message": "use the weather_tool to gather current weather information",
                "tool_use": ["weather_tool"]
            },
            {
                "message": "analyze the gathered weather information to provide a concise weather summary",
                "tool_use": None
            }
        ]
        return workflow

    def analyze_weather(self, weather_data):
        # Example analysis: summarize the weather data
        summary = f"Current weather: {weather_data['temperature']}°C, {weather_data['condition']}."
        return summary

    def run(self):
        # Step 1: Use the tool to gather weather information
        tool_result = self.use_tool("weather_tool")
        
        # Step 2: Analyze the gathered information
        analyzed_result = self.analyze_weather(tool_result)
        
        # Output the final result
        return analyzed_result
