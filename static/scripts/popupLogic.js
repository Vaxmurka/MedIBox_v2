const removeBtn = document.querySelector('.btnRemove');
const closeBtn = document.querySelector('.btnClose');

removeBtn.addEventListener('click', function (e) {
    showDialog('delete');
}, false);

closeBtn.addEventListener('click', function (e) {
    showDialog('logout');
}, false);

const dialog = document.querySelector('.popup_profile');

function showDialog(type) {
    dialog.innerHTML = `
        <p>Вы точно в этом уверены?</p>
        <div class="btns">
            <button class="YesBtn profile__card-btn btnRemove" onclick="popupChannels('${type}')">Да (5)</button>
            <button class="CanselBtn profile__card-btn" onclick="window.popup.close()">Отмена</button>
        </div>
    `;

    const answ = document.querySelector('.YesBtn');
    answ.disabled = true;
    let timeLeft = 5;

    const countdown = setInterval(() => {
        if (timeLeft > 1) {
            timeLeft--;
            answ.textContent = `Да (${timeLeft})`;
        } else {
            clearInterval(countdown);
            answ.textContent = 'Да';
            answ.disabled = false;
        }
    }, 1000);

    window.popup.showModal();
}

function popupChannels(type) {
    const loc = "http://" + window.location.host;
    window.location.href = loc + "/" + type;
}