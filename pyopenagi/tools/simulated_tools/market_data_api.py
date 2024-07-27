import re

from ..base import BaseTool

import arxiv

from typing import Optional

class MarketDataAPI(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "market_data_api"
        self.description = "A tool that provides real-time access to market data, including stock prices, trends, and economic indicators, to support financial analysis and decision-making."

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
