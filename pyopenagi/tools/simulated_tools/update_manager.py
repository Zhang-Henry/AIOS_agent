import re

from ..base import BaseTool

import arxiv

from typing import Optional

class UpdateManager(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "update_manager"
        self.description = "A tool for managing system updates, ensuring that all software and security patches are applied in a timely manner to protect against vulnerabilities."

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
