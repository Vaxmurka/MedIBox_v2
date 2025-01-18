function updateClock() {
    const now = new Date();

    let hours = now.getHours();
    let minute = now.getMinutes();

    const elem = document.querySelector('#timeField').querySelector('span');
    elem.textContent = String(hours) + ":" + String(minute < 10 ? 0 : '') + String(minute);

}

setInterval(updateClock, 1000);