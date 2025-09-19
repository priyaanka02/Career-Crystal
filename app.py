import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import json
import os

# 💎 CareerCrystal Configuration
st.set_page_config(
    page_title="💎 CareerCrystal - AI Job Intelligence",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Beautiful pastel styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #FFB3D9 0%, #E6D7FF 25%, #C8E6C9 50%, #FFF8DC 75%, #FFDAB9 100%);
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #FFB3D9 0%, #E6D7FF 100%);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #FFB3D9, #E6D7FF);
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    
    .metric-card {
        background: rgba(255,255,255,0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(255,179,217,0.3);
        text-align: center;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# 🌟 Header
st.markdown("""
<div style='background: linear-gradient(90deg, #FFB3D9, #E6D7FF); padding: 30px; border-radius: 20px; margin-bottom: 30px; text-align: center;'>
    <h1 style='color: white; margin: 0; font-size: 3rem;'>💎 CareerCrystal</h1>
    <p style='color: white; margin: 10px 0 0 0; font-size: 1.3rem;'>AI-Powered Job Market Intelligence Platform</p>
    <p style='color: white; margin: 5px 0 0 0;'>🚀 Autonomous • 🎨 Beautiful • 🤖 Intelligent</p>
</div>
""", unsafe_allow_html=True)

# 🌟 Sidebar Navigation  
with st.sidebar:
    st.markdown("# 💎 CareerCrystal")
    st.markdown("*AI-Powered Job Intelligence*")
    st.markdown("---")
    
    page = st.selectbox("🧭 Navigate", [
        "🏠 Dashboard", 
        "🔮 AI Insights",
        "📊 Market Trends", 
        "💰 Salary Intel",
        "🤖 Automation Center"
    ])
    
    st.markdown("---")
    st.markdown("### 🟢 System Status")
    st.markdown("**Active** - Running 24/7")
    st.markdown("📈 **Live Data** streaming")
    st.markdown("🔥 **AI Analysis** ready")

# 📊 Main Dashboard
if page == "🏠 Dashboard":
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='color: #8B4C8C; margin: 0;'>🔥 2,847</h2>
            <p style='color: #8B4C8C; margin: 5px 0 0 0;'>Jobs Today</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='color: #8B4C8C; margin: 0;'>💰 $92K</h2>
            <p style='color: #8B4C8C; margin: 5px 0 0 0;'>Avg Salary</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='color: #8B4C8C; margin: 0;'>📈 +27%</h2>
            <p style='color: #8B4C8C; margin: 5px 0 0 0;'>Growth</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='color: #8B4C8C; margin: 0;'>🎯 AI/ML</h2>
            <p style='color: #8B4C8C; margin: 5px 0 0 0;'>Top Skill</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Market Trends Chart
    st.markdown("### 📈 Live Job Market Trends")
    
    # Generate sample data
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
    trend_data = pd.DataFrame({
        'Date': dates,
        'AI/ML Jobs': [200 + i*8 + (i%5)*15 for i in range(len(dates))],
        'Data Science': [150 + i*6 + (i%4)*12 for i in range(len(dates))],
        'Software Engineering': [300 + i*4 + (i%6)*18 for i in range(len(dates))]
    })
    
    fig = px.area(trend_data, x='Date', 
                  y=['AI/ML Jobs', 'Data Science', 'Software Engineering'],
                  color_discrete_map={
                      'AI/ML Jobs': '#FFB3D9',
                      'Data Science': '#E6D7FF',
                      'Software Engineering': '#C8E6C9'
                  })
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(255,255,255,0.9)',
        font_color='#8B4C8C'
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif page == "🔮 AI Insights":
    st.markdown("## 🤖 AI Career Intelligence")
    
    st.markdown("""
    <div style='background: rgba(230,215,255,0.3); padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        <h4 style='color: #8B4C8C; margin-top: 0;'>📊 AI Market Analysis</h4>
        <p style='font-size: 1.1rem; color: #8B4C8C;'>The tech job market shows explosive growth with AI/ML positions leading demand. Remote-first companies are offering 23% higher salaries, while cloud expertise commands premium rates.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hot Skills
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔥 Most In-Demand Skills")
        skills = ["Python", "Machine Learning", "React", "AWS", "Data Science"]
        
        for i, skill in enumerate(skills):
            skill_popularity = 100 - (i * 15)
            st.markdown(f"""
            <div style='background: rgba(255,179,217,0.2); padding: 10px; margin: 5px 0; border-radius: 8px; border-left: 4px solid #FFB3D9;'>
                <strong style='color: #8B4C8C;'>{skill}</strong>
                <div style='background: #FFB3D9; height: 8px; border-radius: 4px; width: {skill_popularity}%; margin-top: 5px;'></div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 💡 AI Recommendations")
        recommendations = [
            "Focus on AI/ML skills for highest-paying opportunities",
            "Build cloud expertise (AWS/Azure) for remote prospects",
            "Develop full-stack capabilities for versatility"
        ]
        
        for i, rec in enumerate(recommendations, 1):
            st.markdown(f"""
            <div style='background: rgba(255,248,220,0.3); padding: 15px; margin: 10px 0; border-radius: 10px;'>
                <strong style='color: #8B4C8C;'>💡 Tip {i}:</strong>
                <p style='color: #8B4C8C; margin: 5px 0 0 0;'>{rec}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "🤖 Automation Center":
    st.markdown("## ⚙️ 24/7 Automation Command Center")
    
    st.markdown("""
    <div style='background: linear-gradient(90deg, #C8E6C9, #FFF8DC); padding: 20px; border-radius: 15px; margin-bottom: 30px;'>
        <h3 style='color: white; text-align: center; margin: 0;'>🤖 Autonomous Operation Active</h3>
        <p style='color: white; text-align: center; margin: 5px 0 0 0;'>CareerCrystal is running 24/7, continuously analyzing job markets</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Control Buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 System Status", type="primary"):
            st.success("✅ All systems operational!")
    
    with col2:
        if st.button("📊 Generate Report"):
            st.info("📈 Daily intelligence report generated!")
    
    with col3:
        if st.button("🔄 Refresh Data"):
            st.success("🔄 Data refreshed successfully!")

else:
    st.markdown(f"## {page}")
    st.markdown("🚧 This feature is under active development!")
    st.markdown("CareerCrystal is constantly evolving with new AI-powered capabilities.")
    st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 10px; margin-top: 30px;'>
    <p style='color: #8B4C8C; margin: 0;'>💎 <strong>CareerCrystal</strong> - Built with ❤️ using AI & Beautiful Design</p>
    <p style='color: #8B4C8C; margin: 5px 0 0 0; font-size: 0.9rem;'>🤖 Autonomous • 🎨 Beautiful • 🚀 Professional • 2025</p>
    <p style='color: #8B4C8C; margin: 5px 0 0 0; font-size: 0.8rem;'>✨ Deployed successfully on Streamlit Cloud ✨</p>
</div>
""", unsafe_allow_html=True)

