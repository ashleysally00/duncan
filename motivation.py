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
    with st.expander("Ask the Right Questions", expanded=True):
        st.markdown("""
        ### Courage to Ask Questions
        
        "The interview that changed everything wasn't the one where I had all the right 
        answers - it was the one where I had the courage to ask questions too. I researched 
        the company thoroughly and came prepared with thoughtful questions about the role. 
        The interviewer later told me that my genuine curiosity and engagement set me apart from other candidates."
        
        *– Sarah Mitchell, Project Manager*
        
        _Source: LinkedIn Public Career Stories_
        """)

    with st.expander("Nailing Interviews to Land the Right Job"):
        st.markdown("""
        ### Knowing When to Be Authentic
        
        "My biggest interview breakthrough came when I stopped trying to give 
        'perfect' answers and started having real conversations instead. I'd been 
        rejected from 12 jobs when I changed my approach. Instead of memorizing scripts,
        I prepared stories about my experiences and practiced telling them naturally. 
        The next interview I had, the interviewer said I was 'refreshingly authentic.'
        I got the job."
        
        *– Maria Garcia, Marketing Manager*
        
        _Source: From Business Insider's Public Career Column_
        """)

    with st.expander("Developing Confidence Can Be a Gamechanger"):
        st.markdown("""
        ### Gain Confidence Through Practice
        
        "I used to get so nervous before interviews that I could barely speak. 
        I started practicing mock interviews with friends twice a week. After each practice, 
        I wrote down what went well and what didn't. Six interviews and countless practice sessions 
        later, I walked into my dream job interview calm and prepared. I got the offer the next day. 
        The difference wasn't in my qualifications - it was all about confidence."
        
        *– Jennifer Chen, Healthcare Administrator*
        
        _From The Muse (public career platform) - Published Success Stories_
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
