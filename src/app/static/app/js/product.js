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
jQuery('.owl-carousel').owlCarousel({
    // Here goes default configs
    responsive : {
      // breakpoint from 0 up
      0 : {
        stagePadding: 0,
        loop: false,
        responsiveClass: true,
        dots: true,
        nav: true,
        autoHeight: true,
        items: 1
      },
      // breakpoint from 768 up
    //   100 : {
    //     items: 1
    //   }
    }
  });

// List-item
// document.getElementById('show-more').addEventListener('click', () => {
//     document.getElementById('list-item-more').style.display = "grid"
//     document.getElementById('list-item').style.display = "none"
// })
// document.getElementById('show-less').addEventListener('click', () => {
//     document.getElementById('list-item-more').style.display = "none"
//     document.getElementById('list-item').style.display = "grid"
// })