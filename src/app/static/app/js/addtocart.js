// Sidebar
const openMenu = document.querySelector('#open-menu')
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

// Dropdown
let dropdownBtn = document.querySelector(".dropdown-btn")
let menuContent = document.querySelector(".dropdown-menu")

dropdownBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    menuContent.classList.toggle('show')
});

window.onclick = () => {
    menuContent.classList.remove('show')
}

// Product Counter
const counter = document.querySelectorAll('.product-counter');

counter.forEach((node) => {
    let i = 1
    const itemCount = node.querySelector('.counter')
    const incr = node.querySelector('.incr')
    const decr = node.querySelector('.decr')
    const del = node.querySelector('.delete')

    incr.addEventListener('click', () => {
        i++;
        itemCount.innerHTML = i;
    })
    decr.addEventListener('click', () => {
        if (i > 1) {
            i--;
            itemCount.innerHTML = i;
        }
    })
    del.addEventListener('click', () => {
        del.parentElement.parentElement.parentElement.remove()
    })
})

// Media Query
if (window.screen.width >= 400) {
    document.querySelector(".cart-container-mob").style.display = 'none'
}
else if (window.screen.width <= 400) {
    document.querySelector(".cart-container").style.display = 'none'
}