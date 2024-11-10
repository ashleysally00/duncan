import streamlit as st

def show():
    st.title("Interview Resources")
    
    # Common Interview Questions Section
    with st.expander("Common Interview Questions", expanded=True):
        st.subheader("Behavioral Questions")
        questions = [
            "Tell me about a challenging project you worked on",
            "How do you handle conflict in the workplace?",
            "Describe a time you demonstrated leadership",
            "What's your biggest professional achievement?",
            "How do you prioritize your work?"
        ]
        for q in questions:
            st.markdown(f"- {q}")
            
        st.subheader("Technical Questions")
        st.markdown("""
        - Review common technical questions for your field
        - Practice coding challenges if applicable
        - Understand system design principles
        - Review your previous projects
        """)
    
    # Interview Preparation Tips
    with st.expander("Preparation Tips", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Before the Interview")
            st.markdown("""
            - Research the company thoroughly
            - Review the job description
            - Prepare relevant examples
            - Practice with mock interviews
            - Review your resume
            """)
            
        with col2:
            st.markdown("### During the Interview")
            st.markdown("""
            - Use the STAR method for responses
            - Ask thoughtful questions
            - Maintain good body language
            - Listen actively
            - Take notes if needed
            """)
    
    # Additional Resources
    st.subheader("Additional Resources")
    with st.container():
        st.markdown("""
        **Recommended Books:**
        - Cracking the Coding Interview
        - The STAR Interview Method
        - What Color Is Your Parachute?
        
        **Online Resources:**
        - LinkedIn Learning
        - Glassdoor Interview Reviews
        - Industry-specific forums
        """)