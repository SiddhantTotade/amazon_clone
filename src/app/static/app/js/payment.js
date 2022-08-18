// Media Query
if (window.screen.width >= 400) {
    document.querySelector('.payment-mob').style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".payment").style.display = 'none'
}

// Continue to payment button
document.getElementById('paypal').addEventListener('click', () => {
    document.getElementById('continue').style.display = 'flex';
});

document.getElementById('paypal-mob').addEventListener('click', () => {
    document.getElementById('next-mob').style.display = 'flex';
});

let next = document.querySelectorAll('#next-mob')




window.onload = () => {
    alert("Please select paypal option to proceed")
}