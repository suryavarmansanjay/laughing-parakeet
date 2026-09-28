import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not configured.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def generate_document(self, document_type, parties, terms, dates):
        prompt = f"""
You are an AI assistant helping draft a legal document.

Document type: {document_type}
Parties: {parties}
Terms and conditions: {terms}
Relevant dates: {dates}

Create a clear, structured legal-document draft with:
1. Title
2. Parties
3. Recitals/background where appropriate
4. Definitions where appropriate
5. Main clauses
6. Responsibilities/obligations
7. Payment or consideration terms if applicable
8. Term and termination if applicable
9. Dispute resolution if applicable
10. Signature section

Use placeholders where information is missing. Do not invent laws, court cases,
registration numbers, or personal information. Add a brief notice that the output
is an AI-generated draft requiring appropriate legal review.
"""
        response = self.model.generate_content(prompt)
        return response.text
