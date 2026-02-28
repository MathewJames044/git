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

## Method 2: Professional Live Hosting (Railway.app) 🌍
*Fayda: Aap duniya mein kahin se bhi dekh sakte hain. Railway fast aur easy hai.*

### Step 1: Account Setup
1. [Railway.app](https://railway.app) par jayein aur GitHub se login karein.
2. **"New Project"** par click karein.
3. **"Deploy from GitHub repo"** select karein aur apni repo `MathewJames044/git` ko choose karein.

### Step 2: Configuration
1. Railway automatically aapki `Procfile` detect kar lega.
2. **"Variables"** tab mein jayein aur ye 2 critical keys add karein (aapki `.env` file se):
   - `VAPID_PUBLIC_KEY`
   - `VAPID_PRIVATE_KEY`

### Step 3: Domain Setup
1. **"Settings"** tab mein jayein.
2. **"Public Networking"** section mein "Generate Domain" par click karein.
3. Railway aapko ek link dega (e.g., `git-production-xxxx.up.railway.app`).

### Step 4: Done!
Ye link ab aap apne mobile browser mein open kar sakte hain. Aapka backend logic, timeline, aur tracker sab live kaam karega!

---

### 💡 Pro Tip
Agar aap chahte hain ke notifications bhi mobile par ayen, to hamesha Railway ka **HTTPS** link use karein. Chrome aur Safari sirf secure sites par hi notifications toggle karne dete hain.

*Bhai, Railway par deploy karte waqt agar passphrase ya build error aye to batana!*
