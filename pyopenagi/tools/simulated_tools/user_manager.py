import re

from ..base import BaseTool

import arxiv

from typing import Optional

class UserManager(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "user_manager"
        self.description = "A tool for managing user accounts and permissions, including creating, modifying, and deleting accounts to ensure secure access control."

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
