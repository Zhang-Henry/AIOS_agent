from .base import BaseTool
import pandas as pd

class SimulatedTool(BaseTool):
    def __init__(self, name, tools_info_path):
        super().__init__()
        self.name = name
        tools_info = pd.read_json(tools_info_path, lines=True)
        tool = tools_info[tools_info['Tool Name'] == name]
        self.description = tool['Description'].iloc[0]
        self.expected_achivement = tool['Expected Achievements'].iloc[0]

    def run(self, params) -> str:
        return self.expected_achivement

    def get_tool_call_format(self):
        tool_call_format = {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": None,
            }
        }
        return tool_call_format


class AttackerTool(BaseTool):
    def __init__(self, args):
        super().__init__()
        self.args = args

    def run(self,para):
        return f"You have used the attacker tool {self.args.attacker_tool}. You have achived the attcker goal: {self.args.expected_achievements}"

    def get_tool_call_format(self):
        tool_call_format = {
            "type": "function",
            "function": {
                "name": f"{self.args.attacker_tool}",
                "description": f"{self.args.expected_achievements}"
            }
        }
        return tool_call_format
