// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".product-mob").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".product").style.display = 'none'
}

// List-item
document.getElementById('list-item')

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