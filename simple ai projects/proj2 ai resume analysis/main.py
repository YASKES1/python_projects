import io

import streamlit as st
import os
from dotenv import load_dotenv
import PyPDF2
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF OR TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job you are targetting (optional")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text =""
    for page in pdf_reader.pages:
        text += page.extractText() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content")
            st.stop()

        prompt = f"""Please analyze this resume and provide feedback.
        focus on the following aspects:
        1. content clarity and impact
        2. skills representation
        3. experience descriptions
        4. specific improvements for {job_role if job_role else 'general job applications'}
        
        Resume content:
        {file_content}
        
        please provide tour analysis in a clear, structured fotmat with specific recommendations"""

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer with years of expirience in Hr"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        st.markdown("### Analysis Results")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occured: {str(e)}")


