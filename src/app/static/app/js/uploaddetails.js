// Category Dropdown
let productCategory = document.querySelector('.select-product-category')
let dropdownCategory = document.querySelector('.product-category-dropdown')

productCategory.addEventListener('click', (e) => {
    e.stopPropagation()
    console.log("clicked");
    dropdownCategory.classList.toggle('show')
})

window.onclick = () => {
    dropdownCategory.classList.remove('show')
}