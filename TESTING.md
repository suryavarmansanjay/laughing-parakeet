# LegalEase Testing Guide

## Backend Health Check

Start the backend:

```bash
uvicorn main:app --reload
```

Open:

```text
http://localhost:8000/
```

Expected response:

```json
{
  "message": "LegalEase API is running",
  "docs": "/docs"
}
```

## Swagger API Test

Open:

```text
http://localhost:8000/docs
```

Select `POST /generate`, click "Try it out", and use:

```json
{
  "document_type": "Non-Disclosure Agreement",
  "parties": "Company A and Person B",
  "terms": "Confidential business information must not be disclosed.",
  "dates": "1 October 2026"
}
```

Click "Execute".

## Frontend Test

Start:

```bash
streamlit run frontend/app.py
```

Enter the document details and click "Generate Document".

Verify:

- Generated text appears.
- Text can be edited.
- TXT download works.
- DOCX download works.
- PDF download works.

## Security Test

- `.env` must not be committed.
- API keys must be stored as environment variables.
- Do not place a real API key in source code.
