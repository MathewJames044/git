import os
import json
import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pywebpush import webpush, WebPushException
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

# Local imports
from . import roadmap_data

load_dotenv()

PKT = ZoneInfo("Asia/Karachi")

app = FastAPI()

# VAPID Keys
VAPID_PRIVATE_KEY = os.getenv("VAPID_PRIVATE_KEY")
VAPID_PUBLIC_KEY = os.getenv("VAPID_PUBLIC_KEY")
VAPID_CLAIMS = {"sub": "mailto:your-email@example.com"}

# Paths based on root directory (assuming current file is in backend/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBSCRIPTIONS_FILE = os.path.join(BASE_DIR, "subscriptions.json")
LOG_FILE = os.path.join(BASE_DIR, "task_log.json")

if not os.path.exists(SUBSCRIPTIONS_FILE):
    with open(SUBSCRIPTIONS_FILE, "w") as f:
        json.dump([], f)

# Roadmap Start Date
ROADMAP_START = datetime.date(2026, 2, 28) # Default

class Subscription(BaseModel):
    endpoint: str
    keys: dict

@app.post("/subscribe")
async def subscribe(subscription: Subscription):
    subs = []
    with open(SUBSCRIPTIONS_FILE, "r") as f:
        subs = json.load(f)
    
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
    now = datetime.datetime.now(tz=PKT)
    current_time = now.strftime("%H:%M")
    print(f"[Scheduler] Tick at {current_time} PKT")

    today_pkt = now.date()
    info = roadmap_data.get_current_roadmap_info(ROADMAP_START, today_pkt)
    if not info or "schedule" not in info:
        return

    current_hhmm_12 = now.strftime("%I:%M %p").lstrip('0')
    current_hhmm_24 = now.strftime("%H:%M")

    target_slot = None
    for slot in info["schedule"]:
        start_time_part = slot["time"].split('–')[0].strip()
        if start_time_part == current_hhmm_12 or start_time_part.lstrip('0') == current_hhmm_12:
            target_slot = slot
            break

    if not target_slot:
        for time_str, label, template in roadmap_data.DAILY_SCHEDULE:
            if time_str == current_hhmm_24:
                try:
                    notification_data = {
                        "title": label,
                        "body": template.format(**info),
                        "icon": "/icons/icon-192x192.png"
                    }
                    send_to_all(notification_data)
                except Exception as e:
                    print(f"[Scheduler] Legacy notify error: {e}")
                return

    if target_slot:
        notification_data = {
            "title": f"🚀 {target_slot['topic']}",
            "body": f"Time: {target_slot['time']}\nTask: {target_slot['task']}\nRole: {target_slot['role']}",
            "icon": "/icons/icon-192x192.png"
        }
        send_to_all(notification_data)

def send_to_all(notification_data):
    try:
        with open(SUBSCRIPTIONS_FILE, "r") as f:
            subs = json.load(f)
        if not subs: return
        for sub in subs:
            send_push_notification(sub, notification_data)
    except Exception as ex:
        print(f"[Scheduler] Error: {ex}")

# Scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(roadmap_job, "cron", minute="*")
scheduler.start()

# API for Frontend
@app.get("/api/today")
async def get_today():
    today_pkt = datetime.datetime.now(tz=PKT).date()
    info = roadmap_data.get_current_roadmap_info(ROADMAP_START, today_pkt)
    return info

@app.get("/api/test-push")
async def test_push():
    with open(SUBSCRIPTIONS_FILE, "r") as f:
        subs = json.load(f)
    if not subs: return {"status": "error", "message": "No subscriptions"}
    
    test_data = {
        "title": "🚀 Test Notification",
        "body": "System ready!",
        "icon": "/icons/icon-192x192.png"
    }
    for sub in subs:
        send_push_notification(sub, test_data)
    return {"status": "success"}

def load_log():
    if not os.path.exists(LOG_FILE): return {}
    with open(LOG_FILE, "r") as f: return json.load(f)

def save_log(log):
    with open(LOG_FILE, "w") as f: json.dump(log, f, indent=2)

class LogEntry(BaseModel):
    date: str
    completed: list
    notes: str = ""

@app.post("/api/log")
async def save_task_log(entry: LogEntry):
    log = load_log()
    log[entry.date] = {"completed": entry.completed, "notes": entry.notes}
    save_log(log)
    return {"status": "saved"}

@app.get("/api/log/{date}")
async def get_day_log(date: str):
    log = load_log()
    return log.get(date, {"completed": [], "notes": ""})

@app.get("/api/history")
async def get_history():
    log = load_log()
    history = []
    for date_str, data in sorted(log.items(), reverse=True):
        try:
            d = datetime.date.fromisoformat(date_str)
            delta = (d - ROADMAP_START).days
            week = (delta // 7) + 1
            day_idx = delta % 7
            if 1 <= week <= 13:
                history.append({
                    "date": date_str,
                    "week": week,
                    "day_idx": day_idx,
                    "day_name": roadmap_data.get_day_name(day_idx),
                    "abs_day": delta + 1,
                    "completed_count": len(data.get("completed", [])),
                    "completed": data.get("completed", []),
                    "notes": data.get("notes", ""),
                })
        except Exception: pass
    return history

@app.get("/api/stats")
async def get_stats():
    log = load_log()
    today_pkt = datetime.datetime.now(tz=PKT).date()
    abs_day_raw = (today_pkt - ROADMAP_START).days + 1
    abs_day = min(max(abs_day_raw, 1), 90)

    weighted_days = 0.0
    total_completed = 0
    total_possible_sum = 0

    for day_offset in range(abs_day):
        d = ROADMAP_START + datetime.timedelta(days=day_offset)
        date_str = d.isoformat()
        week = (day_offset // 7) + 1
        day_idx = day_offset % 7
        if not (1 <= week <= 13): continue

        schedule = roadmap_data.build_detailed_day_schedule(week, day_idx)
        trackable = [s for s in schedule if s["category"] != "sleep"]
        day_total = len(trackable) or 1
        day_log = log.get(date_str, {})
        day_done = len(day_log.get("completed", []))

        total_completed += day_done
        total_possible_sum += day_total
        weighted_days += min(day_done / day_total, 1.0)

    overall_pct = round((weighted_days / 90) * 100, 1)
    today_str = today_pkt.isoformat()
    today_log = log.get(today_str, {"completed": []})
    today_done = len(today_log.get("completed", []))
    
    delta_t = (today_pkt - ROADMAP_START).days
    week_t = (delta_t // 7) + 1
    day_idx_t = delta_t % 7
    if 1 <= week_t <= 13:
        sched_t = roadmap_data.build_detailed_day_schedule(week_t, day_idx_t)
        today_total = len([s for s in sched_t if s["category"] != "sleep"])
    else: today_total = 14

    today_pct = round((today_done / today_total) * 100, 1) if today_total else 0

    return {
        "abs_day": abs_day,
        "overall_pct": overall_pct,
        "total_completed": total_completed,
        "total_possible": total_possible_sum,
        "today_completed": today_done,
        "today_completed_indices": today_log.get("completed", []),
        "today_total": today_total,
        "today_pct": today_pct,
    }

# Serve static files
STATIC_DIR = os.path.join(BASE_DIR, "static")
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
