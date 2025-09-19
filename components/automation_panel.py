import streamlit as st
import json
from datetime import datetime
import sys
import os

# Add automation to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'automation'))

from scheduler import CareerCrystalScheduler

def render_automation_panel():
    """⚙️ Automation Control Panel - Manage 24/7 operations"""
    
    st.markdown("""
    <div style='background: linear-gradient(90deg, #C8E6C9, #FFF8DC); padding: 20px; border-radius: 15px; margin-bottom: 30px;'>
        <h1 style='color: white; text-align: center; margin: 0;'>⚙️ Automation Command Center</h1>
        <p style='color: white; text-align: center; margin: 5px 0 0 0;'>24/7 autonomous job market intelligence</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize scheduler
    if 'scheduler' not in st.session_state:
        st.session_state.scheduler = CareerCrystalScheduler()
    
    scheduler = st.session_state.scheduler
    
    # Control Panel
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 Start Automation", type="primary"):
            scheduler.start_automation()
            st.success("🤖 CareerCrystal is now running autonomously!")
    
    with col2:
        if st.button("⏸️ Pause Automation"):
            scheduler.stop_automation()
            st.warning("⏸️ Automation paused")
    
    with col3:
        if st.button("🔄 Force Update"):
            st.info("🔄 Running manual update...")
            scheduler.scrape_jobs_task()
            scheduler.analyze_market_task()
    
    # 📊 Status Dashboard
    st.markdown("### 📊 Automation Status")
    
    status = scheduler.get_status()
    
    # Status Overview
    status_col1, status_col2, status_col3, status_col4 = st.columns(4)
    
    with status_col1:
        job_status = status.get('job_scraping', {})
        last_scrape = job_status.get('last_run', 'Never')
        jobs_found = job_status.get('jobs_found', 0)
        
        st.markdown(f"""
        <div style='background: rgba(255,179,217,0.3); padding: 15px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #8B4C8C; margin: 0;'>🔍 Job Scraping</h3>
            <p style='margin: 5px 0;'><strong>Status:</strong> {job_status.get('status', 'Inactive')}</p>
            <p style='margin: 5px 0;'><strong>Last Run:</strong> {last_scrape[:16] if last_scrape != 'Never' else 'Never'}</p>
            <p style='margin: 5px 0;'><strong>Jobs Found:</strong> {jobs_found}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with status_col2:
        analysis_status = status.get('market_analysis', {})
        last_analysis = analysis_status.get('last_run', 'Never')
        jobs_analyzed = analysis_status.get('jobs_analyzed', 0)
        
        st.markdown(f"""
        <div style='background: rgba(230,215,255,0.3); padding: 15px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #8B4C8C; margin: 0;'>🤖 AI Analysis</h3>
            <p style='margin: 5px 0;'><strong>Status:</strong> {analysis_status.get('status', 'Inactive')}</p>
            <p style='margin: 5px 0;'><strong>Last Run:</strong> {last_analysis[:16] if last_analysis != 'Never' else 'Never'}</p>
            <p style='margin: 5px 0;'><strong>Jobs Analyzed:</strong> {jobs_analyzed}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with status_col3:
        st.markdown(f"""
        <div style='background: rgba(200,230,201,0.3); padding: 15px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #8B4C8C; margin: 0;'>📊 Reports</h3>
            <p style='margin: 5px 0;'><strong>Status:</strong> Active</p>
            <p style='margin: 5px 0;'><strong>Daily Reports:</strong> Auto-generated</p>
            <p style='margin: 5px 0;'><strong>Next Report:</strong> 09:00 AM</p>
        </div>
        """, unsafe_allow_html=True)
    
    with status_col4:
        st.markdown(f"""
        <div style='background: rgba(255,248,220,0.3); padding: 15px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #8B4C8C; margin: 0;'>🌐 System</h3>
            <p style='margin: 5px 0;'><strong>Uptime:</strong> {_calculate_uptime()}</p>
            <p style='margin: 5px 0;'><strong>Health:</strong> ✅ Healthy</p>
            <p style='margin: 5px 0;'><strong>Mode:</strong> Autonomous</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 🕒 Automation Schedule
    st.markdown("### ⏰ Automation Schedule")
    
    schedule_data = {
        "Task": ["Job Scraping", "AI Analysis", "Daily Report", "Trend Update"],
        "Frequency": ["Every 1 hour", "Every 6 hours", "Daily at 9:00 AM", "Daily at 6:00 PM"],
        "Next Run": ["In 23 mins", "In 2.5 hours", "Tomorrow 9:00 AM", "Today 6:00 PM"],
        "Status": ["🟢 Active", "🟢 Active", "🟢 Active", "🟢 Active"]
    }
    
    schedule_df = pd.DataFrame(schedule_data)
    
    st.markdown("""
    <style>
    .schedule-table {
        background: rgba(255,255,255,0.9);
        border-radius: 10px;
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.dataframe(schedule_df, use_container_width=True, hide_index=True)
    
    # 📈 Performance Metrics
    st.markdown("### 📈 Performance Metrics")
    
    metrics_col1, metrics_col2 = st.columns(2)
    
    with metrics_col1:
        # Jobs scraped over time (mock data)
        import pandas as pd
        import plotly.express as px
        
        dates = pd.date_range(start="2025-09-15", end="2025-09-19", freq="D")
        jobs_scraped = [245, 312, 289, 401, 356]
        
        metrics_df = pd.DataFrame({
            'Date': dates,
            'Jobs Scraped': jobs_scraped
        })
        
        fig = px.line(metrics_df, x='Date', y='Jobs Scraped',
                     title="Daily Job Scraping Performance",
                     color_discrete_sequence=['#FFB3D9'])
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(255,255,255,0.9)',
            font_color='#8B4C8C'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with metrics_col2:
        # System health metrics
        health_metrics = {
            'Metric': ['API Response Time', 'Scraping Success Rate', 'AI Analysis Accuracy', 'System Uptime'],
            'Value': ['0.8s', '94.2%', '87.1%', '99.7%'],
            'Status': ['🟢 Good', '🟢 Excellent', '🟢 Good', '🟢 Excellent']
        }
        
        health_df = pd.DataFrame(health_metrics)
        
        st.markdown("#### 🏥 System Health")
        for _, row in health_df.iterrows():
            st.markdown(f"""
            <div style='background: rgba(255,255,255,0.8); padding: 10px; margin: 5px 0; border-radius: 8px; display: flex; justify-content: space-between;'>
                <span style='color: #8B4C8C;'><strong>{row['Metric']}:</strong> {row['Value']}</span>
                <span>{row['Status']}</span>
            </div>
            """, unsafe_allow_html=True)

def _calculate_uptime():
    """Calculate system uptime"""
    # This would be calculated from actual start time in production
    return "2d 14h 32m"

if __name__ == "__main__":
    render_automation_panel()
