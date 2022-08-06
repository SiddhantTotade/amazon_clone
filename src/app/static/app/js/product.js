// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".product-mob").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".product").style.display = 'none'
}

// List Item
let listItem = document.getElementById('list-item');
console.log(listItem.innerText);

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