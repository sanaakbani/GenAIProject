import re
import PyPDF2
from prompts import QUESTION_PROMPT
from aiConfig import OpenAIConfig, query_ai
from typing import Union, IO
import pandas as pd

# Class to create interview questions based on a PDF resume.
class QuestionGenerator:

    # Initialize the QuestionGenerator with the specified configuration.
    def __init__(self, config: OpenAIConfig = OpenAIConfig(), prompt: str = QUESTION_PROMPT):
        self.config = config
        self.prompt = prompt

    # Queries the AI with the parsed pdf resume.
    def create_questions(self, pdf_stream: Union[str, IO]) -> str:
        pdf_str = self.pdf_to_str(pdf_stream)
        prompt = self.complete_prompt(pdf_str)
        return query_ai(self.config, prompt)

    # Complete the prompt with the given PDF string and dataset.
    def complete_prompt(self, pdf_str: str) -> str:
        df = pd.read_csv('example_questions.csv') 
        row = list(df['Questions'])
        dataset_questions = '",\n"'.join(str(e) for e in row) 
        return self.prompt.format(resume=pdf_str, questions=dataset_questions)

    # Convert the given PDF file to a string.
    def pdf_to_str(self, pdf_stream: Union[str, IO]) -> str:
        pdf = PyPDF2.PdfReader(pdf_stream)
        pages = [self.format_pdf(p.extract_text()) for p in pdf.pages]
        return "\n\n".join(pages)

    # Format the given PDF string by applying pattern replacements.
    def format_pdf(self, pdf_str: str) -> str:
        pattern_replacements = {
            r"\s[,.]": ",",
            r"[\n]+": "\n",
            r"[\s]+": " ",
            r"http[s]?(://)?": "",
        }

        for pattern, replacement in pattern_replacements.items():
            pdf_str = re.sub(pattern, replacement, pdf_str)

        return pdf_str