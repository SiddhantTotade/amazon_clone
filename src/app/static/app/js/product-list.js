// Sidebar Menu
const openMenu = document.querySelector('#open-menu')
const closeMenu = document.querySelector('.close-menu')
const openMenuDesktop = document.querySelector('.open-menu-desktop')
const closeMenuDesktop = document.querySelector('.close-menu-desktop')

openMenu.addEventListener('click', () => {
    document.querySelector('.sidebar').style.width = "250px";
});

closeMenu.addEventListener('click', () => {
    document.querySelector('.sidebar').style.width = "0";
});

openMenuDesktop.addEventListener('click', () => {
    document.querySelector('.sidebar-desktop').style.width = "350px";
});

closeMenuDesktop.addEventListener('click', () => {
    document.querySelector('.sidebar-desktop').style.width = "0";
});

// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".desktop").style.display = 'grid'
    document.querySelector(".mobile").style.display = 'none'
    document.querySelector(".page-1-mob").style.display = 'none'
    document.querySelector(".page-2-mob").style.display = 'none'
    document.querySelector(".upper").style.display = 'none'
    document.querySelector(".lower").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".product-list-container-mob").style.display = 'grid'
    document.querySelector(".desktop").style.display = 'none'
    document.querySelector(".page-1").style.display = 'none'
    document.querySelector(".page-2").style.display = 'none'
    document.querySelector(".upper-desk").style.display = 'none'
    document.querySelector(".middle-desk").style.display = 'none'
    document.querySelector(".lower-desk").style.display = 'none'
}

// Redirect Page Desktop
document.querySelector('.cart').addEventListener('click', () => {
    location.href = '/cart.html';
})

// Redirect Page Mobile
document.getElementById('uil-shopping-cart').addEventListener('click', () => {
    location.href = '/cart.html';
})

// Dropdown Menu
let dropdownBtn = document.querySelector(".dropdown-btn")
let menuContent = document.querySelector(".dropdown-menu")

dropdownBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    menuContent.classList.toggle('show')
});

window.onclick = () => {
    menuContent.classList.remove('show')
}

// Pagination Desktop
document.querySelector('#one').addEventListener('click', () => {
    document.getElementsByClassName('.page-1').style.display = "grid"
    document.getElementsByClassName('.page-2').style.display = "none"
})
document.querySelector('#two').addEventListener('click', () => {
    document.querySelector('.page-2').style.display = "grid"
    document.querySelector('.page-1').style.display = "none"
})
document.querySelector('.prev').addEventListener('click', () => {
    document.querySelector('.page-1').style.display = "grid"
    document.querySelector('.page-2').style.display = "none"
})
document.querySelector('.next').addEventListener('click', () => {
    document.querySelector('.page-2').style.display = "grid"
    document.querySelector('.page-1').style.display = "none"
})

// Pagination Mobile
document.querySelector('#one-mob').addEventListener('click', () => {
    document.getElementsByClassName('.page-1-mob').style.display = "grid"
    document.getElementsByClassName('.page-2-mob').style.display = "none"
})
document.querySelector('#two-mob').addEventListener('click', () => {
    document.querySelector('.page-2-mob').style.display = "grid"
    document.querySelector('.page-1-mob').style.display = "none"
})
document.querySelector('.prev-mob').addEventListener('click', () => {
    document.querySelector('.page-1-mob').style.display = "grid"
    document.querySelector('.page-2-mob').style.display = "none"
})
document.querySelector('.next-mob').addEventListener('click', () => {
    document.querySelector('.page-2-mob').style.display = "grid"
    document.querySelector('.page-1-mob').style.display = "none"
})