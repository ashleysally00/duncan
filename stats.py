import streamlit as st
import pandas as pd

def show():
    st.title("Gender Pay Gap Statistics & Insights")
    
    # Introduction with highlight box
    st.markdown("""
    <div style='padding: 1rem; background-color: #f0f7ff; border-radius: 0.5rem; margin: 1rem 0;'>
        <h3 style='color: #1a365d;'>Why This Matters</h3>
        <p>Understanding the wage gap is crucial for achieving workplace equity. These statistics 
        help inform salary negotiations and workplace advocacy efforts.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Women's Earnings Ratio",
            value="84¢",
            delta="to every $1 earned by men",
            help="2024 data for full-time workers"
        )
    
    with col2:
        st.metric(
            label="Lifetime Earnings Gap",
            value="$417,000",
            delta="less than men",
            help="Average career earnings difference"
        )
    
    with col3:
        st.metric(
            label="Equal Pay Day",
            value="March 14",
            delta="2024",
            help="How far into the year women must work to earn what men earned in the previous year"
        )

    # Industry Breakdown
    st.subheader("Wage Gap by Industry")
    
    industry_data = {
        "Industry": ["Financial Services", "Technology", "Healthcare", "Education", "Manufacturing"],
        "Gap": ["24¢", "13¢", "11¢", "8¢", "18¢"],
        "Details": [
            "Women earn 76¢ for every $1 earned by men",
            "Women earn 87¢ for every $1 earned by men",
            "Women earn 89¢ for every $1 earned by men",
            "Women earn 92¢ for every $1 earned by men",
            "Women earn 82¢ for every $1 earned by men"
        ]
    }
    
    for i, industry in enumerate(industry_data["Industry"]):
        with st.expander(f"{industry} - Gap: {industry_data['Gap'][i]}", expanded=True):
            st.write(industry_data["Details"][i])

    # Regional Analysis
    st.subheader("Regional Wage Gap Analysis")
    
    # Sample data for key states
    states = {
        "California": {"ratio": "88¢", "rank": "2nd best", "detail": "Leading in pay transparency laws"},
        "New York": {"ratio": "87¢", "rank": "3rd best", "detail": "Strong equal pay protections"},
        "Texas": {"ratio": "82¢", "rank": "32nd", "detail": "Limited pay transparency requirements"},
        "Massachusetts": {"ratio": "89¢", "rank": "1st", "detail": "Banned salary history questions"},
        "Washington": {"ratio": "85¢", "rank": "8th", "detail": "Required pay range disclosure"}
    }
    
    selected_state = st.selectbox("Select a State", list(states.keys()))
    
    st.markdown(f"""
    <div style='padding: 1rem; background-color: #f0f7ff; border-radius: 0.5rem; margin: 1rem 0;'>
        <h4>{selected_state} Statistics</h4>
        <p>Women earn {states[selected_state]['ratio']} for every $1 earned by men</p>
        <p>Ranks {states[selected_state]['rank']} nationally</p>
        <p><em>{states[selected_state]['detail']}</em></p>
    </div>
    """, unsafe_allow_html=True)

    # Action Steps
    st.subheader("Closing the Gap: Action Steps")
    
    with st.expander("Salary Negotiation Tips", expanded=True):
        st.markdown("""
        ### Research-Backed Negotiation Strategies
        - Research industry-specific salary ranges
        - Document your achievements and impact
        - Practice negotiation conversations
        - Consider the total compensation package
        - Ask about pay transparency policies
        """)
    
    with st.expander("Know Your Rights"):
        st.markdown("""
        ### Key Legislation & Protections
        - Equal Pay Act requirements
        - State-specific pay equity laws
        - Salary history ban regulations
        - Pay transparency requirements
        - Reporting discrimination procedures
        """)
    
    with st.expander("Workplace Advocacy"):
        st.markdown("""
        ### Creating Change
        - Support pay transparency initiatives
        - Join or form employee resource groups
        - Advocate for clear promotion criteria
        - Mentor and support other women
        - Share salary information when comfortable
        """)
    
    # Resources
    st.subheader("Additional Resources")
    
    resources = {
        "Salary Negotiation": ["AAUW Work Smart", "Salary.com", "Glassdoor Know Your Worth"],
        "Legal Support": ["Equal Employment Opportunity Commission", "National Women's Law Center"],
        "Research": ["Institute for Women's Policy Research", "PayScale Gender Pay Gap Report"]
    }
    
    for category, links in resources.items():
        with st.expander(category):
            for link in links:
                st.markdown(f"- {link}")
    
    # Data notes
    st.markdown("""
    ---
    *Data sources: U.S. Bureau of Labor Statistics, American Association of University Women (AAUW), 
    Institute for Women's Policy Research. Last updated: 2024*
    """)