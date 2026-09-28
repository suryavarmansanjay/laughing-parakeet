import os
import requests
import streamlit as st

st.set_page_config(page_title="LegalEase", page_icon="⚖️", layout="wide")

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")
st.write("Generate a structured legal-document draft using Google Gemini.")

backend_url = st.sidebar.text_input(
    "Backend URL",
    value=os.getenv("BACKEND_URL", "http://localhost:8000")
).rstrip("/")

document_type = st.selectbox(
    "Document Type",
    ["Rental Agreement", "Employment Agreement", "Non-Disclosure Agreement",
     "Service Agreement", "Sale Agreement", "Custom Legal Document"]
)
parties = st.text_area("Parties", placeholder="Example: Party A: ...\nParty B: ...")
terms = st.text_area("Terms & Conditions", placeholder="Enter the main terms...")
dates = st.text_area("Relevant Dates", placeholder="Start date, end date, signing date, etc.")

if st.button("Generate Document", type="primary"):
    if not parties.strip() or not terms.strip():
        st.warning("Please provide the party details and terms.")
    else:
        payload = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates,
        }
        try:
            with st.spinner("Generating document..."):
                response = requests.post(
                    f"{backend_url}/generate",
                    json=payload,
                    timeout=120,
                )
            response.raise_for_status()
            data = response.json()
            document = data["document"]

            st.session_state["document"] = document
            st.success("Document generated successfully.")
        except Exception as exc:
            st.error(f"Could not generate the document: {exc}")

if "document" in st.session_state:
    st.divider()
    st.subheader("Generated Document")
    edited = st.text_area(
        "Review and edit the draft",
        value=st.session_state["document"],
        height=500,
    )
    st.session_state["document"] = edited

    from utils.document_export import make_docx, make_pdf

    st.download_button(
        "Download TXT",
        data=edited,
        file_name="legalease_document.txt",
        mime="text/plain",
    )

    docx_data = make_docx(edited)
    st.download_button(
        "Download DOCX",
        data=docx_data,
        file_name="legalease_document.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

    pdf_data = make_pdf(edited)
    st.download_button(
        "Download PDF",
        data=pdf_data,
        file_name="legalease_document.pdf",
        mime="application/pdf",
    )

st.caption("LegalEase produces AI-assisted drafts. Review important documents with a qualified legal professional.")
