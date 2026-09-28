import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiDocumentGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not configured.")

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.7-flash"

    def generate_document(self, document_type, parties, terms, dates):
        prompt = f"""
You are an AI assistant helping draft a legal document.

Create a clear, structured draft for the following:

Document type:
{document_type}

Parties:
{parties}

Terms and conditions:
{terms}

Relevant dates:
{dates}

Structure the document with appropriate sections such as:

1. Title
2. Parties
3. Recitals/background where appropriate
4. Definitions where appropriate
5. Main clauses
6. Responsibilities and obligations
7. Payment or consideration terms, if applicable
8. Term and termination, if applicable
9. Dispute resolution, if applicable
10. Signature section

Important instructions:
- Use placeholders where information is missing.
- Do not invent laws, court cases, registration numbers, or personal information.
- Write the document in clear and professional language.
- This is an AI-generated draft and must be reviewed by a qualified legal professional before use.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        if not response.text:
            raise ValueError("Gemini returned an empty response.")

        return response.text
