import datetime

# ─────────────────────────────────────────────────────────────────────────────
# ROADMAP CONSTANTS
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

# Daily schedule: (send_time_24h, label, message_template)
DAILY_SCHEDULE = [
    ("07:00", "🌅 WAKE UP", "Subah ki shuru'aat!\nAaj ka focus: {week_focus}\nRole: {role}\nDay {abs_day} | Week {week}"),
    ("07:30", "🌱 PLANNING TIME", "Breakfast karo + din plan karo.\nAaj ka backend task: {backend_task}"),
    ("08:00", "🎧 AUDIO LEARNING", "Topic: {week_focus}\nEarphones lagao. Chal do."),
    ("09:00", "💻 DEEP WORK START", "⚡ AB KAAM SHURU!\nAaj ka task: {backend_task}"),
    ("12:30", "🌿 LUNCH BREAK", "Khaana khao + 10 min chhalna.\nBackend task: {backend_task}"),
    ("16:00", "🔥 BACKEND DEEP SESSION", "Evening session — yeh sabse important hai!\nAaj ka task: {backend_task}"),
    ("18:30", "☕ CHAI BREAK", "Chai pi lo. 15-20 min relax karo.\nKuch naya seekha? Koi issue?"),
    ("20:00", "🌿 DINNER + FAMILY", "Khaana + family time.\nPoori tarah offline."),
    ("21:00", "🧱 MINI PROJECT TIME", "Week {week} Mini Project: {backend_task}"),
    ("22:30", "🌟 REFLECTION", "Aaj ka din khatam — score karo.\nWeek {week} Milestone: {milestone}"),
    ("23:00", "📚 WIND DOWN", "Screen se hato. 30 min.\nEk article ya kitaab padhna."),
    ("23:30", "🛌 SLEEP NOW", "SONA AB MANDATORY HAI.\nGood night. Week {week} — {role} 🌙"),
]

# ─────────────────────────────────────────────────────────────────────────────
# LOGIC
# ─────────────────────────────────────────────────────────────────────────────

def get_phase(week):
    if week <= 3: return 1
    if week <= 6: return 2
    if week <= 9: return 3
    return 4

def get_current_roadmap_info(start_date):
    """Calculate current week, day_index, abs_day based on ROADMAP_START."""
    today = datetime.date.today()
    delta = (today - start_date).days
    
    if delta < 0:
        return None  # Hasn't started
    if delta >= 91:
        return None  # Completed

    week = (delta // 7) + 1
    day_idx = delta % 7
    abs_day = delta + 1

    if week > 13: week = 13

    return {
        "week": week,
        "day_idx": day_idx,
        "abs_day": abs_day,
        "week_focus": WEEK_FOCUS[week],
        "role": WEEK_ROLE[week],
        "backend_task": BACKEND_TASKS[week][min(day_idx, 6)],
        "milestone": WEEK_MILESTONE[week],
    }
