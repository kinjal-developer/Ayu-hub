from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255,blank=True)
    price=models.FloatField(default=0)
    itemimage = models.FileField(upload_to='media/', blank=True, default='tea.jpg')
    available=models.IntegerField(default=0)
    sold = models.IntegerField(default=0)

class User(models.Model):
    email=models.EmailField(unique=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    password=models.CharField(max_length=50)
    otp=models.IntegerField(default=456)
    is_active=models.BooleanField(default=True)
    is_varfied=models.BooleanField(default=False)
    role=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
    first_time_login=models.BooleanField(default=False)
    a_ddress1 = models.CharField(max_length=255, blank=True)

class Customer(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic=models.FileField(upload_to='medico_expert/images/',blank=True,default='default.jpg')
    firstname=models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    about = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    contactno = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=70, blank=True)
    terms=models.BooleanField(default=False)
    password = models.CharField(max_length=50)

class Admin(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic=models.FileField(upload_to='medico_expert/images/',blank=True,default='default.jpg')
    firstname=models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    about = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    contactno = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=70, blank=True)
    terms=models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    product =models.BooleanField(default=False)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # ordered=models.booleanField(default=False)
    total_price=models.FloatField(default=0)

class Cartitem(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    price = models.FloatField(default=0)
    number=models.IntegerField(default=1)
    subtotal = models.FloatField(default=0)
    total=models.FloatField(default=0)
    grandtotal = models.FloatField(default=0)
    itemimage = models.FileField(upload_to='media/', blank=True, default='tea.jpg')

class Likeproduct(models.Model):
    name = models.CharField(max_length=255, blank=True)
    price = models.FloatField(default=0)
    itemimage = models.FileField(upload_to='media/', blank=True, default='tea.jpg')

class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True)
    mobile = models.IntegerField(default=1)
    a_ddress2 = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    pincode = models.IntegerField(default=1)





