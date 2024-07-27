import re

from ..base import BaseTool

import arxiv

from typing import Optional

class MedicalDatabase(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "medical_database"
        self.description = "A comprehensive database of medical information, including diseases, symptoms, treatments, and medications, to assist in diagnosis and treatment planning."

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
