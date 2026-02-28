# 📱 Live Mobile Preview & Deployment Guide

Bhai, aapka project bilkul professional ho gaya hai. Ab isko mobile par live dekhne ke **2 simple tareeqay** hain:

---

## Method 1: Local Preview (Same Wi-Fi) 📶
*Fayda: Instant check, koi setup cost nahi.*

### Step 1: Run Server on PC
Apne VS Code terminal mein ye script chalao (Is se PC ka server mobile ke liye open ho jayega):
```powershell
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8080
```

### Step 2: Access on Mobile
1. Ensure karein ke aapka **Mobile** aur **PC** dono **same Wi-Fi** par hain.
2. Mobile browser (Chrome) open karein aur ye address type karein:
   `http://192.168.101.2:8080`

### Step 3: Install PWA (App look)
Jab page load ho jaye:
- **Android**: Chrome menu (3 dots) par click karein -> "Install App" ya "Add to Home Screen".
- **iOS**: Share button par click karein -> "Add to Home Screen".

---

## Method 2: Professional Live Hosting (Internet Par) 🌍
*Fayda: Aap duniya mein kahin se bhi dekh sakte hain.*

Hum **Render** ya **Railway** use karenge kyunki hamare paas `Procfile` pehle se ready hai.

### Step 1: Account Setup
1. [Render.com](https://render.com) par jayein aur GitHub se login karein.
2. "New +" button par click karein aur **"Web Service"** select karein.

### Step 2: Connect GitHub
1. Apni repo `MathewJames044/git` ko connect karein.
2. Ye settings check karein:
   - **Runtime**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python -m uvicorn backend.main:app --host 0.0.0.0 --port $PORT` (Ye hamare `Procfile` mein pehle se hai).

### Step 3: Add Environment Variables
Render dashboard mein **"Environment"** tab par jayein aur ye 2 cheezain add karein (aapki `.env` file se):
1. `VAPID_PUBLIC_KEY`
2. `VAPID_PRIVATE_KEY`

### Step 4: Done!
Render aapko ek URL dega (e.g., `https://roadmap-abc.onrender.com`). Ye URL aap kisi ko bhi bhej sakte hain aur apne mobile par 24/7 dekh sakte hain.

---

### 💡 Pro Tip
Agar aap chahte hain ke notifications bhi mobile par ayen, to hamesha **HTTPS** (Method 2) use karein, kyunki browsers security ki wajah se notifications sirf secure sites par allow karte hain.

*Bhai, agar live deployment mein koi error aye to batana, main fix kar doon ga!*
