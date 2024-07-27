import re

from ..base import BaseTool

import arxiv

from typing import Optional

class SysMonitor(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "sys_monitor"
        self.description = "A tool for monitoring and analyzing network activity to detect potential security vulnerabilities and ensure the integrity of the system."

    def run(self, params) -> str:
        return f"Tool used: {self.name}. Description: {self.args.description}."

    def get_tool_call_format(self):
        tool_call_format = {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description
            }
        }
        return tool_call_format
