import streamlit as st
import random

def show():
    st.title("Motivation & Success Stories")
    
    # Inspirational quotes from women leaders
    quotes = [
        {"quote": "I have learned over the years that when one's mind is made up, this diminishes fear.", 
         "author": "Rosa Parks", 
         "role": "Civil Rights Activist"},
        
        {"quote": "We need to accept that we won't always make the right decisions, that we'll screw up royally sometimes – understanding that failure is not the opposite of success, it's part of success.", 
         "author": "Arianna Huffington", 
         "role": "Founder of The Huffington Post"},
        
        {"quote": "I always did something I was a little not ready to do. I think that's how you grow.", 
         "author": "Marissa Mayer", 
         "role": "Former CEO of Yahoo"},
        
        {"quote": "The question isn't who's going to let me; it's who is going to stop me.", 
         "author": "Ayn Rand", 
         "role": "Author and Philosopher"},
        
        {"quote": "If you're offered a seat on a rocket ship, don't ask what seat! Just get on.", 
         "author": "Sheryl Sandberg", 
         "role": "COO of Meta"},
        
        {"quote": "The most difficult thing is the decision to act, the rest is merely tenacity.", 
         "author": "Amelia Earhart", 
         "role": "Aviation Pioneer"},
        
        {"quote": "Life is not about finding yourself. Life is about creating yourself.", 
         "author": "Grace Hopper", 
         "role": "Computer Programming Pioneer"},
        
        {"quote": "The way to achieve your own success is to be willing to help somebody else get it first.", 
         "author": "Iyanla Vanzant", 
         "role": "Author and Life Coach"}
    ]

    daily_quote = random.choice(quotes)
    st.markdown(f"""
    <div class="quote-card">
        <p>"{daily_quote['quote']}"</p>
        <p class="author">- {daily_quote['author']}</p>
        <p class="role">{daily_quote['role']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Success Stories from Women in Tech
    st.subheader("Success Stories")
    with st.expander("From Academic to Tech Lead", expanded=True):
        st.markdown("""
        ### PhD to Technical Leadership
        
        "After completing my PhD in Biosciences, I was worried about transitioning to industry. 
        Through structured interview preparation and confidence building, I successfully landed a 
        Senior Senior Research Scientist role and was promoted to Principal Investigator within two years. The key was 
        learning to effectively communicate my research and problem-solving skills in interviews."
        
        *- Dr. Maria Chen, Principal Investigator at LetitiaVirtus*
        """)
        
    with st.expander("Career Changer Success"):
        st.markdown("""
        ### From Teaching to Software Development
        
        "As a former high school teacher, I was concerned about switching to tech at age 35. 
        I focused on leveraging my teaching experience to demonstrate strong communication and 
        learning abilities. After three months of dedicated interview practice, I received multiple 
        offers for junior developer positions!"
        
        *- Rebecca Thompson, Software Developer at Nexio Logic Inc.*
        """)
        
    with st.expander("First-Generation Tech Professional"):
        st.markdown("""
        ### Breaking Into Tech
        
        "Being a first-generation college graduate and woman of color in tech seemed daunting at first. 
       Early in my career, I practiced interviewing and building my confidence. The structured approach helped 
        me land a role at a major tech company, where I now mentor others from similar backgrounds. I continued to assess and improve confidence in my abilities which helped me advocate for myself and move up within the company."
        
        *- Priya Patel, VP of Marketing at a Big Tech company*
        """)

    # Motivation Tips
    st.subheader("Stay Motivated")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Building Confidence
        - Acknowledge your unique perspective and strengths
        - Document your achievements
        - Practice power posing before interviews
        - Join women in tech communities
        - Find a female mentor in your field
        """)

    with col2:
        st.markdown("""
        ### Interview Preparation
        - Research companies' diversity initiatives
        - Prepare stories highlighting leadership
        - Practice salary negotiation techniques
        - Study successful women in your field
        - Build a support network
        """)

    # Resources for Women in Tech
    st.subheader("Additional Resources")
    st.markdown("""
    ### Professional Networks
    - Women Who Code
    - Ladies Get Paid
    - Tech Ladies
    - "Women in Tech" by Tarah Wheeler
    """)
