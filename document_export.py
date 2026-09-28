from io import BytesIO
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from xml.sax.saxutils import escape

def make_docx(text: str) -> bytes:
    document = Document()
    for line in text.splitlines():
        document.add_paragraph(line)
    output = BytesIO()
    document.save(output)
    return output.getvalue()

def make_pdf(text: str) -> bytes:
    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    for line in text.splitlines():
        if line.strip():
            story.append(Paragraph(escape(line), styles["BodyText"]))
            story.append(Spacer(1, 6))
    doc.build(story)
    return output.getvalue()
