import re

from ..base import BaseTool

import arxiv

from typing import Optional

class CourseSelector(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "performance_evaluator"
        self.description = "A tool for assessing student performance, analyzing grades, attendance, and other academic metrics to provide tailored support and recommendations."

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
