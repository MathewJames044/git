# 📱 Twilio WhatsApp Notification — Complete Setup Guide

## Step 1: Twilio Account Banao (Free)

1. Browser mein jao: **https://www.twilio.com/try-twilio**
2. Sign up karo (email, password)
3. Email verify karo
4. Phone number verify karo (OTP aayega)
5. "What are you building?" → Select **WhatsApp**, then continue

---

## Step 2: Account SID aur Auth Token Copy Karo

1. Login ke baad **Console Dashboard** khulega
2. Wahan ye dono cheezein dikhegi:
   - **Account SID** → `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - **Auth Token** → Click the eye icon to reveal
3. Dono copy karo — file mein daalne hain

---

## Step 3: WhatsApp Sandbox Join Karo

> ⚠️ Yeh **zaroor** karna hai — nahi to messages nahi aayenge!

1. Twilio Console mein left sidebar → **Messaging** → **Try it out** → **Send a WhatsApp message**
2. Screen par ek number aayega jaise: `+1 415 523 8886`
3. Aur ek code aayega jaise: `join happy-elephant`
4. **Apne phone se WhatsApp kholo**
5. Is number ko apni contacts mein save karo: `+14155238886`
6. Isi number ko WhatsApp message karo: `join happy-elephant`
   (jo bhi code screen par likha ho)
7. Reply aayega: **"You have joined..."** — sandbox ready!

---

## Step 4: whatsapp_notifier.py Mein Config Bharo

File open karo: `whatsapp_notifier.py`

Ye 4 cheezein update karo (file ki top mein hain):

```python
TWILIO_ACCOUNT_SID   = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"   # ← apna SID
TWILIO_AUTH_TOKEN    = "your_auth_token_here"                 # ← apna token
TWILIO_FROM          = "whatsapp:+14155238886"                # ← yeh mat badlo
YOUR_NUMBER          = "whatsapp:+923001234567"               # ← apna number

ROADMAP_START        = datetime.date(2026, 3, 2)              # ← apna start date
```

---

## Step 5: Libraries Install Karo

PowerShell ya CMD mein yeh run karo:

```
pip install twilio schedule
```

---

## Step 6: Script Chalaao

```
cd C:\Users\Hp\OneDrive\Desktop\Roadmap
python whatsapp_notifier.py
```

Agar sab kuch sahi hai to:
- ✅ Test message aayega WhatsApp par
- ✅ Console mein sab scheduled times dikhenge
- ✅ Window khuli rakhni hai background mein

---

## Daily Notifications Schedule

| Time       | Notification                         |
|------------|--------------------------------------|
| 07:00 AM   | 🌅 Wake Up + Aaj ka focus           |
| 07:30 AM   | 🌱 Planning Time + Backend task     |
| 08:00 AM   | 🎧 Audio Learning (Commute)         |
| 09:00 AM   | 💻 Deep Work Start                  |
| 12:30 PM   | 🌿 Lunch Break                      |
| 04:00 PM   | 🔥 Backend Deep Session             |
| 06:30 PM   | ☕ Chai Break                        |
| 08:00 PM   | 🌿 Dinner + Family                  |
| 09:00 PM   | 🧱 Mini Project Time                |
| 10:30 PM   | 🌟 Reflection + Plan Tomorrow       |
| 11:00 PM   | 📚 Wind Down                        |
| 11:30 PM   | 🛌 Sleep Now                        |
| Sunday 9:30| 🏆 Weekly Milestone Reminder        |

---

## Common Problems

**❌ "Message not delivered"**
→ WhatsApp Sandbox join nahi kiya. Step 3 dobara karo.

**❌ "Authentication Error"**
→ Account SID ya Auth Token galat hai. Copy-paste check karo.

**❌ Messages aana band ho gaye**
→ Twilio Sandbox 72 hours mein expire hota hai.
→ Dobara `join happy-elephant` bhejo.

**❌ Script band ho gayi**
→ Window band ho gayi hogi. Dobara `python whatsapp_notifier.py` run karo.
→ Permanently chalne ke liye: Windows pe Task Scheduler use karo (neeche dekho)

---

## Background Mein Automatic Chalaana (Windows)

Agar har din manually script na chalaani ho:

1. **Task Scheduler** search karo Windows mein
2. **Create Basic Task** click karo
3. Name: `Roadmap Notifier`
4. Trigger: `Daily` → Start time: `6:55 AM`
5. Action: `Start a Program`
6. Program: `python`
7. Arguments: `C:\Users\Hp\OneDrive\Desktop\Roadmap\whatsapp_notifier.py`
8. Finish!

Ab script automatically shuru hogi aur notifications aayengi.
