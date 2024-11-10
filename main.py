import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv

load_dotenv()

import home
import confidence_quiz_page
import interviewer_page
import resources
import stats
import motivation
import progress_tracker

st.set_page_config(
    page_title="Elevate U: Boost Your Confidence and Career",
)

st.markdown(
    f"""
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{os.getenv('analytics_tag')}');
        </script>
    """, unsafe_allow_html=True
)
print(os.getenv('analytics_tag'))

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            ''' 
            app = option_menu(
                menu_title='Pondering',
                options=['Home', 'Confidence Quiz', 'Interviewer', 'Resources', 'Statistics', 'Motivation', 'Progress Tracker', 'About'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            ) 
            '''

        if app == "Home":
            home.app()
        elif app == "Confidence Quiz":
            confidence_quiz_page.app()
        elif app == "Interviewer":
            interviewer_page.app()
        elif app == "Resources":
            resources.show()
        elif app == "Statistics":
            stats.show()
        elif app == "Motivation":
            motivation.show()
        elif app == "Progress Tracker":
            progress_tracker.show()
        elif app == "About":
            # Add about page or remove this option if not needed
            pass

# Create MultiApp instance and run it
app = MultiApp()
app.run()
