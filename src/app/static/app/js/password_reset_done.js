// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".login-mobile").style.display = 'none'
    document.querySelector(".delivery-footer").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".login-desktop").style.display = 'none'
}