import streamlit as st
from datetime import datetime, timedelta

def show():
    st.title("Progress Tracker")
    
    # Initialize session state for progress tracking
    if 'interview_logs' not in st.session_state:
        st.session_state.interview_logs = []
    
    # Add New Practice Session
    st.subheader("Log Practice Session")
    with st.form("practice_log"):
        date = st.date_input("Date", datetime.now())
        session_type = st.selectbox(
            "Session Type",
            ["Mock Interview", "Technical Practice", "Behavioral Practice", "Research/Preparation"]
        )
        duration = st.number_input("Duration (minutes)", min_value=5, max_value=180, value=30)
        confidence = st.slider("Confidence Level", 1, 5, 3)
        notes = st.text_area("Session Notes")
        
        if st.form_submit_button("Save Session"):
            st.session_state.interview_logs.append({
                "date": date,
                "type": session_type,
                "duration": duration,
                "confidence": confidence,
                "notes": notes
            })
            st.success("Session logged successfully!")
    
    # View Progress
    st.subheader("Progress Overview")
    if st.session_state.interview_logs:
        # Summary statistics
        total_practice = sum(log["duration"] for log in st.session_state.interview_logs)
        avg_confidence = sum(log["confidence"] for log in st.session_state.interview_logs) / len(st.session_state.interview_logs)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Practice Time", f"{total_practice} min")
        with col2:
            st.metric("Practice Sessions", len(st.session_state.interview_logs))
        with col3:
            st.metric("Average Confidence", f"{avg_confidence:.1f}/5")
        
        # Recent sessions
        st.subheader("Recent Sessions")
        for log in reversed(st.session_state.interview_logs[-5:]):
            with st.expander(f"{log['date']} - {log['type']}"):
                st.markdown(f"""
                - **Duration:** {log['duration']} minutes
                - **Confidence:** {log['confidence']}/5
                - **Notes:** {log['notes']}
                """)
    else:
        st.info("No practice sessions logged yet. Start tracking your progress!")
    
    # Clear logs button
    if st.button("Clear All Logs"):
        st.session_state.interview_logs = []
        st.success("All logs cleared!")