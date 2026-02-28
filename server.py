import os
import json
import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pywebpush import webpush, WebPushException
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import roadmap_data

load_dotenv()

app = FastAPI()

# VAPID Keys
VAPID_PRIVATE_KEY = os.getenv("VAPID_PRIVATE_KEY")
VAPID_PUBLIC_KEY = os.getenv("VAPID_PUBLIC_KEY")
VAPID_CLAIMS = {"sub": "mailto:your-email@example.com"}

SUBSCRIPTIONS_FILE = "subscriptions.json"

if not os.path.exists(SUBSCRIPTIONS_FILE):
    with open(SUBSCRIPTIONS_FILE, "w") as f:
        json.dump([], f)

# Roadmap Start Date
ROADMAP_START = datetime.date(2026, 2, 28) # Default to today

class Subscription(BaseModel):
    endpoint: str
    keys: dict

@app.post("/subscribe")
async def subscribe(subscription: Subscription):
    subs = []
    with open(SUBSCRIPTIONS_FILE, "r") as f:
        subs = json.load(f)
    
    # Avoid duplicates
    if subscription.endpoint not in [s["endpoint"] for s in subs]:
        subs.append(subscription.dict())
        with open(SUBSCRIPTIONS_FILE, "w") as f:
            json.dump(subs, f)
    
    return {"status": "success"}

@app.get("/vapid-public-key")
async def get_vapid_public_key():
    return {"publicKey": VAPID_PUBLIC_KEY}

def send_push_notification(subscription, data):
    try:
        webpush(
            subscription_info=subscription,
            data=json.dumps(data),
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims=VAPID_CLAIMS
        )
        return True
    except WebPushException as ex:
        print("Push failed:", repr(ex))
        return False

def roadmap_job():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    
    info = roadmap_data.get_current_roadmap_info(ROADMAP_START)
    if not info:
        return

    # Check daily schedule
    for time_str, label, template in roadmap_data.DAILY_SCHEDULE:
        if time_str == current_time:
            message = template.format(**info)
            notification_data = {
                "title": label,
                "body": message,
                "icon": "/icons/icon-192x192.png"
            }
            
            with open(SUBSCRIPTIONS_FILE, "r") as f:
                subs = json.load(f)
            
            for sub in subs:
                send_push_notification(sub, notification_data)
            print(f"[{current_time}] Sent notification: {label}")

# Scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(roadmap_job, "cron", minute="*") # Check every minute
scheduler.start()

# API for Frontend
@app.get("/api/today")
async def get_today():
    info = roadmap_data.get_current_roadmap_info(ROADMAP_START)
    return info

@app.get("/api/test-push")
async def test_push():
    with open(SUBSCRIPTIONS_FILE, "r") as f:
        subs = json.load(f)
    if not subs:
        return {"status": "error", "message": "No subscriptions found"}
    
    test_data = {
        "title": "🚀 Test Notification",
        "body": "System ready! Aapka 90-day roadmap active hai.",
        "icon": "/icons/icon-192x192.png"
    }
    for sub in subs:
        send_push_notification(sub, test_data)
    return {"status": "success"}

# Serve static files for PWA
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
