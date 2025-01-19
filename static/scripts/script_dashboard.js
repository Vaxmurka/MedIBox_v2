function updateClock() {
    const now = new Date();

    let hours = now.getHours();
    let minute = now.getMinutes();

    const elem = document.querySelector('#timeField') //.querySelector('span');
    elem.textContent = String(hours) + "h " + String(minute < 10 ? 0 : '') + String(minute) + "m";

}

setInterval(updateClock, 1000);