// Media Query
if (window.screen.width >= 400) {
    document.querySelector('.payment-mob').style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".payment").style.display = 'none'
}

// Session storage
document.querySelector('#paypal').addEventListener('click', () => {
    let paypal_val = document.querySelector('#paypal').value;
    sessionStorage.setItem("paypal_checked", paypal_val)
});

window.onload = () => {
    sessionStorage.clear()
}