# src/gemini_interviewer.py

import google.generativeai as genai
import streamlit as st

# Define the Gemini AI model
model = genai.GenerativeModel('gemini-pro')

# Candidate details
DEFAULT_CONTEXT = {
    "current_job_type": "graduate student",
    "new_job_type": "software engineer"
}

def start_interview():
    """Initialize the first question of the interview."""
    return "Tell me about yourself and why you are interested in this role."

def analyze_response_and_prompt_next_question(user_response, previous_prompt, context=DEFAULT_CONTEXT):
    """Analyze the user's response and generate the next question."""
    prompt = f"""
    **Interviewer:** {previous_prompt}

    **Candidate:** "{user_response}"

    **Your Role:**
    You are a seasoned career coach simulating an interview to help the candidate improve their performance. The candidate is transitioning from a {context['current_job_type']} role to a {context['new_job_type']} role.

    **Your Task:**
    1. **Provide Concise Feedback:** Offer brief, positive feedback on the candidate's response, focusing on confidence and communication skills.
    2. **Suggest a Confident Response:** Propose a more confident response using conversational language, similar to a real-world interview. Incorporate coaching statements to enhance leadership and communication skills. Use the {context['current_job_type']} role to provide a relevant example that the candidate could apply to the {context['new_job_type']} role.
    3. **Ask a Tailored Follow-up Question:** Pose a natural follow-up question that delves into one or more of the following areas:
       - **Professional Experience:** Explore past experiences relevant to the new role.
       - **Problem-Solving:** Assess the candidate's ability to tackle challenges.
       - **Teamwork and Collaboration:** Gauge their ability to work effectively with others.
       - **Subject Matter Expertise:** Test their knowledge and skills related to the new role.
       - **Leadership Skills:** If applicable, evaluate their leadership potential.
       - **General Interview Questions:** Incorporate common interview questions to broaden the scope.

    **Remember:**
    - **Avoid repetitive questions.**
    - **Tailor questions to the candidate's specific background and the new role.**
    - **Keep your responses concise and conversational.**

    **Format your response as follows:**

    **Coaching Feedback:**
    [Brief, positive feedback on the candidate's response]

    **Suggested Response:**
    [A more confident response with coaching tips]

    **Next Question:**
    [Your follow-up question]
    """
    try:
        # Generate response from Gemini
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "I apologize, but I encountered an error. Could you please rephrase your response?"

def update_interview_context(age=None, gender=None, location=None, 
                           current_job=None, desired_job=None):
    """Update the interview context with new candidate details."""
    context = DEFAULT_CONTEXT.copy()
    if current_job: context['current_job_type'] = current_job
    if desired_job: context['new_job_type'] = desired_job
    return context
