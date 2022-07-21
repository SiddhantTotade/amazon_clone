// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".desktop").style.display = 'block'
    document.querySelector(".mobile").style.display = 'none'
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