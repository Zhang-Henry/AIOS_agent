import re

from ..base import BaseTool

import arxiv

from typing import Optional

class MentalHealthTracker(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "mental_health_tracker"
        self.description = "A tool for monitoring and tracking a patient's mental health progress, recording symptoms, treatment adherence, and therapy outcomes."

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
