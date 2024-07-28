from .base import BaseTool


class AttackerBaseTool(BaseTool):
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
