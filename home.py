# home.py
import streamlit as st

def app():
    # Page title with styling
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Empower Yourself and Elevate Your Career</h1>", unsafe_allow_html=True)
    
    # Add a descriptive subtitle with center alignment
    st.markdown("<h3 style='text-align: center; color: #4B8BBE;'>Use our AI Interview Coach, build your confidence, and reach new heights in your career.</h3>", unsafe_allow_html=True)
    
    # Divider for visual separation
    st.markdown("---")
    
    # Add sections with icons and engaging text
    st.markdown("""
        <div style="display: flex; justify-content: space-around; margin-top: 20px;">
            <div style="text-align: center;">
                <img src="https://img.icons8.com/ios-filled/50/4B8BBE/brain.png" width="50" height="50"/>
                <h4>AI Interview Coach</h4>
                <p style="color: #555555;">Practice interviewing with real-time feedback and ace your next interview.</p>
            </div>
            <div style="text-align: center;">
                <img src="https://img.icons8.com/ios-filled/50/4B8BBE/confetti.png" width="50" height="50"/>
                <h4>Confidence Quiz</h4>
                <p style="color: #555555;">Assess your confidence level and get tips to improve.</p>
            </div>
            <div style="text-align: center;">
                <img src="https://img.icons8.com/ios-filled/50/4B8BBE/book.png" width="50" height="50"/>
                <h4>Resources</h4>
                <p style="color: #555555;">Access a library of resources to support your career growth.</p>
            </div>
        </div>

        <div style="display: flex; justify-content: space-around; margin-top: 20px;">
            <div style="text-align: center;">
                <img src="https://img.icons8.com/ios-filled/50/4B8BBE/bar-chart.png" width="50" height="50"/>
                <h4>Statistics</h4>
                <p style="color: #555555;">Learn about the Gender Pay Gap Statistics & Insights based on your state.</p>
            </div>
            <div style="text-align: center;">
                <img src="https://img.icons8.com/ios-filled/50/4B8BBE/trophy.png" width="50" height="50"/>
                <h4>Motivation</h4>
                <p style="color: #555555;">Read inspirational succes stories and motivational tips to keep pushing forward.</p>
            </div>
            <div style="text-align: center;">
                <img src="https://img.icons8.com/ios-filled/50/4B8BBE/task-completed.png" width="50" height="50"/>
                <h4>Progress Tracker</h4>
                <p style="color: #555555;">Monitor your goals, milestones, and achievements as you grow.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

  # Informational message at the bottom instead of a button
    st.markdown("<div style='text-align: center; margin-top: 40px;'>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: #4B8BBE; font-size: 1.1em;'>Use the menu on the left to get started with Confidence Quiz, try the the Interview Coach, or explore other resources!</p>",
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Footer note or tagline
    st.markdown("<p style='text-align: center; color: #888888; font-size: 0.9em;'>EmpowerU - Your Partner in Professional Growth and Confidence Building</p>", unsafe_allow_html=True)
