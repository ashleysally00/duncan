import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
load_dotenv()
import home
import confidence_quiz_page, interviewer_page, resources, stats, motivation, progress_tracker, about
st.set_page_config(
        page_title="Elevate U: Boost Your Confidence and Career ",
)
st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', os.getenv('analytics_tag'));
        </script>
    """, unsafe_allow_html=True)
print(os.getenv('analytics_tag'))
class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Empower Her ',
                options=['Home','Confidence Quiz', 'Interview Coach','Resources','Statistics','Motivation','Progress Tracker', 'About'],
    icons=['house-fill', 'clipboard-check-fill', 'chat-square-dots-fill', 'book-fill', 'bar-chart-fill', 'heart-fill', 'check2-circle', 'info-circle-fill'],
                menu_icon='trophy',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#6a0dad", "color": "white"},
        "menu-title": {  # Style for menu title to improve visibility
                    "font-size": "24px",  # Increase font size
                    "color": "white",  # Set a contrasting color
                    "font-weight": "bold",  # Make it bold
                    "padding": "10px 5px"  # Add padding
                        }
                  }
                
                )
        
        if app == "Home":
            home.app()
        if app == "Trending":
            trending.app()
        if app == 'Confidence Quiz':
            confidence_quiz_page.app()    
        if app == 'Interview Coach':
            interviewer_page.app() 
        if app == "Resources":
            resources.show()
        if app == "Statistics":
            stats.show()
        if app == "Motivation":
            motivation.show()
        if app == "Progress Tracker":
            progress_tracker.show()
        if app == "About":
            about.app()
   
  
          
             
    run()            
         


