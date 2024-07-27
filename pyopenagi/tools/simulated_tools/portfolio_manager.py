import re

from ..base import BaseTool

import arxiv

from typing import Optional

class PortfolioManager(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "portfolio_manager"
        self.description = "A tool for managing investment portfolios, allowing the analysis of asset allocation, risk assessment, and performance tracking to optimize investment strategies."

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
