# 🚀 90-Day Roadmap PWA

A premium, mobile-first Progress Web Application designed to track a 90-day backend engineering journey. Features dynamic task-specific notifications, a synchronized "NOW/NEXT/DONE" timeline, and local progress tracking tailored for the Asia/Karachi (PKT) timezone.

## ✨ Features

- **Dynamic Timeline**: Real-time tracking of daily tasks with "NOW" indicator and "DONE" state persistence.
- **Smart Notifications**: Context-aware WebPush notifications that alert you to the *exact* task starting at its scheduled time.
- **PWA Ready**: Installable on iOS/Android/Desktop for a native-app feel with offline support.
- **Progress Analytics**: Intelligent scoring system that calculates overall roadmap completion based on daily task impact.
- **Premium Aesthetics**: High-end mobile-first UI with fluid typography and a "Glassmorphism" design system.

## 🏗️ Architecture

The project follows a clean, modular structure:

```text
├── backend/            # FastAPI Server & Business Logic
│   ├── main.py         # Entry point & API routes
│   └── roadmap_data.py # Schedule & Data constants
├── static/             # PWA Frontend
│   ├── js/             # Application logic & Service Workers
│   ├── css/            # Premium Styled components
│   └── icons/          # PWA Assets
├── .gitignore          # Production-ready file exclusions
└── Procfile            # Deployment configuration (e.g., Heroku)
```

## 🛠️ Local Setup

### 1. Prerequisites
- Python 3.8+
- Modern Browser (Chrome/Edge/Safari)

### 2. Installation
1. Clone the repository: `git clone <repo-url>`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure Environment (`.env`):
   ```text
   VAPID_PUBLIC_KEY=your_key
   VAPID_PRIVATE_KEY=your_key
   ```

### 3. Run Development Server
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8080 --reload
```

## 📅 Schedule Logic
All tasks are synchronized to the **Asia/Karachi (PKT)** timezone by default to ensure perfect accuracy for local users.

---
*Maintained by MathewJames044 - Engineering Excellence*