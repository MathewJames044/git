"""
╔══════════════════════════════════════════════════════════════════╗
║        90-DAY ROADMAP — WHATSAPP NOTIFICATION SYSTEM            ║
║        Powered by Twilio WhatsApp Sandbox API                    ║
║                                                                  ║
║  LOCAL:  python whatsapp_notifier.py                            ║
║  SERVER: Set environment variables on Railway dashboard          ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import schedule
import time
import datetime
import argparse # For custom messages
from twilio.rest import Client
from dotenv import load_dotenv # Load from .env file

# Load environment variables from .env
load_dotenv()

# ─────────────────────────────────────────────────────────────────
# ██  CONFIG — Environment Variables (Railway / Server)  ██
# ─────────────────────────────────────────────────────────────────
# IMPORTANT: Hardcoded keys ko remove kar diya hai for security.
# Server dashboard par inhein set karna zaroori hai.
TWILIO_ACCOUNT_SID   = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN    = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM          = os.environ.get("TWILIO_FROM", "whatsapp:+14155238886")
YOUR_NUMBER          = os.environ.get("YOUR_NUMBER", "whatsapp:+923232371066")

# Roadmap START date (YYYY, M, D)
# Default is TODAY (Feb 28), so it works immediately.
env_start = os.environ.get("ROADMAP_START_DATE")
if env_start:
    try:
        ROADMAP_START = datetime.datetime.strptime(env_start, "%Y-%m-%d").date()
    except ValueError:
        ROADMAP_START = datetime.date(2026, 2, 28)
else:
    ROADMAP_START = datetime.date(2026, 2, 28)

print(f"📅 Roadmap Start Date: {ROADMAP_START}")

# Check if credentials exist
if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
    print("\n❌ ERROR: TWILIO_ACCOUNT_SID ya TWILIO_AUTH_TOKEN missing hai!")
    print("   Note: Railway dashboard par 'Variables' tab mein inhein set karein.")
    print("   Local testing ke liye terminal mein 'set TWILIO_ACCOUNT_SID=...' run karein.")
    sys.exit(1)

# Initialize Client ONCE (Optimization)
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# ─────────────────────────────────────────────────────────────────
# WEEK DATA (matches your Roadmap.xlsx)
# ─────────────────────────────────────────────────────────────────
WEEK_FOCUS = {
    1:  "Node.js Internals + HTTP Server",
    2:  "Express.js Deep + Routing + Middleware",
    3:  "PostgreSQL + Schema Design + Auth",
    4:  "JWT + Env Management + Security",
    5:  "Clean Architecture + MVC Pattern",
    6:  "Error Handling + Logging + Production Design",
    7:  "Docker + Containerization",
    8:  "CI/CD + GitHub Actions",
    9:  "Redis + Queues + Async Workers",
    10: "Rate Limiting + Caching + Performance",
    11: "Monitoring + Health Checks + PM2",
    12: "Capstone – Full Backend Blueprint",
    13: "Review + Polish + GitHub Portfolio",
}

WEEK_ROLE = {
    1:  "🟢 Code Cadet",
    2:  "🟡 Route Commander",
    3:  "🟠 Data Architect",
    4:  "🔵 Security Operator",
    5:  "🔵 System Engineer",
    6:  "🔴 Stability Builder",
    7:  "🟤 Deployment Operator",
    8:  "⚫ Pipeline Architect",
    9:  "🟡 Async Specialist",
    10: "🔵 Performance Engineer",
    11: "🟣 Reliability Designer",
    12: "🔴 Production Architect",
    13: "🏆 Backend Engineer",
}

BACKEND_TASKS = {
    1:  ["Build simple HTTP server (no Express) — GET /hello",
         "Explore Node.js event loop — async code + callbacks",
         "Setup npm project, modular scripts",
         "Practice fs, path, os modules",
         "Build a CLI mini-tool using readline",
         "Read Node.js docs: Events, Streams, Timers",
         "MINI PROJECT: HTTP server with /hello /about /api routes"],
    2:  ["Install Express.js, understand req/res lifecycle",
         "Build RESTful CRUD routes for /tasks",
         "Implement middleware: logging, body parser",
         "Practice route params, query strings, nested routes",
         "Implement Express Router — split route files",
         "Add error middleware (4-param function)",
         "MINI PROJECT: Todo CRUD API with Router + Middleware"],
    3:  ["Connect PostgreSQL with pg npm module",
         "Design schema: users + tasks tables",
         "Write raw SQL: SELECT, INSERT, UPDATE, DELETE",
         "Intro to Prisma ORM — schema, migrate, CRUD",
         "Practice SQL JOINs",
         "Link PostgreSQL to Express API",
         "MINI PROJECT: Auth system — register, login, JWT + DB"],
    4:  ["Deep dive JWT: sign, verify, decode, expiry",
         "Setup dotenv — all secrets in .env",
         "Build authMiddleware — protect routes",
         "Implement token refresh endpoint",
         "Add Helmet.js + CORS to Express",
         "Practice: protect full API with auth + role check",
         "MINI PROJECT: Secure Auth with refresh token + protected routes"],
    5:  ["Study MVC pattern — Model, View, Controller",
         "Refactor API: separate controllers from routes",
         "Add service layer — business logic separation",
         "Implement repository pattern",
         "Add config management — env vars in config.js",
         "Refactor Todo API to MVC + Service + Repo",
         "MINI PROJECT: Clean MVC backend pushed to GitHub"],
    6:  ["Setup Winston logger — info, warn, error",
         "Build global error handler middleware",
         "Define custom error classes (ValidationError, etc.)",
         "Practice HTTP status codes map",
         "Add request logging middleware",
         "Write logs to rotating file (winston-daily-rotate-file)",
         "MINI PROJECT: Production-style API with centralized logger"],
    7:  ["Install Docker Desktop — images vs containers",
         "Write Dockerfile for Node.js app",
         "Build + run Docker image locally",
         "Setup docker-compose.yml — Node + PostgreSQL",
         "Understand Docker volumes",
         "Push image to Docker Hub",
         "MINI PROJECT: Full API containerized with docker-compose"],
    8:  ["Understand GitHub Actions: workflows, jobs, triggers",
         "Create CI workflow: on push — install + test",
         "Add Jest unit tests — 3 tests for API endpoints",
         "Integrate tests in GitHub Actions CI",
         "Understand CD concept",
         "Study GitHub secrets — store ENV securely",
         "MINI PROJECT: CI/CD pipeline running on GitHub"],
    9:  ["Install Redis — key-value store concept",
         "Install BullMQ — create queue + add jobs",
         "Build a worker process — consume jobs",
         "Implement email queue on user register",
         "Add retry logic + failure handling to BullMQ",
         "Monitor queues with Bull Board",
         "MINI PROJECT: Email queue worker with BullMQ + Redis"],
    10: ["Setup express-rate-limit — limit by IP",
         "Implement Redis caching — cache responses with TTL",
         "Understand cache invalidation",
         "Test response time with/without cache (Postman)",
         "Add compression middleware",
         "Apply caching to heavy DB query endpoint",
         "MINI PROJECT: Rate-limited + cached API with comparison"],
    11: ["Add /health endpoint — server + DB status",
         "Setup PM2 — process manager for production",
         "Configure PM2 ecosystem.config.js — cluster mode",
         "Implement graceful shutdown — handle SIGTERM",
         "Study log aggregation concept",
         "Add uptime monitoring (Better Uptime / ping check)",
         "MINI PROJECT: Monitored API with PM2 + health check"],
    12: ["Study load balancing — horizontal scaling",
         "Document full backend system design in README",
         "Explore database indexing",
         "Study API versioning — /api/v1 vs /api/v2",
         "Compare monolith vs microservices",
         "Design scalable e-commerce backend architecture",
         "CAPSTONE: Full backend system design on GitHub"],
    13: ["Review all 12 weeks — fill gaps",
         "Add proper README to each project repo",
         "Fix incomplete/buggy projects",
         "Polish GitHub profile — pin 3 best projects",
         "Write '90-Day Backend Journey' blog on Dev.to",
         "Plan next 90 days",
         "FINAL: Portfolio ready. Next roadmap set."],
}

WEEK_MILESTONE = {
    1:  "Simple HTTP Server working without Express",
    2:  "CRUD API with clean routing structure",
    3:  "Auth API with JWT + PostgreSQL working",
    4:  "Secure Token Refresh System complete",
    5:  "MVC backend skeleton deployed to GitHub",
    6:  "Production-style error + logging system",
    7:  "Node API containerized with Docker",
    8:  "GitHub Actions CI/CD pipeline running",
    9:  "Background email queue worker functional",
    10: "Rate-limited + cached API live",
    11: "Health check + monitored API deployed",
    12: "Full backend system design document done",
    13: "90-Day GitHub portfolio + identity shift",
}

# Daily schedule: (send_time_24h, label, message_template)
# These are the notifications you will receive every day.
DAILY_SCHEDULE = [
    ("07:00", "🌅 WAKE UP",
     "Subah ki shuru'aat!\n\n"
     "📋 Aaj ka focus:\n{week_focus}\n\n"
     "👤 Role: {role}\n"
     "📅 Day {abs_day} | Week {week}\n\n"
     "Top 3 tasks apne notebook mein likhein. Abhi!"),

    ("07:30", "🌱 PLANNING TIME",
     "Breakfast karo + din plan karo.\n\n"
     "Aaj ka backend task:\n\n"
     "🎯 {backend_task}\n\n"
     "Shuru se pehle plan, phir execution."),

    ("08:00", "🎧 AUDIO LEARNING (COMMUTE)",
     "Safar shuru! Yeh time waste mat karo.\n\n"
     "🎧 Aaj sunna hai: Backend concepts on YouTube/Podcast\n"
     "Topic: {week_focus}\n\n"
     "Earphones lagao. Chal do."),

    ("09:00", "💻 DEEP WORK START",
     "⚡ AB KAAM SHURU!\n\n"
     "Aaj ka task:\n"
     "🎯 {backend_task}\n\n"
     "✅ VSCode kholo\n"
     "✅ GitHub ready karo\n"
     "✅ Phone side mein rakhdo\n\n"
     "90 min no distraction. GO!"),

    ("12:30", "🌿 LUNCH BREAK",
     "Khaana khao + 10 min chhalna.\n\n"
     "Aaj ka progress?\n"
     "Backend task: {backend_task}\n\n"
     "Baad mein phir aao — fresh mind = better code."),

    ("16:00", "🔥 BACKEND DEEP SESSION",
     "Evening session — yeh sabse important hai!\n\n"
     "Week {week}: {week_focus}\n"
     "Aaj ka task:\n"
     "🎯 {backend_task}\n\n"
     "2 ghante. Pura focus. Abhi shuru karo."),

    ("18:30", "☕ CHAI BREAK",
     "Chai pi lo. 15-20 min relax karo.\n\n"
     "Backend session kaisa raha?\n"
     "Kuch naya seekha? Koi issue? Notebook mein likhna."),

    ("20:00", "🌿 DINNER + FAMILY",
     "Khaana + family time.\n\n"
     "Phone side mein rakhdo. Poori tarah offline.\n"
     "Yeh balance hi long-term engine chalata hai. 🙏"),

    ("21:00", "🧱 MINI PROJECT TIME",
     "Raat ka session:\n\n"
     "Week {week} Mini Project:\n"
     "🎯 {backend_task}\n\n"
     "Jo din mein chhoot gaya woh abhi karo.\n"
     "GitHub par push karo. Evidence banana zaroori hai!"),

    ("22:30", "🌟 REFLECTION + PLAN TOMORROW",
     "Aaj ka din khatam — score karo:\n\n"
     "✅ 3 wins aaj ke?\n"
     "⚠️ 1 improvement?\n"
     "📋 Kal ka plan set karo.\n\n"
     "Week {week} Milestone:\n"
     "🏆 {milestone}\n\n"
     "Consistency hi identity banti hai."),

    ("23:00", "📚 WIND DOWN",
     "Screen se hato. 30 min.\n\n"
     "Ek article ya kitaab padhna.\n"
     "Dev.to ya koi backend blog.\n\n"
     "Brain ko dheere dheere band karo."),

    ("23:30", "🛌 SLEEP NOW",
     "SONA AB MANDATORY HAI.\n\n"
     "Brain neend mein code consolidate karta hai.\n"
     "Kal aur productive hoge agar abhi so gaye.\n\n"
     "Good night. Week {week} — {role} 🌙"),
]

# ─────────────────────────────────────────────────────────────────
# CORE FUNCTIONS
# ─────────────────────────────────────────────────────────────────

def get_current_roadmap_info():
    """Calculate current week, day_index, abs_day based on ROADMAP_START."""
    today = datetime.date.today()
    delta = (today - ROADMAP_START).days
    if delta < 0:
        return None  # Roadmap hasn't started yet
    if delta >= 91:
        return None  # Roadmap completed (90 days)

    week = (delta // 7) + 1
    day_idx = delta % 7        # 0=Mon, 6=Sun
    abs_day = delta + 1        # 1–91

    if week > 13:
        week = 13

    return {
        "week": week,
        "day_idx": day_idx,
        "abs_day": abs_day,
        "week_focus": WEEK_FOCUS[week],
        "role": WEEK_ROLE[week],
        "backend_task": BACKEND_TASKS[week][min(day_idx, 6)],
        "milestone": WEEK_MILESTONE[week],
    }


def send_whatsapp(message: str):
    """Send a WhatsApp message via Twilio."""
    try:
        msg = twilio_client.messages.create(
            from_=TWILIO_FROM,
            to=YOUR_NUMBER,
            body=message
        )
        print(f"[{datetime.datetime.now().strftime('%H:%M')}] ✅ Sent: {msg.sid}")
    except Exception as e:
        print(f"[{datetime.datetime.now().strftime('%H:%M')}] ❌ ERROR: {e}")


def build_and_send(label: str, template: str):
    """Get today's roadmap data and send a formatted notification."""
    info = get_current_roadmap_info()
    if info is None:
        print(f"[{datetime.datetime.now().strftime('%H:%M')}] ℹ️  Roadmap not active yet or already completed.")
        return

    message = f"━━━━━━━━━━━━━━━━━━━━━━━\n{label}\n━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    message += template.format(**info)
    message += f"\n\n━━━━━━━━━━━━━━━━━━━━━━━"

    print(f"\n{'='*50}")
    print(f"SENDING: {label}")
    print(message)
    print(f"{'='*50}\n")
    send_whatsapp(message)


def send_test_message():
    """Send a test message to verify setup is working."""
    info = get_current_roadmap_info()
    if info:
        test_msg = (
            "🚀 TEST MESSAGE — TWILIO SETUP SUCCESSFUL!\n\n"
            f"Aapka 90-Day Roadmap active hai!\n"
            f"Week {info['week']}: {info['week_focus']}\n"
            f"Role: {info['role']}\n"
            f"Day {info['abs_day']} chal raha hai.\n\n"
            "Notifications set ho gayi hain. ✅\n"
            "Har notification time par WhatsApp aayega!"
        )
    else:
        test_msg = (
            "🚀 TEST MESSAGE — TWILIO SETUP SUCCESSFUL!\n\n"
            "Notification system ready hai!\n"
            f"Roadmap {ROADMAP_START.strftime('%d %B %Y')} se shuru hoga.\n\n"
            "Tab tak practice notifications daily aayengi!"
        )
    send_whatsapp(test_msg)


def setup_daily_schedule():
    """Register all daily notification jobs."""
    for time_str, label, template in DAILY_SCHEDULE:
        # We use a lambda with default args to capture values
        def make_job(lbl=label, tmpl=template):
            def job():
                build_and_send(lbl, tmpl)
            return job

        schedule.every().day.at(time_str).do(make_job())
        print(f"  ✅ Scheduled: {time_str} → {label}")

    # Weekly milestone reminder (Sunday at 09:30)
    def sunday_milestone():
        info = get_current_roadmap_info()
        if not info:
            return
        if datetime.date.today().weekday() == 6:  # Sunday
            msg = (
                f"🏆 WEEK {info['week']} MILESTONE\n\n"
                f"Is hafte ka milestone:\n"
                f"📌 {info['milestone']}\n\n"
                f"Complete karo aur GitHub par push karo!\n"
                f"Evidence banana zaroori hai. Proof = confidence."
            )
            build_and_send("🏆 WEEKLY MILESTONE", msg)

    schedule.every().sunday.at("09:30").do(sunday_milestone)
    print("  ✅ Scheduled: Sunday 09:30 → Weekly Milestone")


# ─────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Add CLI Argument Handling
    parser = argparse.ArgumentParser(description="WhatsApp Roadmap & Manual Messenger")
    parser.add_argument("--msg", help="Ek manual message bhejne ke liye")
    args = parser.parse_args()

    # If --msg is provided, just send and exit
    if args.msg:
        print(f"\n📨 Sending manual message: {args.msg}")
        send_whatsapp(args.msg)
        sys.exit(0)

    print("\n" + "="*55)
    print("  90-DAY ROADMAP — WHATSAPP NOTIFICATION SYSTEM")
    print("="*55)

    # Validate config
    if "YOUR_ACCOUNT_SID" in TWILIO_ACCOUNT_SID:
        print("\n❌ ERROR: Pehle CONFIG mein apna Account SID daalo!")
        print("   File mein TWILIO_ACCOUNT_SID update karo.")
        print("\n   Setup guide ke liye SETUP_GUIDE.md padhein.\n")
        exit(1)

    if "92XXXXXXXXX" in YOUR_NUMBER:
        print("\n❌ ERROR: YOUR_NUMBER mein apna WhatsApp number daalo!")
        print("   Example: whatsapp:+923001234567\n")
        exit(1)

    print("\n📋 Roadmap Info:")
    info = get_current_roadmap_info()
    if info:
        print(f"   Week  : {info['week']} — {info['week_focus']}")
        print(f"   Day   : {info['abs_day']} (Day Index: {info['day_idx']})")
        print(f"   Role  : {info['role']}")
    else:
        print(f"   Roadmap {ROADMAP_START} se shuru hoga.")

    print("\n📨 Ek test message bhejte hain...")
    send_test_message()

    print("\n⏰ Daily schedule set ho rahi hai:")
    setup_daily_schedule()

    print("\n✅ System chalu hai. Har notification time par WhatsApp aayega.")
    print("   Is window ko BAND mat karna — system background mein chale ga.")
    print("   Band karne ke liye: Ctrl+C\n")
    print("="*55 + "\n")

    # Run the scheduler loop
    while True:
        schedule.run_pending()
        time.sleep(30)  # Check every 30 seconds
