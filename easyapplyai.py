import streamlit as st
import openai
import fitz 
from dotenv import load_dotenv
import os

load_dotenv()  # Looks for .env by default
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="EasyApplyAi", layout="centered")

st.title("EasyApplyAi")
st.subheader("Tailor Your Resume and Cover Letter to Any Job — Instantly!")

resume_file = st.file_uploader("upload your resume (pdf only)", type=["pdf"])

job_input = st.text_area (
    "Paste your Job Description Here",
    placeholder="Paste your Job Description Here...",
    height=250
)

generate_button = st.button ("Generate Custom Resume & Cover Letter")
 
if resume_file is not None:
    pdf_doc = fitz.open(stream=resume_file.read(), filetype="pdf")
    resume_text = ""
    for page in pdf_doc:
        resume_text += page.get_text()
else:
    resume_text = None

if generate_button:
    if resume_text and job_input:
        with st.spinner("Crafting your personalized documents..."):

            highlights_prompt = f"""
You are a professional resume editor.

Here is the resume:
{resume_text}

Here is the job description:
{job_input}

Extract and list only the most relevant skills and achievements from the resume that match the job description.
Format them as short bullet points.
"""
            highlights_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": highlights_prompt}],
                temperature=0.6
            )
            resume_highlights = highlights_response['choices'][0]['message']['content'].strip()

            cover_prompt = f"""
You are a professional cover letter writer.

Here is the resume:
{resume_text}

Here is the job description:
{job_input}

Write a tailored cover letter in 250–300 words using a confident, professional tone.
"""
            cover_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": cover_prompt}],
                temperature=0.7
            )
            cover_letter = cover_response['choices'][0]['message']['content'].strip()

            st.subheader("Tailored Resume Highlights")
            st.markdown(resume_highlights)

            st.subheader("Custom Cover Letter")
            st.markdown(cover_letter)
    else:
        st.warning("Please upload your resume and paste the job description.")
