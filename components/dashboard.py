import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import json

def render_dashboard():
    """🏠 Main Dashboard Component - Real-time job market overview"""
    
    st.markdown("""
    <div style='background: linear-gradient(90deg, #FFB3D9, #E6D7FF); padding: 20px; border-radius: 15px; margin-bottom: 30px;'>
        <h1 style='color: white; text-align: center; margin: 0;'>🏠 CareerCrystal Dashboard</h1>
        <p style='color: white; text-align: center; margin: 5px 0 0 0;'>Real-time job market intelligence at your fingertips</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 📊 Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style='background: rgba(255,179,217,0.3); padding: 20px; border-radius: 15px; text-align: center;'>
            <h2 style='color: #8B4C8C; margin: 0;'>🔥 2,847</h2>
            <p style='color: #8B4C8C; margin: 5px 0 0 0;'>New Jobs Today</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(230,215,255,0.3); padding: 20px; border-radius: 15px; text-align: center;'>
            <h2 style='color: #8B4C8C; margin: 0;'>💰 $92K</h2>
            <p style='color: #8B4C8C; margin: 5px 0 0 0;'>Avg Salary</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: rgba(200,230,201,0.3); padding: 20px; border-radius: 15px; text-align: center;'>
            <h2 style='color: #8B4C8C; margin: 0;'>📈 +27%</h2>
            <p style='color: #8B4C8C; margin: 5px 0 0 0;'>Market Growth</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style='background: rgba(255,248,220,0.3); padding: 20px; border-radius: 15px; text-align: center;'>
            <h2 style='color: #8B4C8C; margin: 0;'>🎯 AI/ML</h2>
            <p style='color: #8B4C8C; margin: 5px 0 0 0;'>Hottest Skill</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 📊 Market Trends Chart
    st.markdown("### 📈 Live Job Market Trends")
    
    # Generate realistic sample data
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
    trend_data = pd.DataFrame({
        'Date': dates,
        'AI/ML Jobs': [200 + i*8 + (i%5)*15 for i in range(len(dates))],
        'Data Science': [150 + i*6 + (i%4)*12 for i in range(len(dates))],
        'Software Engineering': [300 + i*4 + (i%6)*18 for i in range(len(dates))],
        'Product Management': [100 + i*3 + (i%7)*10 for i in range(len(dates))]
    })
    
    fig = px.area(trend_data, x='Date', 
                  y=['AI/ML Jobs', 'Data Science', 'Software Engineering', 'Product Management'],
                  color_discrete_map={
                      'AI/ML Jobs': '#FFB3D9',
                      'Data Science': '#E6D7FF',
                      'Software Engineering': '#C8E6C9',
                      'Product Management': '#FFF8DC'
                  })
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(255,255,255,0.9)',
        font_color='#8B4C8C',
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 🔥 Hot Companies Section
    st.markdown("### 🔥 Companies Hiring Most")
    
    companies_col1, companies_col2 = st.columns(2)
    
    with companies_col1:
        company_data = pd.DataFrame({
            'Company': ['Google', 'Microsoft', 'Amazon', 'Meta', 'Apple'],
            'Open Positions': [847, 692, 1203, 456, 378],
            'Avg Salary': [165000, 142000, 138000, 158000, 172000]
        })
        
        fig_companies = px.bar(company_data, x='Company', y='Open Positions',
                              color='Open Positions', color_continuous_scale='Pinkyl')
        fig_companies.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(255,255,255,0.9)',
            font_color='#8B4C8C'
        )
        st.plotly_chart(fig_companies, use_container_width=True)
    
    with companies_col2:
        st.markdown("""
        <div style='background: rgba(255,255,255,0.9); padding: 20px; border-radius: 15px; height: 400px; overflow-y: auto;'>
            <h4 style='color: #8B4C8C;'>📊 Top Hiring Companies</h4>
            <div style='margin: 10px 0; padding: 10px; background: rgba(255,179,217,0.2); border-radius: 8px;'>
                <strong>🔥 Google</strong><br>
                847 open positions • $165K avg
            </div>
            <div style='margin: 10px 0; padding: 10px; background: rgba(230,215,255,0.2); border-radius: 8px;'>
                <strong>💻 Microsoft</strong><br>
                692 open positions • $142K avg
            </div>
            <div style='margin: 10px 0; padding: 10px; background: rgba(200,230,201,0.2); border-radius: 8px;'>
                <strong>📦 Amazon</strong><br>
                1,203 open positions • $138K avg
            </div>
            <div style='margin: 10px 0; padding: 10px; background: rgba(255,248,220,0.2); border-radius: 8px;'>
                <strong>👥 Meta</strong><br>
                456 open positions • $158K avg
            </div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_dashboard()

