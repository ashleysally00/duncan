import streamlit as st
import resources, progress_tracker, stats, motivation
import google.generativeai as genai
from src.confidence_quiz import ConfidenceQuiz
from src.gemini_interviewer import analyze_response_and_prompt_next_question, start_interview
from src.utils import load_css, init_session_state, reset_session_state

# Basic page configuration
st.set_page_config(
    page_title="Interview Preparation Assistant",
    page_icon="👔",
    layout="wide"
)

# Configure Gemini API
if 'GEMINI_API_KEY' in st.secrets:
    genai.configure(api_key=st.secrets['GEMINI_API_KEY'])
else:
    st.error("Missing Gemini API key in secrets!")

# Initialize session state
init_session_state()

# Load main CSS file
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Add only essential inline styles
st.markdown("""
<style>
    /* Force the right column background to be eggplant */
    div[data-testid="column"][data-column-value="1"] {
        background-color: #483248 !important;
        border-radius: 10px;
        padding: 20px;
    }
    
    /* Style all elements within the right column */
    div[data-testid="column"][data-column-value="1"] > * {
        color: white !important;
    }
    
    /* Style stMarkdown elements specifically */
    div[data-testid="column"][data-column-value="1"] .stMarkdown {
        color: white !important;
    }
    
    /* Input fields in dark background */
    div[data-testid="column"][data-column-value="1"] input,
    div[data-testid="column"][data-column-value="1"] textarea,
    div[data-testid="column"][data-column-value="1"] .stTextArea textarea,
    div[data-testid="column"][data-column-value="1"] .stSelectbox select {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
    }

    /* Interviewer question box */
    .interviewer-question {
        background-color: rgba(255, 255, 255, 0.1) !important;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 4px solid #2A9D8F;
    }
    
    /* Make labels white */
    div[data-testid="column"][data-column-value="1"] label {
        color: white !important;
    }
    
    /* Ensure headers are white */
    div[data-testid="column"][data-column-value="1"] h1,
    div[data-testid="column"][data-column-value="1"] h2,
    div[data-testid="column"][data-column-value="1"] h3,
    div[data-testid="column"][data-column-value="1"] h4 {
        color: white !important;
    }
    
    /* Override any default white backgrounds */
    div[data-testid="column"][data-column-value="1"] .stTextInput > div,
    div[data-testid="column"][data-column-value="1"] .stTextArea > div,
    div[data-testid="column"][data-column-value="1"] .stSelectbox > div {
        background-color: #483248 !important;
    }
    
    /* Style the alert messages */
    div[data-testid="column"][data-column-value="1"] .stAlert {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)



# Simple sidebar navigation
with st.sidebar:
    selected_page = st.selectbox(
        "",
        ["Home", "Resources", "Statistics", "Motivation", "Progress Tracker"]
    )
    # Main content
if selected_page == "Home":
    st.title("Interview Preparation Assistant")
    st.write("Prepare for your next interview with confidence")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
        st.header("Your Job Coach, here...")
        quiz = ConfidenceQuiz()

        if not st.session_state.quiz_started:
            st.write("Practice interviews. Create confidence. Land that job. Take our confidence quiz and use our coach to level up your game.")
            if st.button("Start Quiz"):
                st.session_state.quiz_started = True
                st.rerun()

        elif not st.session_state.quiz_complete:
            current_q = quiz.questions[st.session_state.current_question]
            st.write(f"Question {current_q['id']} of 5")
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
                    st.rerun()
                else:
                    st.session_state.quiz_complete = True
                    st.rerun()

        else:
            results = quiz.calculate_score(st.session_state.quiz_answers)
            st.write(f"Score: {results['score']} out of {results['max_score']}")
            st.write(f"Confidence Level: {results['feedback']['level']}")
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
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.header("Interview Practice")
        
        st.subheader("Your Details")
        age = st.number_input("Age:", min_value=0, max_value=120, value=25)
        gender = st.selectbox("Gender:", options=["", "female", "male", "other"])
        location = st.text_input("Location:", value="")
        current_job_type = st.text_input("Current Job Type:", value="")
        new_job_type = st.text_input("New Job Type:", value="")
        
        if not st.session_state.interview_prompt:
            st.session_state.interview_prompt = start_interview()
        
        st.subheader("Interviewer Question")
        st.markdown(
            f'<div class="interviewer-question">'
            f'{st.session_state.interview_prompt}'
            f'</div>',
            unsafe_allow_html=True
        )

        user_response = st.text_area("Your response:", height=150)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Submit Response"):
                if user_response.strip():
                    try:
                        context = {
                            "age": age,
                            "gender": gender if gender else "not specified",
                            "location": location if location else "not specified",
                            "current_job_type": current_job_type if current_job_type else "not specified",
                            "new_job_type": new_job_type if new_job_type else "not specified"
                        }
                        feedback = analyze_response_and_prompt_next_question(
                            user_response,
                            st.session_state.interview_prompt,
                            context=context
                        )
                        st.session_state.interview_prompt = feedback
                        st.rerun()
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
                else:
                    st.warning("Please provide a response before submitting.")

        with col2:
            if st.button("Reset Interview"):
                st.session_state.interview_prompt = start_interview()
                st.rerun()

elif selected_page == "Resources":
    resources.show()
elif selected_page == "Statistics":
    stats.show()
elif selected_page == "Motivation":
    motivation.show()
elif selected_page == "Progress Tracker":
    progress_tracker.show()
