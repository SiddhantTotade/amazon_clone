from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Customer, Product, Cart, OrderPlaced, Product_Img_Desktop, Product_Img_Desc_Desktop
# Register your models here.


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name',
                    'locality', 'city', 'zipcode', 'state']


class Product_Img_Admin(admin.StackedInline):
    model = Product_Img_Desktop


class Product_Img_Desc_Admin(admin.StackedInline):
    model = Product_Img_Desc_Desktop


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price',
                    'discounted_price', 'description', 'brand', 'category', 'product_image']
    inlines = [Product_Img_Admin, Product_Img_Desc_Admin]

    class Meta:
        model = Product


@admin.register(Product_Img_Desktop)
class Product_Image_Admin(admin.ModelAdmin):
    pass


@admin.register(Product_Img_Desc_Desktop)
class Product_Image_Desc_Admin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product',
                    'quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'customer_info',
                    'product', 'product_info', 'quantity', 'ordered_date', 'status']

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
