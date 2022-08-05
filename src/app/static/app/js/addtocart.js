// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".cart-container-mob").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".cart-container").style.display = 'none'
}

// Increment Item
$('.plus-cart').click(function () {
    let id = $(this).attr("pid").toString();
    let eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
        }
    })
})

// Decrement Item
$('.minus-cart').click(function () {
    let id = $(this).attr("pid").toString();
    let eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
        }
    })
})

// Remove Item
$('.remove-cart').click(function () {
    let id = $(this).attr("pid").toString();
    let eml = this
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function (data) {
            console.log(eml.parentNode.parentNode.parentNode);
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.remove()
        }
    })
})