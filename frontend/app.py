
import streamlit as st
import requests

BACKEND_URL = "https://laughing-parakeet.onrender.com"

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.info(
    "Generate a structured legal document draft using Google Gemini. "
    "The generated document should be reviewed by a qualified legal professional."
)

document_type = st.selectbox(
    "Document Type",
    [
        "Service Agreement",
        "Rental Agreement",
        "Employment Agreement",
        "Non-Disclosure Agreement",
        "Partnership Agreement",
        "Other"
    ]
)

if document_type == "Other":
    document_type = st.text_input("Enter document type")

parties = st.text_area(
    "Parties",
    placeholder="Example: Party A: ABC Technologies Pvt. Ltd.; Party B: Example Client"
)

terms = st.text_area(
    "Terms and Conditions",
    placeholder="Enter the main terms, responsibilities, payment details, termination conditions, etc."
)

dates = st.text_area(
    "Relevant Dates",
    placeholder="Example: Agreement starts on 1 October 2026 and continues for 6 months."
)

if st.button("Generate Legal Document", type="primary"):

    if not document_type or not parties or not terms or not dates:
        st.warning("Please fill in all fields.")
    else:
        payload = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates
        }

        try:
            with st.spinner("Generating your document..."):
                response = requests.post(
                    f"{BACKEND_URL}/generate",
                    json=payload,
                    timeout=120
                )

            if response.status_code == 200:
                result = response.json()
                document = result.get("document", "")

                st.success("Document generated successfully!")

                edited_document = st.text_area(
                    "Generated Document",
                    value=document,
                    height=500
                )

                st.download_button(
                    "Download TXT",
                    data=edited_document,
                    file_name="legal_document.txt",
                    mime="text/plain"
                )

            else:
                st.error(
                    f"Backend error: {response.status_code}\n\n"
                    f"{response.text}"
                )

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to the backend: {e}")
