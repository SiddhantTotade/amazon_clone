// Redirect Page Desktop
document.querySelector('.account').addEventListener('click', () => {
    location.href = '/account.html';
})

document.querySelector('.order').addEventListener('click', () => {
    location.href = '/order.html';
})

document.querySelector('.address').addEventListener('click', () => {
    location.href = '/changeaddress.html';
})

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

// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".mobile").style.display = 'none'
    document.querySelector(".desktop").style.display = 'block'
    document.querySelector(".item-types").style.display = 'none'
    document.querySelector(".carousel-main-mob").style.display = 'none'
    document.querySelector(".card-carousel").style.display = 'none'
    document.querySelector(".upper").style.display = 'none'
    document.querySelector(".lower").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".mobile").style.display = 'block'
    document.querySelector(".desktop").style.display = 'none'
    document.querySelector(".main").style.display = 'none'
    document.querySelector(".grid-container").style.display = 'none'
    document.querySelector(".upper-desk").style.display = 'none'
    document.querySelector(".middle-desk").style.display = 'none'
    document.querySelector(".lower-desk").style.display = 'none'
}

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

// Carousel Mobile
$(document).ready(() => {
    let carouselMob = $('#carousel-mobile')

    carouselMob.owlCarousel({
        items: 1,
        loop: true,
        nav: false,
        dots: true,
        margin: 0,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: false
    });
})


// Carousel
$(document).ready(() => {
    let one = $('#carousel-1')
    let two = $('#carousel-2')
    let three = $('#carousel-3')
    let four = $('#carousel-4')

    one.owlCarousel({
        items: 1,
        loop: true,
        nav: true,
        dots: false,
        margin: 11.5,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: false
    });
    $('.play').on('click', function () {
        owl.trigger('play.owl.autoplay', [5000])
    })
    $('.stop').on('click', function () {
        owl.trigger('stop.owl.autoplay')
    })


    two.owlCarousel({
        nav: true,
        dots: false,
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

    three.owlCarousel({
        nav: true,
        dots: false,
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

    four.owlCarousel({
        nav: true,
        dots: false,
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
})

// Redirect Page Mobile
document.querySelector('.item-card').addEventListener('click', () => {
    location.href = '/product.html'
})
document.querySelector('.carousel-main-mob').addEventListener('click', () => {
    location.href = '/product.html'
})
document.querySelector('.item').addEventListener('click', () => {
    location.href = '/product.html'
})
document.querySelector('.animation,.sub-card-item,.img-grid').addEventListener('click', () => {
    location.href = '/product.html'
})
document.querySelector('.sub-card-item').addEventListener('click', () => {
    location.href = '/product.html'
})
document.querySelector('.img-grid').addEventListener('click', () => {
    location.href = '/product.html'
})