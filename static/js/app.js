// ─── Service Worker ──────────────────────────────────────────────────────────
async function registerServiceWorker() {
    if (!('serviceWorker' in navigator)) return null;
    return await navigator.serviceWorker.register('/sw.js');
}

function urlBase64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');
    const rawData = window.atob(base64);
    const out = new Uint8Array(rawData.length);
    for (let i = 0; i < rawData.length; ++i) out[i] = rawData.charCodeAt(i);
    return out;
}

// ─── Subscribe ────────────────────────────────────────────────────────────────
async function subscribeToPush() {
    try {
        const reg = await navigator.serviceWorker.ready;
        const { publicKey } = await (await fetch('/vapid-public-key')).json();
        const perm = await Notification.requestPermission();
        if (perm !== 'granted') { alert('❌ Permission denied.'); return; }
        const sub = await reg.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: urlBase64ToUint8Array(publicKey)
        });
        const res = await fetch('/subscribe', {
            method: 'POST',
            body: JSON.stringify(sub.toJSON()),
            headers: { 'Content-Type': 'application/json' }
        });
        if (res.ok) {
            document.getElementById('subscribe-btn').innerHTML = '✅ Enabled';
            document.getElementById('subscribe-btn').disabled = true;
            alert('✅ Notifications enabled! Roadmap reminders set.');
        }
    } catch (err) { alert('❌ Error: ' + err.message); }
}

async function testPush() {
    const res = await fetch('/api/test-push');
    const data = await res.json();
    alert(data.status === 'success' ? '✅ Test push sent!' : '⚠️ ' + (data.message || 'Enable notifications first.'));
}

// ─── Time Helpers ─────────────────────────────────────────────────────────────
const CAT_ICON = {
    backend: '💻', uni: '🎓', office: '💼', travel: '🎧',
    recovery: '🌿', sleep: '🛌', reflect: '🌟', planning: '🗓',
    wind_down: '📚', milestone: '🏆', break: '☕'
};

function timeToMinutes(timeStr) {
    if (!timeStr || timeStr.includes('🏆')) return -1;
    // Handle "07:00–07:30 AM" or "11:30 PM–..."
    const parts = timeStr.split(/[–-]/);
    const startPart = parts[0].trim();
    const m = startPart.match(/(\d+):(\d+)/);
    if (!m) return -1;

    let h = parseInt(m[1]);
    const min = parseInt(m[2]);

    // Detect AM/PM: look in start part first, then end part
    let ampm = 'AM';
    const startAMPM = startPart.match(/(AM|PM)/i);
    if (startAMPM) {
        ampm = startAMPM[0].toUpperCase();
    } else {
        const fullAMPM = timeStr.match(/(AM|PM)/i);
        if (fullAMPM) ampm = fullAMPM[0].toUpperCase();
    }

    if (ampm === 'PM' && h !== 12) h += 12;
    if (ampm === 'AM' && h === 12) h = 0;
    return h * 60 + min;
}

function nowMinutes() {
    // Force time to Asia/Karachi for the 'NOW' indicator
    const n = new Date(new Date().toLocaleString("en-US", { timeZone: "Asia/Karachi" }));
    return n.getHours() * 60 + n.getMinutes();
}

// ─── Render Schedule Timeline ─────────────────────────────────────────────────
function renderSchedule(slots, data, doneIndices = []) {
    const list = document.getElementById('schedule-list');
    if (!slots || !slots.length) {
        list.innerHTML = '<p class="loading-text">No schedule for today.</p>';
        return;
    }

    const now = nowMinutes();

    // Classify each slot
    const classified = slots.map((slot, i) => {
        const start = timeToMinutes(slot.time);
        const nextStart = i + 1 < slots.length ? timeToMinutes(slots[i + 1].time) : 1440;
        const isActuallyDone = doneIndices.includes(i);

        let state = 'upcoming';
        if (isActuallyDone) {
            state = 'done';
        } else if (start !== -1) {
            if (start <= now && now < nextStart) state = 'now';
            else if (start < now) state = 'past';
        }
        return { ...slot, state, idx: i, isActuallyDone };
    });

    // Find now/next
    const nowSlot = classified.find(s => s.state === 'now');
    const nextSlot = classified.find(s => s.state === 'upcoming');

    // Populate Now card
    if (nowSlot) {
        document.getElementById('now-time').innerText = nowSlot.time;
        document.getElementById('now-topic').innerText = nowSlot.topic;
        document.getElementById('now-task').innerText = nowSlot.task;
    } else {
        document.getElementById('now-topic').innerText = 'All done for today! 🎉';
        document.getElementById('now-task').innerText = '';
    }

    // Populate Next card
    if (nextSlot) {
        document.getElementById('next-time').innerText = nextSlot.time;
        document.getElementById('next-topic').innerText = nextSlot.topic;
        document.getElementById('next-task').innerText = nextSlot.task;
    } else {
        document.getElementById('next-topic').innerText = 'No more tasks today';
        document.getElementById('next-task').innerText = '';
    }

    // Day Impact — find the most important backend slot
    const backendSlot = slots.find(s => s.category === 'backend');
    document.getElementById('impact-task').innerText = backendSlot ? backendSlot.task : (data.backend_task || '—');
    document.getElementById('impact-milestone').innerText = '🏆 Week Goal: ' + (data.milestone || '—');

    // Render all slots
    list.innerHTML = classified.map(slot => {
        const icon = CAT_ICON[slot.category] || '📌';
        const badge = slot.state === 'now'
            ? '<span class="now-badge">NOW</span>'
            : slot.state === 'done'
                ? '<span class="done-badge">DONE</span>'
                : slot.state === 'upcoming' && slot.idx === classified.find(s => s.state === 'upcoming')?.idx
                    ? '<span class="next-badge">NEXT</span>'
                    : '';

        const motiv = slot.motivation ? `<div class="slot-motivation">"${slot.motivation}"</div>` : '';
        const isPastOrDone = slot.state === 'past' || slot.state === 'done';

        return `
        <div class="slot cat-${slot.category} ${slot.state === 'now' ? 'slot-now' : ''} ${isPastOrDone ? 'past' : ''}">
            <div class="slot-time">${icon} ${slot.time}${badge}</div>
            <div class="slot-topic">${slot.topic}</div>
            <div class="slot-task">${slot.task}</div>
            ${motiv}
            <span class="slot-role">${slot.role}</span>
        </div>`;
    }).join('');

    // Auto-scroll to current slot
    setTimeout(() => {
        const nowEl = list.querySelector('.slot-now');
        if (nowEl) nowEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 300);
}

// ─── Load All Data ────────────────────────────────────────────────────────────
async function loadData() {
    try {
        const [roadmapRes, statsRes] = await Promise.all([
            fetch('/api/today'),
            fetch('/api/stats')
        ]);
        const [data, stats] = await Promise.all([roadmapRes.json(), statsRes.json()]);

        if (!data || !data.week) {
            document.getElementById('week-focus').innerText = 'Roadmap not started yet!';
            return;
        }

        // Header
        document.getElementById('header-day').innerText = data.abs_day;

        // Week card
        document.getElementById('week-focus').innerText = `Week ${data.week}: ${data.week_focus}`;
        document.getElementById('role').innerText = data.role;
        document.getElementById('stat-week').innerText = `W${data.week}`;
        document.getElementById('stat-day').innerText = `D${data.abs_day}`;
        document.getElementById('stat-dayname').innerText = data.day_name;
        document.getElementById('phase-tag').innerText = `PHASE ${data.phase}`;

        // ── MAIN PROGRESS BAR — based on actual task completions ──
        const overallPct = stats.overall_pct ?? 0;
        const todayPct = stats.today_pct ?? 0;
        const totalDone = stats.total_completed ?? 0;
        const totalPoss = stats.total_possible ?? 0;
        const todayDone = stats.today_completed ?? 0;
        const todayTotal = stats.today_total ?? 14;

        document.getElementById('progress').style.width = overallPct + '%';
        document.getElementById('progress-pct').innerText = overallPct + '%';
        document.getElementById('progress-label-left').innerText = '✅ Overall Completion';
        document.getElementById('progress-label-right').innerText = `${totalDone}/${totalPoss} tasks`;

        // Today sub-bar
        document.getElementById('today-progress').style.width = todayPct + '%';
        document.getElementById('today-pct-text').innerText = `Today: ${todayDone}/${todayTotal} tasks (${todayPct}%)`;
        document.getElementById('today-progress-bar').style.display = 'block';

        // Focus card
        document.getElementById('backend-task').innerText = data.backend_task;
        document.getElementById('milestone').innerText = data.milestone;
        document.getElementById('audio-topic').innerText = data.audio_topic || '';

        // Render timeline
        renderSchedule(data.schedule, data, stats.today_completed_indices || []);

    } catch (e) {
        console.error(e);
        document.getElementById('week-focus').innerText = '⚠️ Server not reachable.';
    }
}

// ─── Init ─────────────────────────────────────────────────────────────────────
document.getElementById('current-date').innerText = new Date().toLocaleDateString('en-PK', {
    weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
});
document.getElementById('subscribe-btn').onclick = subscribeToPush;
document.getElementById('test-btn').onclick = testPush;

window.onload = () => { registerServiceWorker(); loadData(); };
setInterval(loadData, 60000); // Auto-refresh every minute

// ─── Install Prompt ───────────────────────────────────────────────────────────
let deferredPrompt;
window.addEventListener('beforeinstallprompt', e => {
    e.preventDefault();
    deferredPrompt = e;
    document.getElementById('install-banner').style.display = 'flex';
});
document.getElementById('install-btn').onclick = () => {
    if (deferredPrompt) { deferredPrompt.prompt(); deferredPrompt.userChoice.then(() => document.getElementById('install-banner').style.display = 'none'); }
};
