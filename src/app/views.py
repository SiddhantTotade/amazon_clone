from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced, Product_Img_Desktop, Product_Img_Desc_Desktop
from .forms import CustomerRegistrationForm, CustomerProfileForm, UploadProductForm, EditUsernameForm, EditUserEmailForm, MyPasswordResetForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random
import datetime


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
        random_laptop = list(laptops)
        random_computer_accessories = list(computer_accessories)
        mobile_shuffle = random.sample(random_mobile, 11)
        mobile_shuffle_mob = random.sample(random_mobile, 4)
        watch_shuffle_mob = random.sample(random_watch, 4)
        com_acc_shuffle_mob = random.sample(random_computer_accessories, 4)
        laptop_shuffle_mob = random.sample(random_laptop, 4)
        random_item = list(Product.objects.all())
        item_shuffle = random.sample(random_item, 20)
        address = Customer.objects.first()
        product_name = request.GET.get('Mobile')
        print(product_name)
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))

        return render(request, 'app/home.html', {'address': address, 'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles, 'laptops': laptops, 'watch': watch, 'computer_accessories': computer_accessories, 'watch_shuffle': watch_shuffle, 'mobile_shuffle': mobile_shuffle, 'mobile_shuffle_mob': mobile_shuffle_mob, 'com_acc_shuffle_mob': com_acc_shuffle_mob, 'watch_shuffle_mob': watch_shuffle_mob, 'laptop_shuffle_mob': laptop_shuffle_mob, 'item_shuffle': item_shuffle, 'totalitem': totalitem})


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
        product_detail = Product.objects.get(id=pk)
        product_detail_dict = eval(product_detail.product_details)
        address = Customer.objects.first()
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'address': address, 'product': product, 'product_img_dsk': product_img_dsk, 'product_desc_desk': product_desc_desk, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem, 'product_detail_dict': product_detail_dict})
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
        address = Customer.objects.first()
        # cart_amount = Cart.objects.get(user=user)
        amount = 0.0
        shipping_amount = 40.0
        # if cart_amount.product.discounted_price >= 499:
        #     cart_amount = cart_amount.product.discounted_price
        # else:
        #     cart_amount = cart_amount.product.discounted_price
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity*p.product.discounted_price)
                amount += tempamount
                totalamount = amount+shipping_amount
            return render(request, 'app/addtocart.html', {'address': address, 'carts': cart, 'totalamount': totalamount, 'amount': amount})
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
    def get(self, request):
        user = User.objects.all()
        address = Customer.objects.first()
        return render(request, 'app/profile.html', {'address': address, 'user': user})


@method_decorator(login_required, name='dispatch')
class AddAddressView(View):
    def get(self, request):
        form = CustomerProfileForm()
        address = Customer.objects.first()
        return render(request, 'app/addaddress.html', {'address': address, 'form': form})

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
            return redirect('address')

        return render(request, 'app/addaddress.html', {'form': form})


@login_required
def address(request):
    address = Customer.objects.filter(user=request.user)
    add = Customer.objects.first()
    return render(request, 'app/address.html', {'location': add, 'address': address})


@method_decorator(login_required, name='dispatch')
class SelectAddress(View):
    def get(self, request, pk):
        product_id = Product.objects.get(pk=pk)
        address = Customer.objects.filter(user=request.user)
        form = CustomerProfileForm()
        add = Customer.objects.first()
        return render(request, 'app/selectaddress.html', {'location': add, 'product_id': product_id, 'form': form, 'address': address})

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

        return render(request, 'app/selectaddress.html', {'form': form})


@login_required
def edit_address(request, pk):
    edit_add = Customer.objects.get(pk=pk)
    address = Customer.objects.first()
    form = CustomerProfileForm(instance=edit_add)

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=edit_add)
        if form.is_valid():
            form.save()
            return redirect('address')

    return render(request, 'app/editaddress.html', {'address': address, 'form': form, 'edit_add': edit_add})


@login_required
def delete_address(request, pk):
    del_add = Customer.objects.get(pk=pk)
    address = Customer.objects.first()

    if request.method == 'POST':
        del_add.delete()
        return redirect('address')
    return render(request, 'app/deleteaddress.html', {'address': address, 'del_add': del_add})


@login_required
def edit_email(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        form = EditUserEmailForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'app/editemail.html', {'form': form})
    else:
        form = EditUserEmailForm(instance=request.user)
        address = Customer.objects.first()
        return render(request, 'app/editemail.html', {'address': address, 'form': form})


@login_required
def edit_name(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        form = EditUsernameForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'app/editname.html', {'form': form})
    else:
        form = EditUsernameForm(instance=request.user)
        address = Customer.objects.first()
        return render(request, 'app/editname.html', {'address': address, 'form': form})


@login_required
def payment(request, pk):
    product_id = Product.objects.get(pk=pk)
    cust_id = request.GET.get('custid')
    add = Customer.objects.filter(user=request.user)
    address = Customer.objects.first()
    return render(request, 'app/payment.html', {'address': address, 'product_id': product_id, 'add': add, 'cust_id': cust_id})


@login_required
def orders(request):
    address = Customer.objects.first()
    op = OrderPlaced.objects.filter(user=request.user)
    delivery_date = (datetime.datetime.now() +
                     datetime.timedelta(days=10)).strftime("%A")

    return render(request, 'app/orders.html', {'address': address, 'order_placed': op, 'delivery_date': delivery_date})


@login_required
def account(request):
    address = Customer.objects.first()
    return render(request, 'app/account.html', {'address': address})


# def reset_password(request):
#     form = MyPasswordResetForm(request.POST)
#     if form.is_valid():
#         passcode_ascii = ''.join(random.choice(
#             string.ascii_uppercase)for _ in range(2))
#         passcode_num = ''.join(random.choice(string.digits)for _ in range(3))
#         passcode = passcode_ascii.join(passcode_num)
#         email = form.cleaned_data['email']
#         print(request.user)
#         # email_sender = 'noreply.amazonclone.project@gmail.com'
#         # email_password = password
#         # email_receiver = email
#         # sub = "Reset Password"
#         # body = """Username : request.user"""
#     return render(request, 'app/password_reset.html', {'form': form})


class PasswordResetView(View):
    def get(request):
        form = MyPasswordResetForm
        return render(request, 'app/password_reset.html', {'form': form})

    def post(request):
        form = MyPasswordResetForm
        user_email = form.cleaned_data['email']
        print(user_email)
        return render(request, 'app/password_reset.html', {'form': form})


def product_list(request):
    if request.method == 'POST':
        if request.POST.get('Mobile') == 'Mobile':
            product_name = 1
        elif request.POST.get('Watch') == 'Watch':
            product_name = 2
        elif request.POST.get('Laptop') == 'Laptop':
            product_name = 3
        elif request.POST.get('ComAndAcc') == 'ComAndAcc':
            product_name = 4

        match (product_name):
            case 1:
                product_name = 'M'
            case 2:
                product_name = 'W'
            case 3:
                product_name = 'L'
            case 4:
                product_name = 'CA'

        product = Product.objects.filter(category=product_name)
        return render(request, 'app/product-list.html', {'product': product})
    else:
        PRODUCT_CHOICES = {'M': 'mobiles', 'L': 'laptops',
                           'TW': 'top wears', 'BW': 'bottom wears', 'W': 'watches',
                           'P': 'printers', 'F': 'fans', 'EB': 'earbuds',
                           'C': 'cameras', 'O': 'oils', 'SH': 'showers', 'MU': 'muselis', 'CL': 'cleaners', 'CA': 'computer and accessories'}
        if "search_products" in request.GET:
            search_product = request.GET.get('search_products')
        product_key = ""
        product_check = 0
        address = Customer.objects.first()
        for key, val in PRODUCT_CHOICES.items():
            if search_product.lower() == val:
                product_key = key
                product_check = 1
        if product_check:
            product = Product.objects.filter(
                category=product_key)
        elif product_check == 0:
            brand_name = search_product.split(" ")
            brand_filter = brand_name
            price_limit = brand_name.pop()
            if len(brand_name) == 1:
                product = Product.objects.filter(
                    brand=brand_name[0].upper())
            elif len(brand_name) != 1:
                if any(char.isdigit() for char in search_product):
                    price_limit = int(price_limit)
                    for key, val in PRODUCT_CHOICES.items():
                        try:
                            if brand_name[0].lower() == val:
                                product_key = key
                            product = Product.objects.filter(
                                category=product_key).filter(discounted_price__lt=price_limit)
                        except:
                            return redirect('noproduct')
                else:
                    for key, val in PRODUCT_CHOICES.items():
                        try:
                            if brand_filter[1].lower() == val:
                                product_key = key
                            product = Product.objects.filter(
                                category=product_key).filter(brand=brand_filter[0].upper())
                        except:
                            return redirect('noproduct')
    return render(request, 'app/product-list.html', {'address': address, 'product': product})
    # return render(request, 'app/product-list.html')


def no_product(request):
    return render(request, 'app/noproduct.html')


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
    address = Customer.objects.first()
    user = request.user
    cust_id = request.GET.get('custid')
    product_id = request.GET.get('prod_id')
    delivery_date = (datetime.datetime.now() +
                     datetime.timedelta(days=10)).strftime("%d %B %Y")

    try:
        if request.META['HTTP_REFERER'] == 'http://127.0.0.1:8000/payment/'+product_id+"?custid="+cust_id:
            product = Product.objects.get(id=product_id)
            if not Cart.objects.filter(user=user, product=product).exists():
                Cart(user=user, product=product).save()
        return render(request, 'app/checkout.html', {'address': address, 'product_id': product_id, 'add': add, 'totalamount': totalamount, 'item_amount': item_amount, 'cart_items': cart_items, 'delivery_date': delivery_date, 'custid': cust_id})
    except:
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        amount = 0.0
        item_amount = 0.0
        shipping_amount = 40.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity*p.product.discounted_price)
                amount += tempamount
            totalamount = amount+shipping_amount
        for p in cart_product:
            item_amount += p.product.discounted_price
        return render(request, 'app/checkout.html', {'address': address, 'product_id': product_id, 'add': add, 'totalamount': totalamount, 'item_amount': item_amount, 'cart_items': cart_items, 'delivery_date': delivery_date, 'custid': cust_id})


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    delivery_date = (datetime.datetime.now() +
                     datetime.timedelta(days=10)).strftime("%d %B %Y")
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()
        return render(request, 'app/thankyou.html', {'delivery_date': delivery_date})


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
