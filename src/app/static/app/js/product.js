// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".product-mob").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".product").style.display = 'none'
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
    nav: false,
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

// List-item
document.getElementById('show-more').addEventListener('click', () => {
    document.getElementById('list-item-more').style.display = "grid"
    document.getElementById('list-item').style.display = "none"
})
document.getElementById('show-less').addEventListener('click', () => {
    document.getElementById('list-item-more').style.display = "none"
    document.getElementById('list-item').style.display = "grid"
})