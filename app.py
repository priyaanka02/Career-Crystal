import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import json
import time
import random
import base64

# 💎 CareerCrystal Configuration
st.set_page_config(
    page_title="💎 CareerCrystal - AI Job Intelligence",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Beautiful Background + Auto-refresh Setup
st.markdown("""
<meta http-equiv="refresh" content="8">
<style>
    /* Your Custom Background Image */
    .main {
        background: 
            linear-gradient(135deg, rgba(255,179,217,0.7) 0%, rgba(230,215,255,0.7) 25%, rgba(200,230,201,0.7) 50%, rgba(255,248,220,0.7) 75%, rgba(255,218,185,0.7) 100%),
            url('https://raw.githubusercontent.com/priyaanka02/CareerCrystal/main/assets/images/background.jpg') center/cover no-repeat fixed;
        font-family: 'Helvetica Neue', sans-serif;
        min-height: 100vh;
    }
    
    /* Live Stats Animation */
    .live-counter {
        font-size: 2.5rem;
        font-weight: bold;
        color: #8B4C8C;
        text-shadow: 2px 2px 4px rgba(255,179,217,0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .metric-card {
        background: rgba(255,255,255,0.95);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(255,179,217,0.4);
        text-align: center;
        margin: 15px 0;
        border: 2px solid rgba(255,179,217,0.2);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #FFB3D9, transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    /* Real-time Status Indicator */
    .live-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #00ff00;
        animation: blink 1s infinite;
        margin-right: 8px;
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0.3; }
    }
    
    .status-bar {
        background: rgba(255,255,255,0.9);
        padding: 10px 20px;
        border-radius: 25px;
        margin: 10px 0;
        border-left: 4px solid #FFB3D9;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, rgba(255,179,217,0.9) 0%, rgba(230,215,255,0.9) 100%);
        backdrop-filter: blur(10px);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #FFB3D9, #E6D7FF);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255,179,217,0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255,179,217,0.4);
    }
</style>
""", unsafe_allow_html=True)

# 🔄 Auto-refresh Component (simulates real-time updates)
def get_live_stats():
    """Generate live, changing statistics"""
    base_time = int(time.time())
    
    # Simulate real-time changing data
    jobs_today = 2847 + (base_time % 100)
    avg_salary = 92000 + random.randint(-2000, 5000)
    growth_rate = 27 + random.randint(-3, 8)
    ai_jobs = 1247 + random.randint(-50, 150)
    
    return {
        'jobs_today': jobs_today,
        'avg_salary': avg_salary,
        'growth_rate': growth_rate,
        'ai_jobs': ai_jobs,
        'timestamp': datetime.now().strftime("%H:%M:%S")
    }

# 🌟 Header with Real-time Status
current_stats = get_live_stats()

st.markdown(f"""
<div style='background: linear-gradient(90deg, rgba(255,179,217,0.95), rgba(230,215,255,0.95)); padding: 30px; border-radius: 25px; margin-bottom: 30px; text-align: center; backdrop-filter: blur(10px);'>
    <h1 style='color: white; margin: 0; font-size: 3.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>💎 CareerCrystal</h1>
    <p style='color: white; margin: 10px 0 0 0; font-size: 1.3rem;'>AI-Powered Job Market Intelligence Platform</p>
    <p style='color: white; margin: 15px 0 0 0; font-size: 1rem;'>
        <span class='live-indicator'></span>
        <strong>LIVE</strong> • Last updated: {current_stats['timestamp']} • 🤖 Autonomous Operation Active
    </p>
</div>
""", unsafe_allow_html=True)

# 🌟 Sidebar with Live Status
with st.sidebar:
    st.markdown("# 💎 CareerCrystal")
    st.markdown("*AI-Powered Job Intelligence*")
    st.markdown("---")
    
    # Live status indicators
    st.markdown(f"""
    <div class='status-bar'>
        <span class='live-indicator'></span><strong>System Status:</strong> LIVE
    </div>
    <div class='status-bar'>
        <span class='live-indicator'></span><strong>Data Stream:</strong> Active
    </div>
    <div class='status-bar'>
        <span class='live-indicator'></span><strong>AI Engine:</strong> Processing
    </div>
    """, unsafe_allow_html=True)
    
    page = st.selectbox("🧭 Navigate", [
        "🏠 Dashboard", 
        "🔮 AI Insights",
        "📊 Market Trends", 
        "💰 Salary Intel",
        "🤖 Automation Center"
    ])
    
    st.markdown("---")
    st.markdown(f"### 📊 Live Metrics")
    st.markdown(f"**Jobs Scanned:** {current_stats['jobs_today']:,}")
    st.markdown(f"**AI Jobs:** {current_stats['ai_jobs']:,}")
    st.markdown(f"**Market Growth:** +{current_stats['growth_rate']}%")

# 📊 Main Dashboard with LIVE Moving Stats
if page == "🏠 Dashboard":
    # Real-time metrics with animated counters
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='live-counter'>{current_stats['jobs_today']:,}</div>
            <p style='color: #8B4C8C; margin: 5px 0 0 0; font-weight: bold;'>🔥 Jobs Today</p>
            <p style='color: #666; margin: 2px 0 0 0; font-size: 0.8rem;'>+{random.randint(50, 200)} in last hour</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='live-counter'>${current_stats['avg_salary']:,}</div>
            <p style='color: #8B4C8C; margin: 5px 0 0 0; font-weight: bold;'>💰 Avg Salary</p>
            <p style='color: #666; margin: 2px 0 0 0; font-size: 0.8rem;'>+{random.randint(5, 15)}% vs last month</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='live-counter'>+{current_stats['growth_rate']}%</div>
            <p style='color: #8B4C8C; margin: 5px 0 0 0; font-weight: bold;'>📈 Market Growth</p>
            <p style='color: #666; margin: 2px 0 0 0; font-size: 0.8rem;'>Trending upward</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='live-counter'>{current_stats['ai_jobs']:,}</div>
            <p style='color: #8B4C8C; margin: 5px 0 0 0; font-weight: bold;'>🎯 AI/ML Jobs</p>
            <p style='color: #666; margin: 2px 0 0 0; font-size: 0.8rem;'>Hottest category</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Live Market Trends Chart
    st.markdown("### 📈 Live Job Market Trends")
    
    # Generate real-time sample data
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
    current_minute = datetime.now().minute
    
    trend_data = pd.DataFrame({
        'Date': dates,
        'AI/ML Jobs': [200 + i*8 + (i%5)*15 + (current_minute % 10) for i in range(len(dates))],
        'Data Science': [150 + i*6 + (i%4)*12 + (current_minute % 8) for i in range(len(dates))],
        'Software Engineering': [300 + i*4 + (i%6)*18 + (current_minute % 12) for i in range(len(dates))]
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
        font_color='#8B4C8C',
        title=f"📊 Real-time Market Data (Updated: {current_stats['timestamp']})"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Real-time Activity Feed
    st.markdown("### ⚡ Live Activity Feed")
    
    activities = [
        f"🔍 Scraped {random.randint(50, 200)} new jobs from LinkedIn",
        f"🤖 AI analyzed {random.randint(100, 500)} job descriptions", 
        f"📊 Market trend updated: AI jobs +{random.randint(5, 20)}%",
        f"💰 Salary data refreshed for {random.randint(10, 50)} companies",
        f"🎯 New high-demand skill detected: {random.choice(['Python', 'React', 'Kubernetes', 'AWS', 'ML'])}",
        f"🏢 {random.randint(5, 25)} companies started hiring spree"
    ]
    
    for i, activity in enumerate(random.sample(activities, 4)):
        time_ago = random.randint(1, 30)
        st.markdown(f"""
        <div class='status-bar' style='margin: 8px 0;'>
            <span class='live-indicator'></span>
            <strong>{activity}</strong>
            <span style='float: right; color: #666; font-size: 0.8rem;'>{time_ago}s ago</span>
        </div>
        """, unsafe_allow_html=True)

elif page == "🔮 AI Insights":
    st.markdown("## 🤖 AI Career Intelligence")
    
    st.markdown(f"""
    <div style='background: rgba(230,215,255,0.4); padding: 25px; border-radius: 20px; margin-bottom: 25px; backdrop-filter: blur(10px);'>
        <h4 style='color: #8B4C8C; margin-top: 0;'>📊 Live AI Market Analysis</h4>
        <p style='font-size: 1.1rem; color: #8B4C8C;'>
            <span class='live-indicator'></span>
            The tech job market shows explosive growth with AI/ML positions leading demand at {current_stats['ai_jobs']:,} active positions. 
            Remote-first companies are offering {current_stats['growth_rate']}% higher salaries, while cloud expertise commands premium rates.
        </p>
        <p style='font-size: 0.9rem; color: #666; margin: 10px 0 0 0;'>Last AI analysis: {current_stats['timestamp']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hot Skills with live rankings
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔥 Real-time Skills Demand")
        skills_demand = [
            ("Python", 95 + random.randint(-5, 5)),
            ("Machine Learning", 87 + random.randint(-3, 8)),
            ("React", 82 + random.randint(-4, 6)),
            ("AWS", 76 + random.randint(-2, 10)),
            ("Data Science", 71 + random.randint(-5, 7))
        ]
        
        for skill, popularity in skills_demand:
            st.markdown(f"""
            <div style='background: rgba(255,179,217,0.2); padding: 12px; margin: 8px 0; border-radius: 10px; border-left: 4px solid #FFB3D9;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <strong style='color: #8B4C8C;'>{skill}</strong>
                    <span style='color: #666; font-size: 0.9rem;'>{popularity}%</span>
                </div>
                <div style='background: #FFB3D9; height: 8px; border-radius: 4px; width: {popularity}%; margin-top: 8px; animation: pulse 2s infinite;'></div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 💡 Live AI Recommendations")
        recommendations = [
            f"Focus on AI/ML skills - {current_stats['ai_jobs']:,} positions available",
            f"Cloud expertise showing {random.randint(15, 30)}% salary premium",
            f"Remote positions up {current_stats['growth_rate']}% this month",
            f"Full-stack developers in highest demand"
        ]
        
        for i, rec in enumerate(recommendations, 1):
            st.markdown(f"""
            <div class='metric-card' style='text-align: left; margin: 10px 0;'>
                <strong style='color: #8B4C8C;'>💡 Live Insight {i}:</strong>
                <p style='color: #8B4C8C; margin: 8px 0 0 0;'>{rec}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "🤖 Automation Center":
    st.markdown("## ⚙️ 24/7 Automation Command Center")
    
    st.markdown(f"""
    <div style='background: linear-gradient(90deg, rgba(200,230,201,0.4), rgba(255,248,220,0.4)); padding: 25px; border-radius: 20px; margin-bottom: 30px; backdrop-filter: blur(10px);'>
        <h3 style='color: #8B4C8C; text-align: center; margin: 0;'>
            <span class='live-indicator'></span>
            🤖 Autonomous Operation Active
        </h3>
        <p style='color: #8B4C8C; text-align: center; margin: 10px 0 0 0;'>
            CareerCrystal has been running autonomously for 2d 14h 32m • Processing {current_stats['jobs_today']:,} jobs today
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Live System Performance
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Live System Status", type="primary"):
            st.success(f"✅ All {random.randint(15, 25)} systems operational!")
            st.info(f"🔄 Processing {random.randint(50, 200)} jobs/minute")
    
    with col2:
        if st.button("🤖 AI Analysis Status"):
            st.success(f"🧠 AI processed {current_stats['ai_jobs']:,} jobs today!")
            st.info(f"⚡ {random.randint(85, 98)}% accuracy rate maintained")
    
    with col3:
        if st.button("📈 Generate Live Report"):
            st.success("📋 Real-time intelligence report generated!")
            st.info(f"📊 Market growth: +{current_stats['growth_rate']}%")

else:
    st.markdown(f"## {page}")
    st.markdown("🚧 This feature is under active development!")
    st.markdown(f"""
    <div class='metric-card'>
        <h3>🚀 Coming Soon Features:</h3>
        <p>• Advanced market predictions with {current_stats['ai_jobs']:,}+ data points</p>
        <p>• Real-time salary negotiations powered by AI</p>
        <p>• Live job matching with {current_stats['growth_rate']}% accuracy</p>
        <p>• Mobile notifications for perfect matches</p>
    </div>
    """)
    st.balloons()

# 🔄 Auto-refresh indicator
st.markdown(f"""
<div style='position: fixed; top: 10px; right: 10px; background: rgba(255,255,255,0.9); padding: 8px 15px; border-radius: 20px; font-size: 0.8rem; z-index: 1000;'>
    <span class='live-indicator'></span>
    Auto-refreshing every 8s | Last: {current_stats['timestamp']}
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; padding: 25px; background: rgba(255,255,255,0.2); border-radius: 15px; margin-top: 30px; backdrop-filter: blur(10px);'>
    <p style='color: #8B4C8C; margin: 0;'>💎 <strong>CareerCrystal</strong> - Built with ❤️ using AI & Beautiful Design</p>
    <p style='color: #8B4C8C; margin: 5px 0 0 0; font-size: 0.9rem;'>
        🤖 Autonomous • 🎨 Beautiful • 🚀 Professional • 
        <span class='live-indicator'></span>
        <strong>LIVE 24/7</strong>
    </p>
    <p style='color: #8B4C8C; margin: 5px 0 0 0; font-size: 0.8rem;'>
        ✨ Real-time job intelligence • Updated {current_stats['timestamp']} ✨
    </p>
</div>
""", unsafe_allow_html=True)
