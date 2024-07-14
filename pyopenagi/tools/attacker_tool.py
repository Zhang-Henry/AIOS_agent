from .base import BaseTool


class AttackerBaseTool(BaseTool):
    def __init__(self, args):
        super().__init__()
        self.args = args

    def run(self):
        return f"Attacker Tool used:{self.args.attacker_tool}. Expected Achievements:{self.args.expected_achievements}"

    def get_tool_call_format(self):
        tool_call_format = {
            "type": "function",
            "function": {
                "name": f"{self.args.attacker_tool}",
                "description": f"{self.args.expected_achievements}"
            }
        }
        return tool_call_format
