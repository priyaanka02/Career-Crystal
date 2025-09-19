import schedule
import time
import threading
import json
from datetime import datetime, timedelta
import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.scraper import JobScraper
from utils.ai_processor import CareerCrystalAI

class CareerCrystalScheduler:
    """⏰ 24/7 Automation Engine - Keeps CareerCrystal running autonomously"""
    
    def __init__(self):
        self.scraper = JobScraper()
        self.ai = CareerCrystalAI()
        self.is_running = False
        self.last_run = None
        self.status_file = "data/scheduler_status.json"
        
    def start_automation(self):
        """🚀 Start the autonomous operation"""
        
        self.is_running = True
        
        # Schedule different tasks
        schedule.every(1).hours.do(self.scrape_jobs_task)
        schedule.every(6).hours.do(self.analyze_market_task)
        schedule.every().day.at("09:00").do(self.generate_daily_report_task)
        schedule.every().day.at("18:00").do(self.update_trends_task)
        
        # Run in background thread
        scheduler_thread = threading.Thread(target=self._run_scheduler, daemon=True)
        scheduler_thread.start()
        
        st.success("🚀 CareerCrystal automation is now running 24/7!")
        return scheduler_thread
    
    def _run_scheduler(self):
        """Internal scheduler loop"""
        while self.is_running:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    def scrape_jobs_task(self):
        """🔍 Automated job scraping task"""
        try:
            st.info("🔍 Starting automated job scraping...")
            
            # Scrape new jobs
            jobs = self.scraper.get_all_jobs()
            
            # Load existing data
            existing_jobs = self.scraper.load_jobs_data()
            
            # Merge and deduplicate
            all_jobs = existing_jobs + jobs
            unique_jobs = self._deduplicate_jobs(all_jobs)
            
            # Save updated data
            self.scraper.save_jobs_data(unique_jobs)
            
            # Update status
            self._update_status("job_scraping", {
                "last_run": datetime.now().isoformat(),
                "jobs_found": len(jobs),
                "total_jobs": len(unique_jobs),
                "status": "success"
            })
            
            st.success(f"✅ Scraped {len(jobs)} new jobs! Total: {len(unique_jobs)}")
            
        except Exception as e:
            st.error(f"❌ Job scraping failed: {str(e)}")
            self._update_status("job_scraping", {
                "last_run": datetime.now().isoformat(),
                "status": "error",
                "error": str(e)
            })
    
    def analyze_market_task(self):
        """🤖 Automated market analysis task"""
        try:
            st.info("🤖 Running AI market analysis...")
            
            # Load job data
            jobs = self.scraper.load_jobs_data()
            
            # Generate AI insights
            analysis = self.ai.analyze_job_trends(jobs)
            
            # Save analysis
            with open("data/market_analysis.json", 'w') as f:
                json.dump(analysis, f, indent=2)
            
            self._update_status("market_analysis", {
                "last_run": datetime.now().isoformat(),
                "jobs_analyzed": len(jobs),
                "status": "success"
            })
            
            st.success("🧠 AI market analysis completed!")
            
        except Exception as e:
            st.error(f"❌ Market analysis failed: {str(e)}")
    
    def generate_daily_report_task(self):
        """📊 Generate daily intelligence report"""
        try:
            st.info("📊 Generating daily market report...")
            
            jobs = self.scraper.load_jobs_data()
            
            # Load market trends
            try:
                with open("data/market_analysis.json", 'r') as f:
                    market_trends = json.load(f)
            except:
                market_trends = {}
            
            # Generate comprehensive report
            report = self.ai.generate_daily_report(jobs, market_trends)
            
            # Save report
            report_filename = f"data/daily_reports/report_{datetime.now().strftime('%Y_%m_%d')}.json"
            os.makedirs("data/daily_reports", exist_ok=True)
            
            with open(report_filename, 'w') as f:
                json.dump(report, f, indent=2)
            
            # Update latest report
            with open("data/latest_report.json", 'w') as f:
                json.dump(report, f, indent=2)
            
            st.success("📰 Daily report generated successfully!")
            
        except Exception as e:
            st.error(f"❌ Report generation failed: {str(e)}")
    
    def update_trends_task(self):
        """📈 Update market trends data"""
        try:
            st.info("📈 Updating market trends...")
            
            jobs = self.scraper.load_jobs_data()
            
            # Calculate trends
            trends = self._calculate_trends(jobs)
            
            # Save trends
            with open("data/market_trends.json", 'w') as f:
                json.dump(trends, f, indent=2)
            
            st.success("📊 Market trends updated!")
            
        except Exception as e:
            st.error(f"❌ Trends update failed: {str(e)}")
    
    def _deduplicate_jobs(self, jobs):
        """Remove duplicate jobs"""
        seen = set()
        unique_jobs = []
        
        for job in jobs:
            # Create unique identifier
            job_id = f"{job.get('title', '')}-{job.get('company', '')}-{job.get('location', '')}"
            
            if job_id not in seen:
                seen.add(job_id)
                unique_jobs.append(job)
        
        return unique_jobs
    
    def _calculate_trends(self, jobs):
        """Calculate market trends from job data"""
        if not jobs:
            return {"status": "no_data", "updated_at": datetime.now().isoformat()}
        
        # Extract skills
        all_skills = []
        for job in jobs:
            all_skills.extend(job.get('skills', []))
        
        # Calculate skill demand
        from collections import Counter
        skill_counts = Counter(all_skills)
        
        trends = {
            "total_jobs": len(jobs),
            "top_skills": dict(skill_counts.most_common(10)),
            "companies_hiring": len(set([job.get('company') for job in jobs if job.get('company')])),
            "remote_jobs": len([job for job in jobs if 'remote' in job.get('location', '').lower()]),
            "updated_at": datetime.now().isoformat()
        }
        
        return trends
    
    def _update_status(self, task_name, status_data):
        """Update scheduler status"""
        try:
            # Load existing status
            try:
                with open(self.status_file, 'r') as f:
                    status = json.load(f)
            except:
                status = {}
            
            # Update task status
            status[task_name] = status_data
            status['last_updated'] = datetime.now().isoformat()
            
            # Save status
            with open(self.status_file, 'w') as f:
                json.dump(status, f, indent=2)
                
        except Exception as e:
            print(f"Failed to update status: {e}")
    
    def get_status(self):
        """Get current scheduler status"""
        try:
            with open(self.status_file, 'r') as f:
                return json.load(f)
        except:
            return {"status": "not_started"}
    
    def stop_automation(self):
        """🛑 Stop the automation"""
        self.is_running = False
        schedule.clear()
        st.warning("🛑 Automation stopped")

# 🧪 Test scheduler
if __name__ == "__main__":
    scheduler = CareerCrystalScheduler()
    print("🤖 Starting CareerCrystal automation...")
    scheduler.start_automation()
    
    # Keep running
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        scheduler.stop_automation()
        print("👋 Automation stopped")
