import re

from ..base import BaseTool

import arxiv

from typing import Optional

class ResearchDatabase(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "research_database"
        self.description = "A tool for accessing a wide range of academic literature, including journal articles, conference papers, and theses, to support research activities."

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
