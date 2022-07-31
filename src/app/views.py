from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced, Product_Img_Desktop, Product_Img_Desc_Desktop
from .forms import CustomerRegistrationForm, CustomerProfileForm, UploadProductForm, EditAddressForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random


class ProductView(View):
    def get(self, request):
        totalitem = 0
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        watch = Product.objects.filter(category='W')
        computer_accessories = Product.objects.filter(category='CA')
        random_watch = list(watch)
        watch_shuffle = random.sample(random_watch, 14)
        random_mobile = list(mobiles)
        mobile_shuffle = random.sample(random_mobile, 11)
        mobile_shuffle_mob = random.sample(random_mobile, 4)
        random_item = list(Product.objects.all())
        item_shuffle = random.sample(random_item, 20)
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))

        return render(request, 'app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles, 'laptops': laptops, 'watch': watch, 'computer_accessories': computer_accessories, 'watch_shuffle': watch_shuffle, 'mobile_shuffle': mobile_shuffle, 'mobile_shuffle_mob': mobile_shuffle_mob, 'item_shuffle': item_shuffle, 'totalitem': totalitem})


# def home(request):
#     return render(request, 'app/home.html')

class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        product_img_dsk = Product_Img_Desktop.objects.filter(
            product_img_desktop=product)
        product_desc_desk = Product_Img_Desc_Desktop.objects.filter(
            product_img_desc_desktop=product)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product': product, 'product_img_dsk': product_img_dsk, 'product_desc_desk': product_desc_desk, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})
# def product_detail(request):
#     return render(request, 'app/productdetail.html')


@ login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


@ login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 40.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity*p.product.discounted_price)
                amount += tempamount
                totalamount = amount+shipping_amount
            return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
        else:
            return render(request, 'app/emptycart.html')


def plus_cart(request):
    if request.method == "GET":
        user = request.user
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 40.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.discounted_price)
            amount += tempamount
        data = {'quantity': c.quantity,
                'amount': amount, 'totalamount': amount+shipping_amount}

        return JsonResponse(data)


def minus_cart(request):
    if request.method == "GET":
        user = request.user
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 40.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.discounted_price)
            amount += tempamount
        data = {'quantity': c.quantity,
                'amount': amount, 'totalamount': amount+shipping_amount}

        return JsonResponse(data)


def remove_cart(request):
    if request.method == "GET":
        user = request.user
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.delete()
        amount = 0.0
        shipping_amount = 40.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.discounted_price)
            amount += tempamount
        data = {
            'amount': amount, 'totalamount': amount+shipping_amount}

        return JsonResponse(data)


def buy_now(request):
    return render(request, 'app/buynow.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request,):
        form = CustomerProfileForm()
        return render(request, 'app/editaddress.html', {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality,
                           city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Profile Updated Successfully")

        return render(request, 'app/editaddress.html', {'form': form})


# def profile(request):
#     return render(request, 'app/profile.html')

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    address = Customer.objects.all()
    return render(request, 'app/address.html', {'add': add, 'address': address})


@method_decorator(login_required, name='dispatch')
class SelectAddress(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/selectaddress.html', {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            country = form.cleaned_data['country']
            reg = Customer(user=usr, name=name, address=address, locality=locality,
                           city=city, state=state, zipcode=zipcode, country=country)
            reg.save()
            messages.success(request, "Profile Updated Successfully")

        return render(request, 'app/selectaddress.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class EditAddressView(View):
    def get(self, request):
        form = CustomerProfileForm()
        # edit_add_form = EditAddressForm(request.POST, instance=request.user)
        return render(request, 'app/editaddress.html', {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            country = form.cleaned_data['country']
            reg = Customer(user=usr, name=name, address=address, locality=locality,
                           city=city, state=state, zipcode=zipcode, country=country)
            reg.save()
            messages.success(request, "Profile Updated Successfully")

        return render(request, 'app/editaddress.html', {'form': form})


@login_required
def edit_user_address(request):
    if request.method == 'POST':
        form = EditAddressForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/address')
    else:
        form = EditAddressForm(instance=request.user)
        return render(request, 'app/address.html', {'form': form})


@login_required
def edit_mobile(request):
    return render(request, 'app/editmobile.html')


@login_required
def edit_email(request):
    return render(request, 'app/editemail.html')


@login_required
def edit_name(request):
    return render(request, 'app/editname.html')


@login_required
def payment(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/payment.html', {'add': add})


@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed': op})


@login_required
def account(request):
    return render(request, 'app/account.html')


# def change_password(request):
#     return render(request, 'app/changepassword.html')


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Xiomi' or data == 'Samsung' or data == 'Nokia' or data == 'Realme' or data == 'Oneplus' or data == 'Motorola':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__gt=10000)

    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def login(request):
    return render(request, 'app/login.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registration Successful.")
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})
    # def customerregistration(request):
    #     return render(request, 'app/customerregistration.html')


@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 40.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity*p.product.discounted_price)
            amount += tempamount
        totalamount = amount+shipping_amount
    return render(request, 'app/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items})


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()
        return redirect('orders')


class ProductUpload(View):
    def get(self, request):
        form = UploadProductForm(request.POST, request.FILES)
        return render(request, 'app/uploaddetails.html', {'form': form})

    def post(self, request):
        form = UploadProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.cleaned_data['title']
            product_selling_price = form.cleaned_data['selling_price']
            product_discounted_price = form.cleaned_data['discounted_price']
            product_description = form.cleaned_data['description']
            product_brand = form.cleaned_data['brand']
            product_category = form.cleaned_data['category']
            product_img = form.cleaned_data['product_image']
            save_product = Product(title=product_name, selling_price=product_selling_price,
                                   discounted_price=product_discounted_price, description=product_description,
                                   brand=product_brand.upper(), category=product_category, product_image=product_img)
            save_product.save()
            return render(request, 'app/uploaddetails.html', {'form': form})

        # @login_required
        # def upload_details(request):
        #     category = CATEGORY_CHOICES
        #     dict_category = dict(category)
        #     print("Category", type(category))
        #     if request.method == "POST":
        #         product_name = request.POST.get('product-title')
        #         product_selling_price = request.POST.get('product-selling-price')
        #         product_discounted_price = request.POST.get('product-discounted-price')
        #         product_description = request.POST.get('product-description')
        #         product_brand = request.POST.get('product-brand')
        #         product_category = request.POST.get('product-category')
        #         product_main_image = request.FILES['product-main-image']

        #         print("Product Category", type(product_category))

        #         save_product = Product(title=product_name, selling_price=product_selling_price,
        #                                discounted_price=product_discounted_price, description=product_description,
        #                                brand=product_brand.upper(), category=product_category, product_image=product_main_image)
        #         save_product.save()
        #     return render(request, 'app/uploaddetails.html', {'dict_category': dict_category})
