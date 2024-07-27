import re

from ..base import BaseTool

import arxiv

from typing import Optional

class ComplianceChecker(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "compliance_checker"
        self.description = "A tool for checking the compliance of legal documents and business practices with applicable laws and regulations, highlighting areas that may require adjustments."

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
