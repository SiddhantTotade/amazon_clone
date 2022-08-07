// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".thank-you-mob").style.display = 'none'
    document.querySelector(".continue-shopping-mob").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".thankyou").style.display = 'none'
    document.querySelector(".continue-shopping").style.display = 'none'
}