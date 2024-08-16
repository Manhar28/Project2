from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(unique=True,max_length=40)
    password=models.CharField(max_length=10)
    otp=models.IntegerField(default=1234)

    def __str__(self) -> str:
        return self.name

class main_category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name
     
class sub_category(models.Model):
    main_category=models.ForeignKey(main_category,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name



class product(models.Model):
    sub_category=models.ForeignKey(sub_category,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    img=models.ImageField(upload_to="image")
    img1=models.ImageField(upload_to="image",blank=True,null=True)
    img2=models.ImageField(upload_to="image",blank=True,null=True)
    img3=models.ImageField(upload_to="image",blank=True,null=True)
    qty=models.IntegerField(blank=True,null=True)


    def __str__(self) -> str:
            return self.name


class add_cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="image")
    price=models.IntegerField()
    qty=models.IntegerField()
    total=models.IntegerField()

class billing_address1(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    Pastcode=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)
    phone=models.IntegerField()



     
     