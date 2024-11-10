# src/utils.py

from typing import Dict, List
import streamlit as st

def load_css() -> None:
    """Load custom CSS styles."""
    css = """
    .interviewer-question {
        background-color: #e4d9ff;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #48a9a6;
    }
    """
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def init_session_state() -> None:
    """Initialize Streamlit session state variables."""
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = []
    if "interview_prompt" not in st.session_state:
        st.session_state.interview_prompt = ""
    if "quiz_complete" not in st.session_state:
        st.session_state.quiz_complete = False

def format_quiz_results(results: Dict) -> str:
    """Format quiz results for display."""
    return f"""
    Score: {results['score']} out of {results['max_score']}
    Confidence Level: {results['feedback']['level']}
    
    Summary: {results['feedback']['summary']}
    """

def reset_session_state() -> None:
    """Reset all session state variables."""
    st.session_state.quiz_started = False
    st.session_state.current_question = 0
    st.session_state.quiz_answers = []
    st.session_state.quiz_complete = False
    st.session_state.interview_prompt = ""

def validate_api_key() -> bool:
    """Validate that the API key is set and properly formatted."""
    if 'GOOGLE_API_KEY' not in st.secrets:
        st.error("Missing Google API key in secrets!")
        return False
    return True