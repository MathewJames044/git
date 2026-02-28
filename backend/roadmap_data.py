import datetime

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

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

AUDIO_TOPICS = {
    1: "Node.js fundamentals: event loop, async, modules",
    2: "Express.js: routing, middleware, MVC basics",
    3: "Databases: SQL, PostgreSQL, ORMs explained",
    4: "JWT, OAuth, security in web APIs",
    5: "Software architecture: MVC, Clean Code, SOLID",
    6: "Production backend: logging, error handling, monitoring",
    7: "Docker and containerization for developers",
    8: "CI/CD, DevOps basics, GitHub Actions",
    9: "Redis, queues, async background jobs",
    10: "Caching strategies and performance optimization",
    11: "SRE, monitoring, reliability engineering basics",
    12: "System design for backend engineers",
    13: "Backend career growth and learning strategy",
}

# Notification schedule (time, label, template)
DAILY_SCHEDULE = [
    ("07:00", "🌅 WAKE UP", "Subah ki shuru'aat!\nAaj ka focus: {week_focus}\nRole: {role}\nDay {abs_day} | Week {week}"),
    ("07:30", "🌱 PLANNING TIME", "Breakfast karo + din plan karo.\nAaj ka backend task: {backend_task}"),
    ("08:00", "🎧 AUDIO LEARNING", "Topic: {week_focus}\nEarphones lagao. Chal do."),
    ("09:00", "💻 DEEP WORK START", "⚡ AB KAAM SHURU!\nAaj ka task: {backend_task}"),
    ("12:30", "🌿 LUNCH BREAK", "Khaana khao + 10 min chhalna.\nBackend task: {backend_task}"),
    ("16:00", "🔥 BACKEND DEEP SESSION", "Evening session!\nAaj ka task: {backend_task}"),
    ("18:30", "☕ CHAI BREAK", "Chai pi lo. 15-20 min relax karo."),
    ("20:00", "🌿 DINNER + FAMILY", "Khaana + family time. Poori tarah offline."),
    ("21:00", "🧱 MINI PROJECT TIME", "Week {week} Mini Project: {backend_task}"),
    ("22:30", "🌟 REFLECTION", "Aaj ka din khatam.\nWeek {week} Milestone: {milestone}"),
    ("23:00", "📚 WIND DOWN", "Screen se hato. 30 min.\nEk article ya kitaab padhna."),
    ("23:30", "🛌 SLEEP NOW", "SONA AB MANDATORY HAI.\nGood night. {role} 🌙"),
]

# ─────────────────────────────────────────────────────────────────────────────
# PER-DAY DETAILED SCHEDULE (matches Excel sheet structure)
# ─────────────────────────────────────────────────────────────────────────────

def get_day_name(day_idx):
    return ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][day_idx]

def get_phase(week):
    if week <= 3: return 1
    if week <= 6: return 2
    if week <= 9: return 3
    return 4

def build_detailed_day_schedule(week, day_idx):
    """Returns a list of time-slot dicts for a specific week day."""
    dname    = get_day_name(day_idx)
    wf       = WEEK_FOCUS[week]
    wr       = WEEK_ROLE[week]
    bt       = BACKEND_TASKS[week][min(day_idx, 6)]
    at       = AUDIO_TOPICS[week]
    wm       = WEEK_MILESTONE[week]

    slots = []

    def s(time, topic, task, role, cat, motivation=""):
        slots.append({
            "time": time, "topic": topic, "task": task,
            "role": role, "category": cat, "motivation": motivation
        })

    # ── SUNDAY ────────────────────────────────────────
    if dname == "Sunday":
        s("07:30 AM–08:00 AM", "Wake Up + Light Breakfast", "Hydrate, light stretch, disconnect from work", "🌅 Rest Architect", "recovery", "Rest is productive.")
        s("08:00 AM–09:00 AM", "Morning Walk", "30–40 min walk. No phone. Just breathe.", "🌿 Energy Guardian", "recovery", "Your mind wants silence.")
        s("09:00 AM–10:30 AM", "Weekly Review", f"Review Week {week}: what worked, what to improve", "🧭 Weekly Strategist", "reflect", "Measure to improve.")
        s("10:30 AM–12:30 PM", "Light University Revision", "Review 1 subject lightly. No deep study today.", "📖 Academic Keeper", "uni", "Keep it light on Sunday.")
        s("12:30 PM–01:30 PM", "Lunch + Family Time", "Eat + family time. Full offline.", "🌿 Balanced Achiever", "recovery")
        s("01:30 PM–03:00 PM", f"Backend Concept Recap — {wf}", f"Re-read key notes from Week {week} backend study.", "💡 Knowledge Consolidator", "backend", "Let learning consolidate.")
        s("03:00 PM–04:30 PM", "Next Week Planning", f"Plan Week {min(week+1,13)} backend + university tasks", "🗓 Weekly Planner", "reflect", "Planning = stress-free week.")
        s("04:30 PM–06:00 PM", "Hobbies / Rest", "Free time only. No tech pressure.", "🎮 Human Being", "recovery")
        s("06:00 PM–07:30 PM", "Dinner + Relax", "Family + food. Full disconnect.", "🌿 Balanced Achiever", "recovery")
        s("07:30 PM–09:00 PM", "Light Tech Reading", "1 article or short YouTube video max.", "📚 Mind Explorer", "wind_down", "Feed the brain gently.")
        s("09:00 PM–10:00 PM", "Prepare for Monday", "Set VSCode ready, check assignments, plan Monday", "🗓 Monday Architect", "reflect", "Prepare the battlefield the night before.")
        s("10:00 PM–10:30 PM", "Wind Down", "Calm music, no screens 30 min before sleep", "🌙 Night Scholar", "wind_down")
        s("10:30 PM–07:00 AM", "Sleep — 8 Hours", "Full cognitive reset. Non-negotiable.", "🛌 Energy Guardian", "sleep")
        # Week milestone on day 7
        slots.append({"time": "🏆 WEEK MILESTONE", "topic": f"Week {week} Milestone", "task": wm, "role": wr, "category": "milestone", "motivation": "Complete and push: evidence the system works."})
        return slots

    # ── COMMON WEEKDAY START ───────────────────────────
    s("07:00 AM–07:30 AM", "Wake Up + Morning Routine", "Freshen up, stretch, hydrate. No phone for 15 min.", "⏰ Morning Starter", "recovery", "Your morning routine is your performance foundation.")
    s("07:30 AM–08:00 AM", "Breakfast + Daily Planning", f"Top 3 tasks of the day. Week {week}: {wf}", "🌱 Initiator", "planning", "Every master starts with a clear plan.")
    s("08:00 AM–08:45 AM", "Travel (Home → Office/University)", f"🎧 Audio: {at}", "🎧 Knowledge Commuter", "travel", "Waste no commute time.")

    # ── MONDAY ────────────────────────────────────────
    if dname == "Monday":
        s("09:00 AM–12:30 PM", "Office Work — Deep Focus", "Deep focus: 1 major task + general office work", "💼 Office Strategist", "office", "Make your office hours count.")
        s("12:30 PM–01:00 PM", "Lunch / Recharge", "Eat + short walk before uni commute", "🌿 Energy Keeper", "recovery")
        s("01:00 PM–01:30 PM", "Travel Office → University", f"🎧 Audio: {at}", "🎧 Road Scholar", "travel")
        s("01:30 PM–03:00 PM", "University — Theory of Automata (TOA)", "Active note-taking, follow examples, ask questions", "🎓 Student Coder", "uni", "Automata is the math foundation of all computing.")
        s("03:00 PM–03:45 PM", "Travel University → Home", "Audio recap — reinforce TOA concepts", "🎧 Road Scholar", "travel")
        s("03:45 PM–04:00 PM", "Micro Break", "Stretch, hydrate, decompress", "🧘 Micro Reset", "recovery")
        s("04:00 PM–06:00 PM", f"Backend — {wf}", bt, wr, "backend", "This 2-hour session is the engine of your 90 days.")
        s("06:00 PM–06:30 PM", "Tea Break", "Refresh, snack", "🌿 Energy Keeper", "break")
        s("06:30 PM–08:00 PM", "University Study — TOA", "Review notes, solve exercises, prep quiz/assignment", "📝 Academic Builder", "uni")
        s("08:00 PM–09:00 PM", "Dinner + Family Time", "Eat, full disconnect from work", "🌿 Balanced Achiever", "recovery")
        s("09:00 PM–10:30 PM", f"Backend Mini Project — Week {week}", bt, "🧱 System Builder", "backend", "Every push to GitHub is proof.")
        s("10:30 PM–11:00 PM", "Reflection + Plan Tuesday", "3 wins today. 1 improvement. Plan tomorrow.", "🌟 Daily Strategist", "reflect")
        s("11:00 PM–11:30 PM", "Wind Down", "Light reading. No screens 30 min before sleep.", "📚 Mind Explorer", "wind_down")
        s("11:30 PM–07:00 AM", "Sleep — 7.5 Hours", "Non-negotiable. Brain consolidates code while you sleep.", "🛌 Energy Guardian", "sleep")

    # ── TUESDAY ───────────────────────────────────────
    elif dname == "Tuesday":
        s("08:45 AM–09:15 AM", "Travel Home → University (SE)", f"🎧 Audio: {at}", "🎧 Knowledge Commuter", "travel")
        s("09:15 AM–10:30 AM", "Office Work — Mini Session", "1 focused backend task or quick office work", "💼 Office Strategist", "office")
        s("10:30 AM–12:00 PM", "University — Software Engineering (SE)", "Active note-taking, participate, summarize", "🎓 Student Coder", "uni", "SE teaches you to build systems, not just features.")
        s("12:00 PM–12:45 PM", "Lunch / Recharge", "Eat + short walk", "🌿 Energy Keeper", "recovery")
        s("12:45 PM–02:30 PM", "Office Work — Deep Focus", "Major deep work session: core office task", "💼 Office Strategist", "office")
        s("02:30 PM–04:00 PM", f"Backend — {wf}", bt, wr, "backend")
        s("04:00 PM–04:45 PM", "Travel Home", f"🎧 Audio recap — reinforce backend concepts", "🎧 Road Scholar", "travel")
        s("04:45 PM–05:00 PM", "Micro Break", "Stretch / hydrate", "🧘 Micro Reset", "recovery")
        s("05:00 PM–06:30 PM", "Cortellect Supervision (No Coding)", "Review team tasks, approve outputs, delegate only", "🏢 Team Lead", "office")
        s("06:30 PM–07:30 PM", "University Study — SE", "Review SE notes, solve exercises", "📝 Academic Builder", "uni")
        s("07:30 PM–08:30 PM", "Dinner + Family Time", "Full offline, family present", "🌿 Balanced Achiever", "recovery")
        s("08:30 PM–10:00 PM", f"Backend Mini Project — Week {week}", bt, "🧱 System Builder", "backend")
        s("10:00 PM–10:30 PM", "Reflection + Plan Wednesday", "3 wins + 1 improvement. Tomorrow is heavy — plan it.", "🌟 Daily Strategist", "reflect")
        s("10:30 PM–11:00 PM", "Wind Down", "Light reading, calm down", "📚 Mind Explorer", "wind_down")
        s("11:00 PM–07:00 AM", "Sleep EARLY — Heavy Day Tomorrow", "Sleep early before heavy Wednesday.", "🛌 Energy Guardian", "sleep")

    # ── WEDNESDAY ─────────────────────────────────────
    elif dname == "Wednesday":
        s("08:00 AM–10:00 AM", f"Morning Deep Work — {wf}", bt, wr, "backend", "Morning coding = top performance.")
        s("10:00 AM–10:30 AM", "Break + Prep for Uni", "Light snack, review PD lecture topic", "🌿 Energy Keeper", "recovery")
        s("10:30 AM–11:15 AM", "Travel Home → University", f"🎧 Audio: {at}", "🎧 Road Scholar", "travel")
        s("11:15 AM–12:00 PM", "Arrive Uni + Canteen Lunch", "Eat before 4.5 hour class block", "🌿 Energy Keeper", "recovery")
        s("12:00 PM–03:00 PM", "University — Personal Development (PD)", "Active notes, reflect on each concept, participate", "🎓 Knowledge Seeker", "uni", "PD is the software upgrade for your mindset.")
        s("03:00 PM–04:30 PM", "University — Information Security (IS)", "Active notes, practice exercises, mini quiz prep", "🔒 Security Explorer", "uni", "IS is the shield every backend engineer must master.")
        s("04:30 PM–05:15 PM", "Travel Uni → Home", "Audio recap: IS + PD concepts", "🎧 Road Scholar", "travel")
        s("05:15 PM–05:30 PM", "Micro Break", "Stretch, hydrate, decompress", "🧘 Micro Reset", "recovery")
        s("05:30 PM–06:30 PM", "Light University Study", "Review PD or IS notes gently — no deep work", "📝 Academic Builder", "uni")
        s("06:30 PM–07:30 PM", "Dinner + Family Time", "Full offline. Brain recovery mode.", "🌿 Balanced Achiever", "recovery")
        s("07:30 PM–08:00 PM", "Plan Thursday + Weekly Check", "Quick 30-min review: backend progress + assignments", "🧭 Weekly Strategist", "reflect")
        s("08:00 PM–08:30 PM", "Wind Down", "Light reading, calm music, dark room", "📚 Mind Explorer", "wind_down")
        s("08:30 PM–07:00 AM", "FULL RECOVERY SLEEP — 10.5 hrs", "Wednesday is the heaviest day. Sleep fully. No exception.", "🛌 Energy Guardian", "sleep", "Heavy days demand complete recovery nights.")

    # ── THURSDAY ──────────────────────────────────────
    elif dname == "Thursday":
        s("08:00 AM–10:00 AM", f"Morning Deep Work — {wf}", bt, wr, "backend")
        s("10:00 AM–10:30 AM", "Break + TOA Prep", "Snack, review TOA notes from Monday", "🌿 Energy Keeper", "recovery")
        s("10:30 AM–12:30 PM", "Office Work — Deep Focus", "Complete 1 major office task or backend module", "💼 Office Strategist", "office")
        s("12:30 PM–01:00 PM", "Lunch / Recharge", "Eat healthy — long afternoon ahead", "🌿 Energy Keeper", "recovery")
        s("01:00 PM–01:30 PM", "Travel Office → University", f"🎧 Audio: {at}", "🎧 Road Scholar", "travel")
        s("01:30 PM–03:00 PM", "University — Theory of Automata (TOA)", "Active notes, solve exercises, ask questions", "🎓 Student Coder", "uni")
        s("03:00 PM–06:00 PM", "University — Operating Systems Lab", "Lab exercises, hands-on practicals, document steps", "🖥 Lab Engineer", "uni", "OS: understand what runs beneath your code.")
        s("06:00 PM–06:45 PM", "Travel Uni → Home", "Decompress — light audio or silence on the way", "🎧 Road Scholar", "travel")
        s("06:45 PM–07:30 PM", "Dinner + Full Rest", "Eat + family time. No screens.", "🌿 Balanced Achiever", "recovery")
        s("07:30 PM–08:30 PM", "University Study — Light", "Review OS Lab notes only — max 1 hour, keep it light", "📝 Academic Builder", "uni")
        s("08:30 PM–09:00 PM", "Plan Friday", "Plan: SE class + backend + Badar revenue task", "🧭 Daily Strategist", "reflect")
        s("09:00 PM–09:30 PM", "Wind Down", "Calm music, no work talk", "📚 Mind Explorer", "wind_down")
        s("09:30 PM–07:00 AM", "FULL RECOVERY SLEEP — 9.5 hrs", "Thursday is heavy. Complete sleep mandatory.", "🛌 Energy Guardian", "sleep")

    # ── FRIDAY ────────────────────────────────────────
    elif dname == "Friday":
        s("08:30 AM–09:15 AM", "Travel Home → University (SE class)", f"🎧 Audio: {at}", "🎧 Knowledge Commuter", "travel")
        s("09:15 AM–10:30 AM", "Office Work — Quick Deep Focus", "1 important office task completed before SE class", "💼 Office Strategist", "office")
        s("10:30 AM–12:00 PM", "University — Software Engineering (SE)", "Active note-taking, project discussion, apply from backend", "🎓 Student Coder", "uni")
        s("12:00 PM–12:45 PM", "Lunch / Recharge", "Eat + short walk", "🌿 Energy Keeper", "recovery")
        s("12:45 PM–02:30 PM", f"Backend Deep Session — {wf}", bt, wr, "backend", "This session matters the most today.")
        s("02:30 PM–04:00 PM", "Office Work — Badar Revenue Task", "Most critical Badar revenue task of the week", "💼 Office Strategist", "office")
        s("04:00 PM–04:45 PM", "Travel Home", "Audio recap", "🎧 Road Scholar", "travel")
        s("04:45 PM–05:00 PM", "Micro Break", "Stretch / hydrate / short walk", "🧘 Micro Reset", "recovery")
        s("05:00 PM–06:00 PM", f"Backend Mini Project — Week {week}", bt, "🧱 System Builder", "backend")
        s("06:00 PM–07:00 PM", "University Study — SE", "SE notes + exercises + upcoming quiz prep", "📝 Academic Builder", "uni")
        s("07:00 PM–08:00 PM", "Dinner + Family Time", "Full offline, family time", "🌿 Balanced Achiever", "recovery")
        s("08:00 PM–09:00 PM", "Cortellect / Badar Weekly Check", "Team review, approve outputs, plan next week delegation", "🏢 CEO Mode", "office")
        s("09:00 PM–09:30 PM", "Reflection + Weekend Plan", f"Review Week {week} progress. Plan Saturday + Sunday.", "🌟 Weekly Planner", "reflect")
        s("09:30 PM–10:00 PM", "Wind Down", "Light reading / calm content", "📚 Mind Explorer", "wind_down")
        s("10:00 PM–07:00 AM", "Sleep — Full 9 Hours", "Recover fully — Saturday is also heavy.", "🛌 Energy Guardian", "sleep")

    # ── SATURDAY ──────────────────────────────────────
    elif dname == "Saturday":
        s("07:00 AM–08:00 AM", "Wake Up + Planning", "Breakfast + review weekend goals. Light start.", "🌱 Initiator", "planning")
        s("08:00 AM–10:00 AM", f"Backend — {wf} (Peak Morning)", bt, wr, "backend", "Weekend focused work = week ahead advantage.")
        s("10:00 AM–10:30 AM", "Break + Uni Prep", "Snack, glance at FA notes briefly", "🌿 Energy Keeper", "recovery")
        s("10:30 AM–11:15 AM", "Travel Home → University (FA+IS)", f"🎧 Audio: {at}", "🎧 Road Scholar", "travel")
        s("11:15 AM–12:00 PM", "Arrive Uni + Canteen Lunch", "Eat before 4.5 hour class block", "🌿 Energy Keeper", "recovery")
        s("12:00 PM–03:00 PM", "University — Financial Accounting (FA)", "Active notes, solve exercises, mini quiz prep", "🎓 Accounting Scholar", "uni", "Every founder must understand numbers.")
        s("03:00 PM–04:30 PM", "University — Information Security (IS)", "Active notes, practice exercises", "🔒 Security Explorer", "uni")
        s("04:30 PM–05:15 PM", "Travel Uni → Home", "Audio recap: IS + FA concepts", "🎧 Road Scholar", "travel")
        s("05:15 PM–05:30 PM", "Micro Break", "Hydrate, decompress", "🧘 Micro Reset", "recovery")
        s("05:30 PM–06:30 PM", "University Study (Light)", "Review FA or IS notes — consolidate gently", "📝 Academic Builder", "uni")
        s("06:30 PM–07:30 PM", "Dinner + Family Time", "Offline completely.", "🌿 Balanced Achiever", "recovery")
        s("07:30 PM–09:00 PM", f"Backend Mini Project — Week {week} (Weekend Push)", bt, "🧱 System Builder", "backend")
        s("09:00 PM–09:30 PM", "Pending Assignments", "Quick catch-up on any pending assignment", "📝 Academic Builder", "uni")
        s("09:30 PM–10:00 PM", "Reflection — Saturday", "Note wins + 1 improvement. Update progress tracker.", "🌟 Daily Strategist", "reflect")
        s("10:00 PM–10:30 PM", "Wind Down", "Light reading, calm music", "📚 Mind Explorer", "wind_down")
        s("10:30 PM–07:30 AM", "FULL RECOVERY SLEEP", "Saturday is heavy. Sleep fully.", "🛌 Energy Guardian", "sleep")

    return slots


# ─────────────────────────────────────────────────────────────────────────────
# CORE LOGIC
# ─────────────────────────────────────────────────────────────────────────────

def get_current_roadmap_info(start_date, today=None):
    if today is None:
        today = datetime.date.today()
    delta = (today - start_date).days

    if delta < 0:
        return None
    if delta >= 91:
        return None

    week    = (delta // 7) + 1
    day_idx = delta % 7
    abs_day = delta + 1

    if week > 13: week = 13

    backend_task = BACKEND_TASKS[week][min(day_idx, 6)]

    return {
        "week":         week,
        "phase":        get_phase(week),
        "day_idx":      day_idx,
        "day_name":     get_day_name(day_idx),
        "abs_day":      abs_day,
        "week_focus":   WEEK_FOCUS[week],
        "role":         WEEK_ROLE[week],
        "backend_task": backend_task,
        "milestone":    WEEK_MILESTONE[week],
        "audio_topic":  AUDIO_TOPICS[week],
        "schedule":     build_detailed_day_schedule(week, day_idx),
    }
