/* =========================
   MEMBUKA UNDANGAN
========================= */
function openInvitation() {
    const opening = document.getElementById("opening");
    if (opening) {
        opening.classList.add("hidden");
    }
}

const weddingDate = new Date("2026-12-20T08:00:00+07:00").getTime();
let countdownInterval;

function updateCountdown() {
    const now = Date.now();
    const distance = weddingDate - now;

    const daysEl = document.getElementById("days");
    const hoursEl = document.getElementById("hours");
    const minutesEl = document.getElementById("minutes");
    const secondsEl = document.getElementById("seconds");
    const messageEl = document.getElementById("countdown-message");

    if (!daysEl || !hoursEl || !minutesEl || !secondsEl || !messageEl) {
        return;
    }

    if (distance <= 0) {
        daysEl.textContent = "00";
        hoursEl.textContent = "00";
        minutesEl.textContent = "00";
        secondsEl.textContent = "00";

        messageEl.textContent = "Hari bahagia telah tiba. Mohon doa restu Anda.";
        clearInterval(countdownInterval);
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    daysEl.textContent = String(days).padStart(2, "0");
    hoursEl.textContent = String(hours).padStart(2, "0");
    minutesEl.textContent = String(minutes).padStart(2, "0");
    secondsEl.textContent = String(seconds).padStart(2, "0");

    messageEl.textContent = "Kami menantikan kehadiran Anda.";
}

document.addEventListener("DOMContentLoaded", function () {
    updateCountdown();
    countdownInterval = setInterval(updateCountdown, 1000);

    const rsvpForm = document.getElementById("rsvpForm");
    if (rsvpForm) {
        rsvpForm.addEventListener("submit", function (event) {
            event.preventDefault();

            const name = document.getElementById("guestName")?.value.trim();
            const attendance = document.getElementById("attendance")?.value;
            const guestCount = document.getElementById("guestCount")?.value;
            const message = document.getElementById("message")?.value.trim();

            if (!name || !attendance) {
                alert("Mohon isi nama dan konfirmasi kehadiran.");
                return;
            }

            const confirmation =
                "KONFIRMASI KEHADIRAN\n\n" +
                "Nama: " + name + "\n" +
                "Kehadiran: " + attendance + "\n" +
                "Jumlah tamu: " + guestCount + " orang\n" +
                "Ucapan: " + (message || "-");

            alert(confirmation);
            this.reset();
        });
    }
});