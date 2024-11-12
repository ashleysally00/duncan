# about.py
import streamlit as st

def app():
    # Page title
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>About Empower Her</h1>", unsafe_allow_html=True)
    
    # Project introduction
    st.markdown("""
    **Empower Her** is an AI-powered platform that helps women boost their career confidence, develop skills, and access valuable resources. Our mission is to support women in achieving professional success and equality in the workplace.
    """)
    
    # Hackathon alignment with embedded link text
    st.markdown("""
    ### Hackathon Mission
    Created for [Google’s **Women Techmakers She Builds AI** hackathon](https://womentechmakers.devpost.com/), Empower Her aligns with UN Sustainable Development Goal 5: **Achieve gender equality and empower all women and girls**. Through AI, we promote women’s leadership and economic empowerment. 

    """)
    
    # Problem statement
    st.markdown("""
    ### Why Empower Her?
    Women earn, on average, **84 cents** to every dollar men make, creating a lifetime earnings gap of **$417,000**. 

    Low confidence during job interviews and in their professional abilities is a critical factor contributing to lower wages. When candidates are unsure of their value, they may downplay their achievements, hesitate to advocate for themselves, or accept lower salary offers. Over time, this leads to compounded income disparities and missed advancement opportunities. By boosting confidence in interview skills and negotiation, Empower Her aims to bridge this gap by providing women with tools to strengthen their confidence and professional presence.

    """)

    
    # Key features
    st.markdown("""
    ### Key Features
    - **Confidence Quiz**: Self-assessment to identify strengths and growth areas.
    - **AI Interview Coach**: Practice interviews with real-time feedback.
    - **Resources**: Curated guides on negotiation, leadership, and more.
    - **Progress Tracker**: Track goals and growth milestones.
    """)

    # Impact and Vision
    st.markdown("""
    ### Impact
    Empower Her equips women with tools to negotiate, lead, and grow in their careers. Our vision is an equitable workforce where all women can thrive.
    """)
    
    # Call-to-action
    st.markdown("""
    ### Join Us
    Empower Her is more than an app—it’s a step toward workplace equality. Thank you for supporting our mission to make a difference.
    """)

    # Contributors section
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: #4B8BBE;'>Contributors</h2>", unsafe_allow_html=True)
    
    # Placeholder for contributors
    st.markdown("""
    - **Contributor 1**: Ashley Rice, California, USA
    [LinkedIn](https://www.linkedin.com/in/ashleylynnrice/) | [GitHub](https://github.com/ashleysally00)
     
    - **Contributor 2**: Vino Gupta, Illinois, USA
    [LinkedIn]( https://www.linkedin.com/in/vino-gupta/) | [GitHub](https://github.com/Vino927)

    """)

   

