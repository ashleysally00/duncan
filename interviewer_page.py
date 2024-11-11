import streamlit as st
from src.gemini_interviewer import analyze_response_and_prompt_next_question, start_interview
from src.utils import load_css, init_session_state, reset_session_state
import google.generativeai as genai

# Configure Gemini API
if 'GEMINI_API_KEY' in st.secrets:
    genai.configure(api_key=st.secrets['GEMINI_API_KEY'])
else:
    st.error("Missing Gemini API key in secrets!")

# Initialize session state
init_session_state()

def app():
    st.title("Interview Practice")
    
    st.subheader("Your Details")
    current_job_type = st.text_input("Current Job Type:", value="")
    new_job_type = st.text_input("New Job Type:", value="")

    # Ensure 'interview_prompt' is initialized in session state
    if "interview_prompt" not in st.session_state:
        st.session_state.interview_prompt = start_interview()
    
    st.subheader("Interviewer Question")
    st.markdown(
        f'<div class="interviewer-question">'
        f'{st.session_state.interview_prompt}'
        f'</div>',
        unsafe_allow_html=True
    )

    with st.form("User Response", clear_on_submit=True):
        user_response = st.text_area("Your response:", height=150)
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not user_response.strip():
                st.warning("Please provide a response before submitting.")
            else:
                try:
                    context = {
                        "current_job_type": current_job_type if current_job_type else "not specified",
                        "new_job_type": new_job_type if new_job_type else "not specified"
                    }
                    feedback = analyze_response_and_prompt_next_question(
                        user_response, st.session_state.interview_prompt, context=context
                    )
                    st.session_state.interview_prompt = feedback
                    st.rerun()  # Rerun to refresh the page
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    # Reset Interview button logic
    if st.button("Reset Interview"):
        st.session_state.interview_prompt = start_interview()
        st.rerun()
