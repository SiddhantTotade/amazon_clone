// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".item-types").style.display = 'none'
    document.querySelector(".carousel-main-mob").style.display = 'none'
    document.querySelector(".card-carousel").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".main").style.display = 'none'
    document.querySelector(".grid-container").style.display = 'none'
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

// Modal
window.onload = () => {
    document.getElementById('myModal').style.display = 'grid'
}

document.querySelector('.close-modal').addEventListener('click', () => {
    document.getElementById('myModal').style.display = 'none'
})