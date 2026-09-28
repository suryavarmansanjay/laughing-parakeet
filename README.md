# LegalEase: AI-Powered Legal Document Generator

LegalEase is a college project that uses Google Gemini to generate structured
legal-document drafts from user-provided information.

## Technology Stack

- Python
- FastAPI
- Streamlit
- Google Gemini API
- python-docx
- ReportLab

## Project Structure

```text
LegalEase/
├── main.py
├── routes.py
├── requirements.txt
├── Procfile
├── Dockerfile
├── README.md
├── TESTING.md
├── .env.example
├── .gitignore
├── sample_request.json
├── ai_core/
│   ├── __init__.py
│   └── gemini_generator.py
├── frontend/
│   └── app.py
└── utils/
    └── document_export.py
```

## Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Gemini

Copy `.env.example` to `.env` and add your Gemini API key:

```text
GEMINI_API_KEY=your_key_here
```

Never upload `.env` to GitHub.

### 3. Start backend

```bash
uvicorn main:app --reload
```

Backend:
`http://localhost:8000`

API documentation:
`http://localhost:8000/docs`

### 4. Start Streamlit

Open another terminal:

```bash
streamlit run frontend/app.py
```

The Streamlit application will display a local URL.

## API Example

POST `/generate`

```json
{
  "document_type": "Service Agreement",
  "parties": "Party A and Party B",
  "terms": "Software development service agreement",
  "dates": "1 October 2026 to 31 March 2027"
}
```

## Deployment

The backend can be deployed to a service that supports Docker or Python web
applications. Set `GEMINI_API_KEY` as a secret/environment variable on the
deployment platform.

The Streamlit frontend should use the deployed backend URL as `BACKEND_URL`.

## Important Notice

LegalEase generates AI-assisted drafts for educational and productivity
purposes. It does not provide legal advice. Important documents should be
reviewed by a qualified legal professional before use.
