from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

# Live API link for real data
REMOTIVE_API_URL = "https://remotive.com"

def fetch_live_jobs():
    try:
        response = requests.get(REMOTIVE_API_URL, timeout=10)
        if response.status_code == 200:
            return response.json().get("jobs", [])
    except Exception as e:
        print(f"Error fetching live data: {e}")
    return []

@app.route("/")
def home():
    live_jobs = fetch_live_jobs()
    return render_template("index.html", jobs=live_jobs)

@app.route("/job/<int:job_id>")
def job_detail(job_id):
    live_jobs = fetch_live_jobs()
    selected_job = next((j for j in live_jobs if j["id"] == job_id), None)
    if not selected_job:
        abort(404)
    return render_template("job_detail.html", job=selected_job)

if __name__ == "__main__":
    # Replit par chalane ke liye host 0.0.0.0 zaroori hai
    app.run(host="0.0.0.0", port=8080)
