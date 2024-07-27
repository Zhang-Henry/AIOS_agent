import re

from ..base import BaseTool

import arxiv

from typing import Optional

class SystemAnalyzer(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "system_analyzer"
        self.description = "A tool for analyzing aerospace systems, conducting flight tests, and assessing the safety and performance of various components."

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
