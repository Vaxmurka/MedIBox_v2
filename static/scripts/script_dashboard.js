const desktopBlock = document.querySelectorAll('.patient-row');
const mobileBlock = document.querySelectorAll('.patient-column');

function checkScreenWidth() {
    if (window.innerWidth < 700) {
        desktopBlock.forEach(elem => { elem.style.display = 'none'; });
        mobileBlock.forEach(elem => { elem.style.display = ''; });

    } else {
        mobileBlock.forEach(elem => { elem.style.display = 'none'; });
        desktopBlock.forEach(elem => { elem.style.display = ''; });
    }
}

// Вызываем функцию при загрузке страницы
checkScreenWidth();

// Добавляем обработчик события при изменении размера окна
window.addEventListener('resize', checkScreenWidth);


function updateClock() {
    const now = new Date();

    let hours = now.getHours();
    let minute = now.getMinutes();

    const elem = document.querySelector('#timeField') //.querySelector('span');
    elem.textContent = String(hours) + "h " + String(minute < 10 ? 0 : '') + String(minute) + "m";

}

setInterval(updateClock, 1000);