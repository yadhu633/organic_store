from django.db import models

# Create your models here.
class reguser(models.Model):
    yourname=models.CharField(max_length=20)
    username=models.CharField(max_length=20,unique=True)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=20)
    repassword=models.CharField(max_length=20)
    def __str__(self):
        return self.yourname
class regshop(models.Model):
    profile=models.FileField(upload_to='static')
    ownername=models.CharField(max_length=20)
    shopname=models.CharField(max_length=20,unique=True)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=20)
    re_password=models.CharField(max_length=20)
    status=models.BooleanField(default="True")
    def __str__(self):
        return self.shopname
class additem(models.Model):
    shopname=models.ForeignKey(regshop,on_delete=models.CASCADE)
    product_id=models.CharField(max_length=20,unique=True)
    product_name=models.CharField(max_length=10)
    price=models.IntegerField(max_length=20)
    stock=models.IntegerField(max_length=20)
    category=models.CharField(default="vegerable",max_length=20)
    image=models.FileField(upload_to='static')

    def __int__(self):
        return self.product_name
class cart(models.Model):
    product_name=models.ForeignKey(additem,on_delete=models.CASCADE)
    username=models.ForeignKey(reguser,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total_price=models.IntegerField()
    def __int__(self):
        return self.product_name
# class buy(models.Model):
#     product_name = models.ForeignKey(additem, on_delete=models.CASCADE)
#     username = models.ForeignKey(reguser, on_delete=models.CASCADE)
#
#     def __int__(self):
#         return self.product_name

class displaycart(models.Model):
    product_name = models.ForeignKey(additem, on_delete=models.CASCADE)
    username = models.ForeignKey(reguser, on_delete=models.CASCADE)

class order(models.Model):
    product=models.ForeignKey(additem, on_delete=models.CASCADE)
    user=models.ForeignKey(reguser, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total_price=models.IntegerField()
    date=models.DateField()

class feedback(models.Model):
    shop=models.ForeignKey(regshop,on_delete=models.CASCADE)
    user=models.ForeignKey(reguser,on_delete=models.CASCADE)
    feed=models.CharField(max_length=100)

