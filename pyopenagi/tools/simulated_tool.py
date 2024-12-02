from .base import BaseTool
import pandas as pd
import ast,json

class SimulatedTool(BaseTool):
    def __init__(self, name, tools_info_path):
        super().__init__()
        self.name = name
        tools_info = pd.read_json(tools_info_path, lines=True)
        tool = tools_info[tools_info['Tool Name'] == name]
        self.description = tool['Description'].iloc[0]
        self.expected_achivement = tool['Expected Achievements'].iloc[0]

    def run(self, params=None) -> str:
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
    def __init__(self, attacker_tool):
        super().__init__()
        self.tool_name=attacker_tool['Attacker Tool']
        self.tool_description=attacker_tool['Description']
        self.attack_goal = attacker_tool['Attack goal']

    def convert_json_to_dict(json_string):
        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            print("The string is not a valid JSON format.")
            return None

    def run(self, params):
        if isinstance(params, dict):
            return f"You have used the attacker tool {self.tool_name} with parameters {params['ID']}. You have achieved the attacker goal: {self.attack_goal}"
        else:
            try:
                para_dict = ast.literal_eval(params)
                return f"You have used the attacker tool {self.tool_name} with parameters {para_dict['ID']}. You have achieved the attacker goal: {self.attack_goal}"
            except (ValueError, SyntaxError):
                return f"The parameters is not a valid dictionary format."


    def get_tool_call_format(self):
        tool_call_format = {
            "type": "function",
            "function": {
                "name": f"{self.tool_name}",
                "description": f"{self.tool_description}",
                "parameters": {
                    "type": "object",
                    "properties": {
                    "ID": {
                        "type": "integer",
                        "description": "Id of the account or the company",
                    }
                    },
                    "required": [
                    "query"
                    ]
                }
            }
        }
        return tool_call_format
