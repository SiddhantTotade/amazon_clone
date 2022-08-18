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

let next = document.getElementsByClassName('next-mob')
document.getElementById('paypal-mob').addEventListener('click', () => {
    for (let index = 0; index < next.length; index++) {
        next[index].style.display = 'flex'
    }
});

window.onload = () => {
    alert("Please select paypal option to proceed")
}