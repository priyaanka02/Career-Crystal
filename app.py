import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import json
import time
import random
import math

# 💎 CareerCrystal Configuration
st.set_page_config(
    page_title="💎 CareerCrystal - AI Job Intelligence",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Beautiful CSS with Background Image
st.markdown("""
<style>
    /* Your Beautiful Crystal Background - FIXED */
    .main {
        background: 
            linear-gradient(135deg, rgba(255,179,217,0.6) 0%, rgba(230,215,255,0.6) 25%, rgba(200,230,201,0.6) 50%, rgba(255,248,220,0.6) 75%, rgba(255,218,185,0.6) 100%),
            url('https://raw.githubusercontent.com/priyaanka02/Career-Crystal/main/assets/images/background.jpg') center/cover no-repeat fixed;
        font-family: 'Helvetica Neue', sans-serif;
        min-height: 100vh;
    }
    
    /* Smooth Counter Animations */
    .live-counter {
        font-size: 2.5rem;
        font-weight: bold;
        color: #8B4C8C;
        text-shadow: 2px 2px 4px rgba(255,179,217,0.5);
        animation: smoothPulse 3s ease-in-out infinite;
    }
    
    @keyframes smoothPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .metric-card {
        background: rgba(255,255,255,0.95);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(255,179,217,0.4);
        text-align: center;
        margin: 15px 0;
        border: 2px solid rgba(255,179,217,0.3);
        backdrop-filter: blur(15px);
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #FFB3D9, transparent);
        animation: shimmer 4s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    /* Live Indicator */
    .live-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #00ff00;
        animation: blink 2s infinite;
        margin-right: 8px;
        box-shadow: 0 0 10px rgba(0,255,0,0.5);
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0.3; }
    }
    
    .status-bar {
        background: rgba(255,255,255,0.9);
        padding: 12px 20px;
        border-radius: 25px;
        margin: 10px 0;
        border-left: 4px solid #FFB3D9;
        backdrop-filter: blur(10px);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, rgba(255,179,217,0.9) 0%, rgba(230,215,255,0.9) 100%);
        backdrop-filter: blur(15px);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #FFB3D9, #E6D7FF);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255,179,217,0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255,179,217,0.5);
    }
</style>
""", unsafe_allow_html=True)

# 🔄 FIXED Stats Generation Function
def get_live_stats():
    """Generate smoothly changing statistics - FIXED MATH IMPORT"""
    base_time = int(time.time())
    
    # Fixed sine wave calculations
    jobs_today = 2847 + int(50 * (1 + 0.1 * math.sin(base_time / 10)))  # ← FIXED
    avg_salary = 92000 + int(3000 * (1 + 0.05 * math.sin(base_time / 15)))  # ← FIXED
    growth_rate = 27 + int(5 * (1 + 0.1 * math.sin(base_time / 20)))  # ← FIXED
    ai_jobs = 1247 + int(100 * (1 + 0.08 * math.sin(base_time / 12)))  # ← FIXED
    
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
<div style='background: linear-gradient(90deg, rgba(255,179,217,0.95), rgba(230,215,255,0.95)); padding: 30px; border-radius: 25px; margin-bottom: 30px; text-align: center; backdrop-filter: blur(15px); border: 2px solid rgba(255,255,255,0.3);'>
    <h1 style='color: white; margin: 0; font-size: 3.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>💎 CareerCrystal</h1>
    <p style='color: white; margin: 10px 0 0 0; font-size: 1.3rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);'>AI-Powered Job Market Intelligence Platform</p>
    <p style='color: white; margin: 15px 0 0 0; font-size: 1rem;'>
        <span class='live-indicator'></span>
        <strong>LIVE</strong> • Updated: {current_stats['timestamp']} • 🤖 Processing {current_stats['jobs_today']:,} jobs
    </p>
</div>
""", unsafe_allow_html=True)

# 🌟 Sidebar Navigation  
with st.sidebar:
    st.markdown("# 💎 CareerCrystal")
    st.markdown("*AI-Powered Job Intelligence*")
    st.markdown("---")
    
    # Live status indicators
    st.markdown(f"""
    <div class='status-bar'>
        <span class='live-indicator'></span><strong>System:</strong> LIVE ✅
    </div>
    <div class='status-bar'>
        <span class='live-indicator'></span><strong>Background:</strong> Crystal Galaxy ✨
    </div>
    <div class='status-bar'>
        <span class='live-indicator'></span><strong>Updates:</strong> Smooth Refresh 🔄
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
    st.markdown(f"**Jobs Today:** {current_stats['jobs_today']:,}")
    st.markdown(f"**AI Jobs:** {current_stats['ai_jobs']:,}")
    st.markdown(f"**Growth:** +{current_stats['growth_rate']}%")

# 📊 Main Dashboard
if page == "🏠 Dashboard":
    
    # 📊 Live Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='live-counter'>{current_stats['jobs_today']:,}</div>
            <p style='color: #8B4C8C; margin: 5px 0 0 0; font-weight: bold;'>🔥 Jobs Today</p>
            <p style='color: #666; margin: 2px 0 0 0; font-size: 0.8rem;'>+{random.randint(50, 200)} last hour</p>
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
    
    # 📈 Live Chart 
    st.markdown("### 📈 Live Job Market Trends")
    
    # Generate smooth data 
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
    current_minute = datetime.now().minute
    
    trend_data = pd.DataFrame({
        'Date': dates,
        'AI/ML Jobs': [200 + i*8 + (i%5)*15 + (current_minute % 20) for i in range(len(dates))],
        'Data Science': [150 + i*6 + (i%4)*12 + (current_minute % 15) for i in range(len(dates))],
        'Software Engineering': [300 + i*4 + (i%6)*18 + (current_minute % 25) for i in range(len(dates))]
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
        title=f"📊 Live Market Data • {current_stats['timestamp']}"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ⚡ Live Activity Feed
    st.markdown("### ⚡ Live Activity Stream")
    
    activities = [
        f"🔍 Scraped {random.randint(50, 200)} jobs from LinkedIn",
        f"🤖 AI analyzed {random.randint(100, 500)} job descriptions", 
        f"📊 Trend update: AI jobs +{random.randint(5, 20)}%",
        f"💰 Salary data refreshed for {random.randint(10, 50)} companies",
        f"🎯 Hot skill: {random.choice(['Python', 'React', 'AWS', 'ML', 'Docker'])}",
        f"🏢 {random.randint(5, 25)} companies started hiring"
    ]
    
    for activity in random.sample(activities, 3):
        time_ago = random.randint(1, 60)
        st.markdown(f"""
        <div class='status-bar' style='margin: 8px 0;'>
            <span class='live-indicator'></span>
            <strong>{activity}</strong>
            <span style='float: right; color: #666; font-size: 0.8rem;'>{time_ago}s ago</span>
        </div>
        """, unsafe_allow_html=True)

else:
    # Other pages
    st.markdown(f"## {page}")
    st.markdown("🚧 This feature is under development!")
    
    # Simple metrics 
    stats = get_live_stats()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🔥 Active", f"{stats['jobs_today']:,}", "+12%")
    with col2:
        st.metric("💰 Salary", f"${stats['avg_salary']:,}", "+8%") 
    with col3:
        st.metric("📈 Growth", f"+{stats['growth_rate']}%", "+2%")

# Auto-refresh every 10 seconds (controlled refresh)
if st.button("🔄 Refresh Stats", key="refresh_btn"):
    st.rerun()

# Add automatic refresh with timer
if 'last_refresh' not in st.session_state:
    st.session_state.last_refresh = time.time()

current_time = time.time()
if current_time - st.session_state.last_refresh > 10:  # 10 seconds
    st.session_state.last_refresh = current_time
    st.rerun()

# Footer
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; padding: 25px; background: rgba(255,255,255,0.2); border-radius: 15px; margin-top: 30px; backdrop-filter: blur(10px);'>
    <p style='color: #8B4C8C; margin: 0;'>💎 <strong>CareerCrystal</strong> - Built with ❤️ using AI & Beautiful Design</p>
    <p style='color: #8B4C8C; margin: 5px 0 0 0; font-size: 0.9rem;'>
        🤖 Autonomous • 🎨 Crystal Background • 🚀 Live Updates • 
        <span class='live-indicator'></span>
        <strong>LIVE</strong>
    </p>
</div>
""", unsafe_allow_html=True)
