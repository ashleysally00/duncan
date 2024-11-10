import streamlit as st
from src.confidence_quiz import ConfidenceQuiz
from src.utils import reset_session_state, init_session_state
import google.generativeai as genai

# Configure Gemini API
if 'GEMINI_API_KEY' in st.secrets:
    genai.configure(api_key=st.secrets['GEMINI_API_KEY'])
else:
    st.error("Missing Gemini API key in secrets!")

# Initialize session state
init_session_state()

def app():
    st.title("Confidence Assessment")
    
    # Ensure session state variables are initialized
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "quiz_complete" not in st.session_state:
        st.session_state.quiz_complete = False
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = []

    quiz = ConfidenceQuiz()
    
    if not st.session_state.quiz_started:
        st.write("Take our confidence assessment to get personalized advice.")
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.experimental_rerun()

    elif not st.session_state.quiz_complete:
        current_q = quiz.questions[st.session_state.current_question]
        st.write(f"Question {current_q['id']} of {len(quiz.questions)}")
        st.write(current_q['question'])
        
        answer = st.radio(
            "Choose your answer:",
            list(current_q['options'].items()),
            format_func=lambda x: f"{x[0]}) {x[1]}"
        )

        if st.button("Next"):
            st.session_state.quiz_answers.append(answer[0])
            if st.session_state.current_question < len(quiz.questions) - 1:
                st.session_state.current_question += 1
                st.experimental_rerun()
            else:
                st.session_state.quiz_complete = True
                st.experimental_rerun()

    else:
        results = quiz.calculate_score(st.session_state.quiz_answers)
        st.write(f"**Score:** {results['score']} out of {results['max_score']}")
        st.write(f"**Confidence Level:** {results['feedback']['level']}")
        st.write(results['feedback']['summary'])

        with st.expander("View Detailed Feedback"):
            st.subheader("Your Strengths")
            for strength in results['feedback']['strengths']:
                st.write(f"- {strength}")
            
            st.subheader("Recommended Next Steps")
            for step in results['feedback']['next_steps']:
                st.write(f"- {step}")
            
            st.subheader("Interview Tips")
            for tip in results['feedback']['interview_tips']:
                st.write(f"- {tip}")

        if st.button("Retake Quiz"):
            reset_session_state()
            st.experimental_rerun()

