// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".cart-container-mob").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".cart-container").style.display = 'none'
}

// Increment Item Desk
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

// Increment Item Mob
$('.plus-cart-mob').click(function () {
    let id = $(this).attr("pid").toString();
    let eml = this.parentNode.children[1]
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById('amount-mob').innerText = data.amount
            document.getElementById('totalamount-mob').innerText = data.totalamount
        }
    })
})

// Decrement Item Desk
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
// Decrement Item Mob
$('.minus-cart-mob').click(function () {
    let id = $(this).attr("pid").toString();
    let eml = this.parentNode.children[1]
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById('amount-mob').innerText = data.amount
            document.getElementById('totalamount-mob').innerText = data.totalamount
        }
    })
})

// Remove Cart Desktop
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
            document.getElementById('amount').innerText = data.amount
            // document.getElementById('totalamount').innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.remove()
        }
    })
})

// Remove cart Mob
$('.remove-cart-mob').click(function () {
    let id = $(this).attr("pid").toString();
    let eml = this
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function (data) {
            document.getElementById('amount-mob').innerText = data.amount
            // document.getElementById('totalamount-mob').innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})