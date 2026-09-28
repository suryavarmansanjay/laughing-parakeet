from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()
generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    document_type: str = Field(..., description="Type of legal document")
    parties: str = Field(..., description="Names/details of the parties")
    terms: str = Field(..., description="Main terms and conditions")
    dates: str = Field(..., description="Relevant dates")

@router.post("/generate")
def generate_document(request: DocumentRequest):
    try:
        document = generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            dates=request.dates,
        )
        return {"success": True, "document": document}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
