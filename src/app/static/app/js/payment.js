// Media Query
if (window.screen.width >= 400) {
    document.querySelector('.payment-mob').style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".payment").style.display = 'none'
}

// Session storage
document.getElementById('paypal').addEventListener('click', () => {
    document.getElementById('continue').style.display = 'flex'
});

window.onload = () => {
    alert("Please select paypal option to proceed")
}