// Redirect Page Desktop
document.querySelector('.buynow').addEventListener('click', () => {
    location.href = '/address.html'
})

document.querySelector('.addtocart').addEventListener('click', () => {
    alert('Your item has been added to the cart')
})

document.querySelector('.cart').addEventListener('click', () => {
    location.href = '/cart.html';
})


// Redirect Page Mobile
document.querySelector('.buynow-mob').addEventListener('click', () => {
    location.href = '/address.html'
})

document.querySelector('.addtocart-mob').addEventListener('click', () => {
    alert('Your item has been added to the cart')
})

document.getElementById('uil-shopping-cart').addEventListener('click', () => {
    location.href = '/cart.html';
})

// Sidebar
const openMenu = document.querySelector('#open-menu')
const closeMenu = document.querySelector('#close-menu')
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

if (window.screen.width >= 400) {
    document.querySelector(".mobile").style.display = 'none'
    document.querySelector(".desktop").style.display = 'block'
    document.querySelector(".product-mob").style.display = 'none'
    document.querySelector(".upper").style.display = 'none'
    document.querySelector(".lower").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".mobile").style.display = 'block'
    document.querySelector(".desktop").style.display = 'none'
    document.querySelector(".product").style.display = 'none'
    document.querySelector(".upper-desk").style.display = 'none'
    document.querySelector(".middle-desk").style.display = 'none'
    document.querySelector(".lower-desk").style.display = 'none'
    document.querySelector(".copyright").style.display = 'none'
}

// Product Zoom
$(function () {
    $(".xzoom,.xzoom-gallery").xzoom({
        zoomWidth: 500,
        zoomHeight: 500,
        tint: "#331",
        Xoffset: 50,
    })
});


// Product Carousel
$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 0,
    dots: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})