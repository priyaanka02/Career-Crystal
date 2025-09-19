import streamlit as st
import json
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from ai_processor import CareerCrystalAI

def render_ai_insights():
    """🔮 AI-Powered Career Insights Dashboard"""
    
    st.markdown("""
    <div style='background: linear-gradient(90deg, #E6D7FF, #C8E6C9); padding: 20px; border-radius: 15px; margin-bottom: 30px;'>
        <h1 style='color: white; text-align: center; margin: 0;'>🔮 AI Career Intelligence</h1>
        <p style='color: white; text-align: center; margin: 5px 0 0 0;'>Smart insights powered by advanced AI analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load AI analysis data
    analysis_data = load_ai_analysis()
    
    if analysis_data:
        display_ai_analysis(analysis_data)
    else:
        display_generate_analysis()

def load_ai_analysis():
    """Load existing AI analysis"""
    try:
        with open("data/market_analysis.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except Exception as e:
        st.error(f"Error loading AI analysis: {e}")
        return None

def display_ai_analysis(analysis):
    """Display AI analysis results"""
    
    # 🧠 AI Trend Analysis
    st.markdown("### 🧠 AI Market Analysis")
    st.markdown(f"""
    <div style='background: rgba(230,215,255,0.3); padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        <h4 style='color: #8B4C8C; margin-top: 0;'>📊 Market Trend Analysis</h4>
        <p style='font-size: 1.1rem; color: #8B4C8C;'>{analysis.get('trend_analysis', 'No analysis available')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 🔥 Hot Skills Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔥 Most In-Demand Skills")
        hot_skills = analysis.get('hot_skills', [])
        
        for i, skill in enumerate(hot_skills[:5]):
            skill_popularity = 100 - (i * 15)  # Simulate popularity
            st.markdown(f"""
            <div style='background: rgba(255,179,217,0.2); padding: 10px; margin: 5px 0; border-radius: 8px; border-left: 4px solid #FFB3D9;'>
                <strong style='color: #8B4C8C;'>{skill}</strong>
                <div style='background: #FFB3D9; height: 8px; border-radius: 4px; width: {skill_popularity}%; margin-top: 5px;'></div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 💰 Salary Intelligence")
        salary_insights = analysis.get('salary_insights', 'Salary data being analyzed...')
        
        st.markdown(f"""
        <div style='background: rgba(200,230,201,0.2); padding: 15px; border-radius: 10px; height: 200px;'>
            <p style='color: #8B4C8C; margin: 0;'>{salary_insights}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 📈 Growth Prediction
    st.markdown("### 📈 AI Growth Predictions")
    growth_prediction = analysis.get('growth_prediction', 'Growth analysis in progress...')
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(255,179,217,0.2), rgba(230,215,255,0.2)); padding: 20px; border-radius: 15px;'>
        <h4 style='color: #8B4C8C; margin-top: 0;'>🚀 Market Growth Forecast</h4>
        <p style='font-size: 1.1rem; color: #8B4C8C;'>{growth_prediction}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 🎯 AI Recommendations
    st.markdown("### 🎯 Personalized AI Recommendations")
    recommendations = analysis.get('recommendations', [])
    
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"""
        <div style='background: rgba(255,248,220,0.3); padding: 15px; margin: 10px 0; border-radius: 10px; border-left: 4px solid #FFF8DC;'>
            <strong style='color: #8B4C8C;'>💡 Recommendation {i}:</strong>
            <p style='color: #8B4C8C; margin: 5px 0 0 0;'>{rec}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 📊 Skills Demand Chart
    if hot_skills:
        st.markdown("### 📊 Skills Demand Visualization")
        
        # Create skills demand chart
        skills_data = pd.DataFrame({
            'Skill': hot_skills[:5],
            'Demand Score': [95, 87, 82, 76, 71],  # Simulated demand scores
            'Growth Rate': ['+23%', '+18%', '+15%', '+12%', '+9%']
        })
        
        fig = px.bar(skills_data, x='Skill', y='Demand Score',
                     color='Demand Score', color_continuous_scale='Pinkyl',
                     title="AI-Analyzed Skills Demand Ranking")
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(255,255,255,0.9)',
            font_color='#8B4C8C'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # 🕒 Analysis Timestamp
    generated_at = analysis.get('generated_at', 'Unknown')
    st.markdown(f"""
    <p style='text-align: center; color: #8B4C8C; font-size: 0.9rem; margin-top: 30px;'>
        🤖 Analysis generated at: {generated_at}
    </p>
    """, unsafe_allow_html=True)

def display_generate_analysis():
    """Display interface to generate new analysis"""
    
    st.markdown("### 🤖 Generate AI Analysis")
    st.markdown("No AI analysis found. Generate fresh insights from current job market data!")
    
    if st.button("🚀 Generate AI Insights", type="primary"):
        with st.spinner("🧠 AI is analyzing job market data..."):
            ai = CareerCrystalAI()
            
            # Load job data
            try:
                with open("data/jobs_database.json", 'r') as f:
                    jobs_data = json.load(f).get('jobs', [])
            except:
                jobs_data = []
            
            # Generate analysis
            analysis = ai.analyze_job_trends(jobs_data)
            
            # Save analysis
            os.makedirs("data", exist_ok=True)
            with open("data/market_analysis.json", 'w') as f:
                json.dump(analysis, f, indent=2)
            
            st.success("✅ AI analysis generated successfully!")
            st.rerun()

if __name__ == "__main__":
    render_ai_insights()
