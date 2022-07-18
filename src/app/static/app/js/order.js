// Redirect Page Desktop
document.querySelector('.cart').addEventListener('click', () => {
    location.href = '/cart.html';
})

document.querySelector('.uil-shopping-cart').addEventListener('click', () => {
    location.href = '/cart.html';
})
// For Desktop
document.querySelector('.search-btn').addEventListener('click', (e) => {
    if (document.getElementById('search-bar').value.toLowerCase() == 'mobile') {
        e.preventDefault();
        window.location.href = '/product-list.html';
        document.getElementById('search-bar').value = " ";
    }
    else {
        alert('Please type mobile in search bar.')
    }
})

// For Mobile
document.querySelector('.submit-btn').addEventListener('click', (e) => {
    if (document.getElementById('search-bar-mob').value.toLowerCase() == 'mobile') {
        e.preventDefault();
        window.location.href = '/product-list.html';
        document.getElementById('search-bar-mob').value = " ";
    }
    else {
        alert('Please type mobile in search bar.')
    }
})

let item = document.querySelectorAll('.item,.carousel-main-mob,.item-card,.img-grid,.animation,.sub-card-item')

Array.prototype.forEach.call(item, (e) => {
    e.addEventListener('click', () => {
        location.href = '/product.html'
    })
})

// Sidebar Menu
const openMenu = document.querySelector('.open-menu')
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

// Dropdown
let dropdownBtn = document.querySelector(".dropdown-btn")
let menuContent = document.querySelector(".dropdown-menu")

dropdownBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    menuContent.classList.toggle('show')
});

window.onclick = () => {
    menuContent.classList.remove('show')
}

// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".desktop").style.display = 'block'
    document.querySelector(".mobile").style.display = 'none'
    document.querySelector(".orders-mob").style.display = 'none'
    document.querySelector(".upper").style.display = 'none'
    document.querySelector(".lower").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".mobile").style.display = 'block'
    document.querySelector(".desktop").style.display = 'none'
    document.querySelector(".orders").style.display = 'none'
    document.querySelector(".upper-desk").style.display = 'none'
    document.querySelector(".middle-desk").style.display = 'none'
    document.querySelector(".lower-desk").style.display = 'none'
}