import streamlit as st
import sys
import os
import pandas as pd

# Add all paths
sys.path.append(os.path.join(os.path.dirname(__file__), 'components'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'automation'))

from dashboard import render_dashboard
from ai_insights import render_ai_insights  
from automation_panel import render_automation_panel
from scraper import JobScraper

# 💎 CareerCrystal Configuration
st.set_page_config(
    page_title="💎 CareerCrystal - AI Job Intelligence",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Beautiful styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #FFB3D9 0%, #E6D7FF 25%, #C8E6C9 50%, #FFF8DC 75%, #FFDAB9 100%);
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #FFB3D9 0%, #E6D7FF 100%);
    }
    
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.9);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 🌟 Sidebar Navigation  
with st.sidebar:
    st.markdown("# 💎 CareerCrystal")
    st.markdown("*AI-Powered Job Intelligence Platform*")
    st.markdown("---")
    
    page = st.selectbox("🧭 Navigate", [
        "🏠 Dashboard", 
        "📊 Market Trends", 
        "💰 Salary Intelligence",
        "🔮 AI Insights",
        "⚙️ Automation Center",
        "🔧 Data Scraper"
    ])
    
    st.markdown("---")
    st.markdown("### 🤖 Automation Status")
    st.markdown("🟢 **Active** - Running 24/7")
    st.markdown("📈 **2,847** jobs scanned today")
    st.markdown("🔥 **AI Analysis** updated 2h ago")

# 📱 Route to different pages
if page == "🏠 Dashboard":
    render_dashboard()
    
elif page == "🔮 AI Insights":
    render_ai_insights()
    
elif page == "⚙️ Automation Center":
    render_automation_panel()
    
elif page == "🔧 Data Scraper":
    st.markdown("## 🔍 Advanced Job Data Scraper")
    st.markdown("*Real-time job data collection from multiple sources*")
    
    scraper_col1, scraper_col2 = st.columns(2)
    
    with scraper_col1:
        if st.button("🚀 Quick Scrape (GitHub Jobs)", type="primary"):
            scraper = JobScraper()
            with st.spinner("🔍 Scanning GitHub for opportunities..."):
                jobs = scraper.scrape_github_jobs()
                
                st.success(f"✅ Found {len(jobs)} GitHub jobs!")
                
                for job in jobs:
                    st.markdown(f"""
                    <div style='background: rgba(255,255,255,0.9); padding: 15px; margin: 10px 0; border-radius: 10px; border-left: 4px solid #FFB3D9;'>
                        <h4 style='color: #8B4C8C; margin: 0;'>{job['title']}</h4>
                        <p style='margin: 5px 0;'><strong>🏢 Company:</strong> {job['company']}</p>
                        <p style='margin: 5px 0;'><strong>📍 Location:</strong> {job['location']}</p>
                        <p style='margin: 5px 0;'><strong>💰 Salary:</strong> {job['salary']}</p>
                        <p style='margin: 5px 0;'><strong>🛠️ Skills:</strong> {', '.join(job['skills'])}</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    with scraper_col2:
        if st.button("🌍 Full Market Scan", type="secondary"):
            scraper = JobScraper()
            with st.spinner("🌐 Comprehensive market scanning..."):
                all_jobs = scraper.get_all_jobs()
                scraper.save_jobs_data(all_jobs)
                
                st.success(f"🎉 Complete! Scanned {len(all_jobs)} total opportunities!")
                
                # Show summary stats
                companies = list(set([job['company'] for job in all_jobs]))
                locations = list(set([job['location'] for job in all_jobs]))
                
                st.markdown(f"""
                <div style='background: rgba(200,230,201,0.3); padding: 20px; border-radius: 15px; margin-top: 20px;'>
                    <h3 style='color: #8B4C8C;'>📊 Scan Summary</h3>
                    <p><strong>Total Jobs:</strong> {len(all_jobs)}</p>
                    <p><strong>Companies:</strong> {len(companies)}</p>
                    <p><strong>Locations:</strong> {len(locations)}</p>
                    <p><strong>Data Saved:</strong> ✅ jobs_database.json</p>
                </div>
                """, unsafe_allow_html=True)

else:
    st.markdown(f"## {page}")
    st.markdown("🚧 *This amazing feature is coming soon!*")
    st.markdown("CareerCrystal is constantly evolving with new AI-powered capabilities.")
    
    # Show preview of what's coming
    st.markdown("""
    ### 🔮 What's Coming Next:
    - 📊 **Advanced Market Trends** - Deep dive analytics with predictive insights
    - 💰 **Salary Intelligence** - AI-powered salary negotiations and benchmarking  
    - 🎯 **Smart Job Matching** - Personalized job recommendations based on your profile
    - 📱 **Mobile Alerts** - Real-time notifications for perfect job matches
    - 🤝 **Social Integration** - Share insights on LinkedIn, Twitter, and more
    """)
    
    st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 10px; margin-top: 30px;'>
    <p style='color: #8B4C8C; margin: 0;'>💎 <strong>CareerCrystal</strong> - Built with ❤️ using AI & Beautiful Design</p>
    <p style='color: #8B4C8C; margin: 5px 0 0 0; font-size: 0.9rem;'>🤖 Autonomous • 🎨 Beautiful • 🚀 Intelligent • 2025</p>
</div>
""", unsafe_allow_html=True)
