// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".login-desktop").style.display = 'block'
    document.querySelector(".login-mobile").style.display = 'none'
    document.querySelector(".delivery-footer").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".login-desktop").style.display = 'none'

}

// Login and Create for Mobile
document.getElementById('user').style.display = 'none'

document.getElementById('signin').addEventListener('click', () => {
    signin.checked = true
    create.checked = false
    document.getElementById('email').style.display = 'grid'
    document.getElementById('user').style.display = 'none'
})
document.getElementById('create').addEventListener('click', () => {
    create.checked = true
    signin.checked = false
    document.getElementById('user').style.display = 'block'
    document.getElementById('email').style.display = 'none'
})