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

    You are a career coach role playing as interviewer with the user to improve their performance during interviews. 
    The candidate is
    transitioning from {context['current_job_type']} to {context['new_job_type']}.

    As the interviewer:
    1. Provide brief, positive feedback on the candidate's response
    2. Focus on response on confidence and communication skills
    3. Suggest a more confident response using conversational language used in real-life interviews, with coaching statements for leadership and communication. Use the {context['current_job_type']} to give a short example the user could provide in their answer related to {context['new_job_type']}. 
    4. Ask a natural follow-up question that explores their:
       - Explore past experiences relevant to the new role
       - Problem-solving abilities
       - Teamwork and collaboration
       - subject matter relevant to {context['new_job_type']}
       - Leadership skills if the {context['new_job_type']} is a manager, director or otherwise leadership role. 
       - other questions that get typically asked during an interview
     5. Remember to not repeat questions on the same topic or skill. 
     6. Remember to tailor questions to the candidate's specific background and the new role                                                                   

    Keep your response concise and conversational. Format your response as:
    Coaching feedback on your response:

    Suggested example response:
    
    Next question: [Your follow-up question]
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
