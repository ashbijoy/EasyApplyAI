import streamlit as st
import openai
openai.apikey = "your_key_here"

st.set_page_config(page_title="EasyApplyAi", layout="centered")

st.title("EasyApplyAi")
st.subheader("Tailor Your Resume and Cover Letter to Any Job — Instantly!")

resume_input = st.text_area (
    "Paste your Resume here",
   placeholder="Paste your resume here...",
    height=250
)

job_input = st.text_area (
    "Paste your Job Description here",
    placeholder="Paste your JD here...",
    height=250    
)

generate_button = st.button ("Generate Custom Resume & Cover Letter")