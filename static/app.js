const publicKey = '/vapid-public-key';

async function registerServiceWorker() {
    if ('serviceWorker' in navigator) {
        const registration = await navigator.serviceWorker.register('/sw.js');
        console.log('Service Worker registered');
        return registration;
    }
    throw new Error('No Service Worker support');
}

async function subscribeToPush() {
    const registration = await navigator.serviceWorker.ready;

    // Get public key from server
    const response = await fetch('/vapid-public-key');
    const { publicKey } = await response.json();

    const subscription = await registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: urlBase64ToUint8Array(publicKey)
    });

    await fetch('/subscribe', {
        method: 'POST',
        body: json.stringify(subscription),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    alert('Notifications Enabled! ✅');
}

function urlBase64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
        .replace(/\-/g, '+')
        .replace(/_/g, '/');

    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);

    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
}

// UI Handling
async function loadData() {
    try {
        const res = await fetch('/api/today');
        const data = await res.json();

        if (data) {
            document.getElementById('week-focus').innerText = `Week ${data.week}: ${data.week_focus}`;
            document.getElementById('role').innerText = data.role;
            document.getElementById('backend-task').innerText = data.backend_task;

            const progress = (data.abs_day / 90) * 100;
            document.getElementById('progress').style.width = `${progress}%`;
            document.getElementById('days-remaining').innerText = `${data.abs_day} / 90 Days Completed`;
        }
    } catch (e) {
        console.error("Failed to load roadmap data", e);
    }
}

document.getElementById('current-date').innerText = new Date().toLocaleDateString('en-PK', {
    weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
});

document.getElementById('subscribe-btn').onclick = subscribeToPush;
document.getElementById('test-btn').onclick = () => fetch('/api/test-push');

window.onload = () => {
    registerServiceWorker();
    loadData();
};

// Install app prompt
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    document.getElementById('install-banner').style.display = 'flex';
});

document.getElementById('install-btn').onclick = async () => {
    if (deferredPrompt) {
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        if (outcome === 'accepted') {
            document.getElementById('install-banner').style.display = 'none';
        }
    }
};
