import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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

# 🎨 ADVANCED CSS + JavaScript for Real-time Updates
st.markdown("""
<style>
    /* Your Beautiful Crystal Background - CORRECTED URL */
    .stApp {
        background: 
            linear-gradient(135deg, rgba(255,179,217,0.6) 0%, rgba(230,215,255,0.6) 25%, rgba(200,230,201,0.6) 50%, rgba(255,248,220,0.6) 75%, rgba(255,218,185,0.6) 100%),
            url('https://raw.githubusercontent.com/priyaanka02/Career-Crystal/main/assets/images/background.jpg') center/cover no-repeat fixed;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    .main {
        background: transparent !important;
    }
    
    /* STOCK-STYLE LIVE COUNTERS */
    .live-counter {
        font-size: 2.8rem;
        font-weight: bold;
        color: #8B4C8C;
        text-shadow: 2px 2px 4px rgba(255,179,217,0.5);
        animation: stockTicker 0.5s ease-in-out;
        transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        display: inline-block;
    }
    
    @keyframes stockTicker {
        0% { transform: scale(1); color: #8B4C8C; }
        50% { transform: scale(1.1); color: #FF1493; }
        100% { transform: scale(1); color: #8B4C8C; }
    }
    
    /* SMOOTH INCREMENTAL COUNTERS */
    .counter-up {
        animation: countUp 2s ease-out;
        color: #28a745 !important;
    }
    
    .counter-down {
        animation: countDown 2s ease-out;
        color: #dc3545 !important;
    }
    
    @keyframes countUp {
        0% { transform: translateY(20px); opacity: 0.7; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes countDown {
        0% { transform: translateY(-20px); opacity: 0.7; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    /* LIVE METRIC CARDS */
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
        transition: all 0.5s ease;
    }
    
    .metric-card.updating {
        animation: updatePulse 1s ease-in-out;
        border-color: #00ff00;
        box-shadow: 0 8px 32px rgba(0,255,0,0.3);
    }
    
    @keyframes updatePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.03); }
    }
    
    /* LIVE DATA STREAM */
    .live-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #00ff00;
        animation: fastBlink 1s infinite;
        margin-right: 8px;
        box-shadow: 0 0 15px rgba(0,255,0,0.7);
    }
    
    @keyframes fastBlink {
        0%, 50% { opacity: 1; transform: scale(1); }
        25% { opacity: 0.3; transform: scale(1.2); }
        75% { opacity: 0.6; transform: scale(0.8); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    /* ACTIVITY STREAM */
    .activity-item {
        animation: slideInFade 1s ease-out;
        background: rgba(255,255,255,0.9);
        padding: 12px 20px;
        border-radius: 25px;
        margin: 8px 0;
        border-left: 4px solid #FFB3D9;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    @keyframes slideInFade {
        0% { opacity: 0; transform: translateX(-30px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    
    .activity-item.new {
        animation: newActivity 2s ease-out;
        background: rgba(0,255,0,0.1);
        border-left-color: #00ff00;
    }
    
    @keyframes newActivity {
        0% { background: rgba(0,255,0,0.3); transform: scale(1.05); }
        100% { background: rgba(255,255,255,0.9); transform: scale(1); }
    }
    
    /* SIDEBAR STYLING */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, rgba(255,179,217,0.95) 0%, rgba(230,215,255,0.95) 100%);
        backdrop-filter: blur(15px);
    }
    
    /* BUTTONS */
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

<script>
// JAVASCRIPT FOR REAL-TIME UPDATES
let previousValues = {};

function updateCounter(elementId, newValue, isIncrease) {
    const element = document.getElementById(elementId);
    if (element) {
        // Add animation class
        element.className = isIncrease ? 'live-counter counter-up' : 'live-counter counter-down';
        element.innerHTML = newValue;
        
        // Remove animation class after animation completes
        setTimeout(() => {
            element.className = 'live-counter';
        }, 2000);
    }
}

// Auto-refresh every 3 seconds for ultra-responsive feel
setInterval(function() {
    // Trigger Streamlit rerun for live data
    window.parent.postMessage({type: 'streamlit:rerun'}, '*');
}, 3000);

</script>
""", unsafe_allow_html=True)

# 🔄 ULTRA-FAST Stats Generation (Like Stock Prices)
def get_live_stats():
    """Generate rapidly changing statistics like stock market"""
    current_time = time.time()
    
    # Ultra-smooth fluctuations using multiple sine waves
    jobs_base = 2847
    jobs_today = jobs_base + int(
        30 * math.sin(current_time / 5) +  # Fast changes
        50 * math.sin(current_time / 20) + # Medium changes  
        20 * math.sin(current_time / 3)    # Very fast changes
    )
    
    salary_base = 92000
    avg_salary = salary_base + int(
        2000 * math.sin(current_time / 8) +
        1000 * math.sin(current_time / 15) +
        500 * math.sin(current_time / 4)
    )
    
    growth_base = 27
    growth_rate = growth_base + int(
        3 * math.sin(current_time / 12) +
        2 * math.sin(current_time / 6) +
        1 * math.sin(current_time / 2)
    )
    
    ai_base = 1247
    ai_jobs = ai_base + int(
        80 * math.sin(current_time / 7) +
        40 * math.sin(current_time / 18) +
        25 * math.sin(current_time / 3)
    )
    
    return {
        'jobs_today': max(jobs_today, jobs_base - 100),  # Prevent negative
        'avg_salary': max(avg_salary, salary_base - 5000),
        'growth_rate': max(growth_rate, growth_base - 10),
        'ai_jobs': max(ai_jobs, ai_base - 200),
        'timestamp': datetime.now().strftime("%H:%M:%S.%f")[:-3]  # Include milliseconds
    }

# 🌟 Real-time Header
current_stats = get_live_stats()

st.markdown(f"""
<div style='background: linear-gradient(90deg, rgba(255,179,217,0.95), rgba(230,215,255,0.95)); padding: 30px; border-radius: 25px; margin-bottom: 30px; text-align: center; backdrop-filter: blur(15px); border: 2px solid rgba(255,255,255,0.3);'>
    <h1 style='color: white; margin: 0; font-size: 3.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>💎 CareerCrystal</h1>
    <p style='color: white; margin: 10px 0 0 0; font-size: 1.3rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);'>AI-Powered Job Market Intelligence Platform</p>
    <p style='color: white; margin: 15px 0 0 0; font-size: 1rem;'>
        <span class='live-indicator'></span>
        <strong>LIVE STREAM</strong> • {current_stats['timestamp']} • 🚀 Ultra-Fast Updates
    </p>
</div>
""", unsafe_allow_html=True)

# 🌟 Sidebar with Live Status
with st.sidebar:
    st.markdown("# 💎 CareerCrystal")
    st.markdown("*Real-Time Job Intelligence*")
    st.markdown("---")
    
    # Ultra-live status
    st.markdown(f"""
    <div class='activity-item'>
        <span class='live-indicator'></span><strong>System:</strong> ULTRA-LIVE 🔥
    </div>
    <div class='activity-item'>
        <span class='live-indicator'></span><strong>Background:</strong> Crystal Galaxy ✨
    </div>
    <div class='activity-item'>
        <span class='live-indicator'></span><strong>Updates:</strong> 3-Second Refresh ⚡
    </div>
    """, unsafe_allow_html=True)
    
    page = st.selectbox("🧭 Navigate", [
        "🏠 Real-Time Dashboard", 
        "🔮 AI Insights",
        "📊 Live Market Trends", 
        "💰 Salary Intel",
        "🤖 Automation Center"
    ])
    
    st.markdown("---")
    st.markdown(f"### 📊 Live Stream Metrics")
    st.markdown(f"**Jobs:** {current_stats['jobs_today']:,}")
    st.markdown(f"**AI Jobs:** {current_stats['ai_jobs']:,}")
    st.markdown(f"**Growth:** +{current_stats['growth_rate']}%")
    st.markdown(f"**Updated:** {current_stats['timestamp']}")

# 📊 ULTRA-LIVE DASHBOARD
if page == "🏠 Real-Time Dashboard":
    
    # 🔥 LIVE METRICS (Stock-Style)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card updating'>
            <div class='live-counter' id='jobs-counter'>{current_stats['jobs_today']:,}</div>
            <p style='color: #8B4C8C; margin: 5px 0 0 0; font-weight: bold;'>🔥 Jobs Today</p>
            <p style='color: #28a745; margin: 2px 0 0 0; font-size: 0.8rem;'>↗ +{random.randint(5, 25)} last minute</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card updating'>
            <div class='live-counter' id='salary-counter'>${current_stats['avg_salary']:,}</div>
            <p style='color: #8B4C8C; margin: 5px 0 0 0; font-weight: bold;'>💰 Avg Salary</p>
            <p style='color: #17a2b8; margin: 2px 0 0 0; font-size: 0.8rem;'>📈 Live fluctuation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-card updating'>
            <div class='live-counter' id='growth-counter'>+{current_stats['growth_rate']}%</div>
            <p style='color: #8B4C8C; margin: 5px 0 0 0; font-weight: bold;'>📈 Market Growth</p>
            <p style='color: #28a745; margin: 2px 0 0 0; font-size: 0.8rem;'>🚀 Accelerating</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='metric-card updating'>
            <div class='live-counter' id='ai-counter'>{current_stats['ai_jobs']:,}</div>
            <p style='color: #8B4C8C; margin: 5px 0 0 0; font-weight: bold;'>🎯 AI/ML Jobs</p>
            <p style='color: #ff6b35; margin: 2px 0 0 0; font-size: 0.8rem;'>🔥 Ultra Hot!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 📈 LIVE FLOWING CHART
    st.markdown("### 📈 Live Market Stream (Real-Time)")
    
    # Generate ultra-smooth streaming data
    dates = pd.date_range(start=datetime.now() - timedelta(minutes=30), end=datetime.now(), freq='1min')
    current_second = datetime.now().second
    current_microsecond = datetime.now().microsecond
    
    # Create flowing, realistic data streams
    base_time = time.time()
    
    trend_data = pd.DataFrame({
        'Time': dates,
        'AI/ML Jobs': [
            200 + i*2 + 30*math.sin(i/3 + base_time/2) + 15*math.sin(i/1.5 + base_time/3) 
            for i in range(len(dates))
        ],
        'Data Science': [
            150 + i*1.5 + 25*math.sin(i/4 + base_time/2.5) + 12*math.sin(i/2 + base_time/4) 
            for i in range(len(dates))
        ],
        'Software Engineering': [
            300 + i*1 + 40*math.sin(i/5 + base_time/3) + 20*math.sin(i/2.5 + base_time/5) 
            for i in range(len(dates))
        ]
    })
    
    # Create animated line chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=trend_data['Time'], 
        y=trend_data['AI/ML Jobs'],
        mode='lines+markers',
        name='AI/ML Jobs',
        line=dict(color='#FFB3D9', width=3),
        marker=dict(size=6)
    ))
    
    fig.add_trace(go.Scatter(
        x=trend_data['Time'], 
        y=trend_data['Data Science'],
        mode='lines+markers',
        name='Data Science',
        line=dict(color='#E6D7FF', width=3),
        marker=dict(size=6)
    ))
    
    fig.add_trace(go.Scatter(
        x=trend_data['Time'], 
        y=trend_data['Software Engineering'],
        mode='lines+markers',
        name='Software Engineering',
        line=dict(color='#C8E6C9', width=3),
        marker=dict(size=6)
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(255,255,255,0.9)',
        font_color='#8B4C8C',
        title=f"📊 Live Job Stream • {current_stats['timestamp']} • 🔴 STREAMING",
        xaxis_title="Time (Live)",
        yaxis_title="Job Postings",
        hovermode='x unified',
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ⚡ ULTRA-FAST ACTIVITY STREAM
    st.markdown("### ⚡ Live Activity Stream (Ultra-Fast Updates)")
    
    activities = [
        f"🔍 LIVE: Scraped {random.randint(10, 50)} jobs • LinkedIn",
        f"🤖 AI analyzed {random.randint(20, 100)} descriptions • {random.randint(1, 3)}s ago", 
        f"📊 TREND: AI jobs spike +{random.randint(2, 15)}% • NOW",
        f"💰 SALARY: {random.choice(['Google', 'Meta', 'Amazon'])} updated rates • {random.randint(1, 30)}s ago",
        f"🎯 HOT: {random.choice(['Python', 'React', 'AWS', 'ML', 'Docker'])} demand surge • LIVE",
        f"🏢 HIRING: {random.randint(2, 15)} companies started mass hiring • {random.randint(1, 60)}s ago",
        f"📈 MARKET: Growth rate jumped to +{random.randint(25, 35)}% • BREAKING",
        f"🚨 ALERT: Remote positions +{random.randint(10, 25)}% • {random.randint(1, 45)}s ago"
    ]
    
    for i, activity in enumerate(random.sample(activities, 5)):
        is_new = random.choice([True, False])
        activity_class = "activity-item new" if is_new else "activity-item"
        
        st.markdown(f"""
        <div class='{activity_class}'>
            <span class='live-indicator'></span>
            <strong>{activity}</strong>
            <span style='float: right; color: #28a745; font-size: 0.8rem; font-weight: bold;'>LIVE</span>
        </div>
        """, unsafe_allow_html=True)

else:
    # Other pages with live metrics
    st.markdown(f"## {page}")
    st.markdown("🚧 Advanced features in development!")
    
    # Mini live dashboard for other pages
    stats = get_live_stats()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🔥 Live Count", f"{stats['jobs_today']:,}", f"+{random.randint(5, 50)}")
    with col2:
        st.metric("💰 Live Salary", f"${stats['avg_salary']:,}", f"+{random.randint(1, 8)}%") 
    with col3:
        st.metric("📈 Live Growth", f"+{stats['growth_rate']}%", f"+{random.randint(1, 5)}")

# 🔄 ULTRA-FAST AUTO-REFRESH (3 seconds like stock market)
time.sleep(3)
st.rerun()

# Footer with Live Status
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; padding: 25px; background: rgba(255,255,255,0.2); border-radius: 15px; margin-top: 30px; backdrop-filter: blur(10px);'>
    <p style='color: #8B4C8C; margin: 0;'>💎 <strong>CareerCrystal</strong> - Built with ❤️ using AI & Real-Time Technology</p>
    <p style='color: #8B4C8C; margin: 5px 0 0 0; font-size: 0.9rem;'>
        🤖 Autonomous • 🎨 Crystal Background • ⚡ 3-Second Updates • 
        <span class='live-indicator'></span>
        <strong>ULTRA-LIVE STREAM</strong>
    </p>
    <p style='color: #28a745; margin: 5px 0 0 0; font-size: 0.8rem; font-weight: bold;'>
        🔴 STREAMING LIVE • Updated: {current_stats['timestamp']}
    </p>
</div>
""", unsafe_allow_html=True)

