// ---------- LOGIN ----------

function login() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;

    if (user === "nazeem" && pass === "nazeem123!") {
        window.location.href = "/dashboard";
    } else {
        alert("Invalid username or password");
    }
}

// ---------- LOGOUT ----------

function logout() {
    window.location.href = "/";
}

// ---------- CONFETTI ON DASHBOARD ----------

if (window.location.pathname.includes("dashboard")) {

    setTimeout(() => {
        if (typeof confetti === "function") {
            confetti({
                particleCount: 150,
                spread: 100,
                origin: { y: 0.6 }
            });
        }
    }, 500);
}

// ---------- AI CHAT ----------

async function sendMessage() {

    const input = document.getElementById("chatInput");
    const message = input.value.trim();

    if (!message) return;

    const chatBox = document.getElementById("chatBox");

    // Show user message
    chatBox.innerHTML += `<div class="user-msg">${message}</div>`;
    input.value = "";

    // Show typing...
    const typingId = "typing-" + Date.now();
    chatBox.innerHTML += `<div id="${typingId}" class="bot-msg typing">AI is typing...</div>`;

    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        // Remove typing
        document.getElementById(typingId).remove();

        // ✅ UPDATED (line break + bold headings support)
        chatBox.innerHTML += `<div class="bot-msg">${
            data.reply
                .replace(/\n/g, "<br>")
                .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        }</div>`;

    } catch (error) {

        document.getElementById(typingId).remove();

        chatBox.innerHTML += `<div class="bot-msg">⚠️ Server error</div>`;
    }

    // Auto scroll
    chatBox.scrollTop = chatBox.scrollHeight;
}

// ---------- ENTER KEY SUPPORT (✅ FIXED) ----------

const chatInputElement = document.getElementById("chatInput");

if (chatInputElement) {
    chatInputElement.addEventListener("keypress", function(e) {
        if (e.key === "Enter") {
            sendMessage();
        }
    });
}

// ---------- TIME + GREETING ----------

function updateTime() {
    const now = new Date();

    let hours = now.getHours();
    let minutes = now.getMinutes();
    let ampm = hours >= 12 ? 'PM' : 'AM';

    hours = hours % 12 || 12;
    minutes = minutes < 10 ? '0' + minutes : minutes;

    const timeEl = document.getElementById("time");
    const greetEl = document.getElementById("greeting");

    if (timeEl) {
        timeEl.innerText = `${hours}:${minutes} ${ampm}`;
    }

    let greeting = "Good Morning";

    if (now.getHours() >= 12 && now.getHours() < 17) {
        greeting = "Good Afternoon";
    } else if (now.getHours() >= 17) {
        greeting = "Good Evening";
    }

    if (greetEl) {
        greetEl.innerText = greeting;
    }
}

setInterval(updateTime, 1000);
updateTime();

// ---------- CHART ----------

const ctx = document.getElementById('myChart');

if (ctx) {
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
            datasets: [{
                label: 'Hours',
                data: [2, 3, 1, 4, 2],
                borderWidth: 1
            }]
        }
    });
}