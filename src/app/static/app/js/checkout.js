if (window.screen.width >= 400) {
    document.querySelector('.checkout-container').style.display = 'bock'
    document.querySelector('.checkout-container-mob').style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".checkout-container-mob").style.display = 'block'
    document.querySelector(".checkout-container").style.display = 'none'
}