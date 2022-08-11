from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_countries.fields import CountryField
# Create your models here.


STATE_CHOICES = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"), ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"), ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"), ("Odisha", "Odisha"),
                 ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"), ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"), ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(default=None, max_length=100)
    locality = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    zipcode = models.IntegerField()
    country = CountryField()

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('address')


CATEGORY_CHOICES = (('M', 'Mobile'), ('L', 'Laptop'),
                    ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('W', 'Watch'),
                    ('P', 'Printer'), ('F', 'Fan'), ('EB', 'Earbuds'),
                    ('C', 'Camera'), ('O', 'Oil'), ('SH', 'Shower'), ('MU', 'Museli'), ('CL', 'Cleaner'), ('CA', 'Computer and Accessories'))


class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    product_details = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Product_Img_Desktop(models.Model):
    product_img_desktop = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    product_img_desk = models.ImageField(null=False, blank=False,
                                         default=None, upload_to='product_img_desktop')

    def __str__(self):
        return str(self.product_img_desktop.id)


class Product_Img_Desc_Desktop(models.Model):
    product_img_desc_desktop = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    product_img_desc_desk = models.ImageField(
        upload_to='product_img_desc_desktop')

    def __str__(self):
        return str(self.product_img_desc_desktop.id)


class Product_Img_Color_Desktop(models.Model):
    product_img_color_desktop = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    product_img_color_desk = models.ImageField(
        upload_to='product_img_color_desktop')

    def __str__(self):
        return str(self.product_img_color_desktop.id)


class Product_Img_Mobile(models.Model):
    product_img_mobile = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    product_img_mob = models.ImageField(
        upload_to='product_img_mobile')

    def __str__(self):
        return str(self.product_img_mobile.id)


class Product_Img_Desc_Mobile(models.Model):
    product_img_desc_mobile = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    product_img_desc_mob = models.ImageField(
        upload_to='product_img_desc_mobile')

    def __str__(self):
        return str(self.product_img_desc_mobile.id)


class Product_Img_Color_Mobile(models.Model):
    product_img_color_mobile = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    product_img_color_mob = models.ImageField(
        upload_to='product_img_color_mobile')

    def __str__(self):
        return str(self.product_img_desc_mobile.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (('Accepted', 'Accepted'), ('Packed', 'Packed'),
                  ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'))


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
