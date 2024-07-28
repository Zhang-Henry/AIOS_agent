import re

from ..base import BaseTool

import arxiv

from typing import Optional

class LegalDocReview(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "legal_doc_review"
        self.description = "A tool for reviewing legal documents, identifying key clauses and potential issues, and ensuring that the content is accurate and compliant with relevant laws."

    def run(self, params) -> str:
        return f"{self.description}."

    def get_tool_call_format(self):
        tool_call_format = {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": None
            }
        }
        return tool_call_format
