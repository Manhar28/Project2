from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
import random
import razorpay
# Create your views here.

def home(request):
    return HttpResponse("hello python")

def index(request):
    if "email" in request.session:
        
        uid=user.objects.get(email=request.session['email'])
        a_count=add_cart.objects.filter(user=uid).count()
        contaxt={
            "a_count":a_count
        }
        return render(request,"index.html",contaxt)
    else:
        return render(request,"login.html")


def shop(request):
    pid=product.objects.all()
    mid=main_category.objects.all()
    
    sid=request.GET.get("sid")
    if sid:
        pid=product.objects.filter(sub_category=sid)
    else:
        pid=product.objects.all()
    paginator=Paginator(pid,2)
    page_number=request.GET.get("page")
    pid=paginator.get_page(page_number)

    contaxt={
        "pid":pid,
        "mid":mid,
    }
    return render(request,"shop.html",contaxt)


def blog_details(request):
    return render(request,"blog_details.html")

def blog(request):
    return render(request,"blog.html")

def checkout(request):
    uid=user.objects.get(email=request.session['email'])
    aid=add_cart.objects.filter(user=uid)
    l1=[]
    sub_total=0
    total=0
    for i in aid:
        l1.append(i.total)
    sub_total=sum(l1)
    total=sub_total    
    amount = total*100 #100 here means 1 dollar,1 rupree if currency INR
    client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
    print(response,"**************")
    contaxt={
        "aid":aid,
        "uid":uid,
        "sub_total":sub_total,
        "total":total,
        "response":response,
    }
    return render(request,"checkout.html",contaxt)

def contact(request):
    return render(request,"contact.html")

def main(request):
    return render(request,"main.html")

def product_details(request,id):
    p_id=product.objects.get(id=id)
    contaxt={
        "p_id":p_id
    }
    return render(request,"product_details.html",contaxt)

def shop_cart(request):
    uid=user.objects.get(email=request.session['email'])
    aid=add_cart.objects.filter(user=uid)
    a_count=add_cart.objects.filter(user=uid).count()
    l1=[]
    sub_total=0
    total=0

    for i in aid:
        l1.append(i.total)
    sub_total=sum(l1)
    total=sub_total

    contaxt={
        "aid":aid,
        "a_count":a_count,
        "sub_total":sub_total,
        "total":total,
    }
    return render(request,"shop_cart.html",contaxt)

def ragister(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        print(name,email,password,c_password)
        uid=user.objects.filter(email=email).exists()
        if uid:
            contaxt={
                "msg":"invalid email"
            }    
            return render(request,"ragister.html",contaxt)
        else:
            if password == c_password:
                user.objects.create(name=name,email=email,password=password)
                return render(request,"ragister.html")

            else:
                contaxt={
                    "msg":"invalid password"
                }    
                return render(request,"ragister.html",contaxt)
    else:
            return render(request,"ragister.html")

def login(request):
    if "email" in request.session:
        return redirect("index")
    else:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']
            try:
                uid=user.objects.get(email=email)
                if uid.email==email:
                    if uid.password==password:
                        request.session['email']=uid.email
                        return redirect("index")
                    else:
                        contaxt={
                            "msg":"invalid password"
                        }    
                        return render(request,"login.html",contaxt)


                else:
                    return render(request,"login.html")
            except:
                contaxt={
                    "msg":"invalid email"
                }    
                return render(request,"login.html",contaxt)


        else:
            return render(request,"login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect("login")
    else:
        return redirect("login")


def search_fun(request):
    search = request.GET.get("search")
    if search:
        pid = product.objects.filter(name__contains=search)
    context = {
        "pid": pid 
    }
    return render(request, "shop.html", context)


def forgot(request):
    if request.POST:
        email=request.POST['email']
        otp=random.randint(1000,9999)
        try:
            uid=user.objects.get(email=email)
            uid.otp=otp
            uid.save()
            send_mail('simple mail',f"Your Otp Is - {otp}","lionsqued8@gmail.com",[email])
            contaxt={
                "email":email,
                "uid":uid
            }
            return render(request, "confirm_password.html",contaxt)

        except:
            contaxt={
                "msg":"Invalid Email"
            }
            return render(request, "forgot_password.html",contaxt)

    return render(request, "forgot_password.html")

def confirm(request): 
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']
        uid=user.objects.get(email=email)
        if uid.otp == int(otp):
            if new_password == confirm_password:
                uid.password=new_password
                uid.save()
                return redirect("login")
            else:
                contaxt={
                    "msg":"invalid password",
                    "email":email
                }
                return render(request, "confirm_password.html",contaxt)
            
        else:
            contaxt={
                "msg":"invalid otp",
                "email":email
            }
            return render(request, "confirm_password.html",contaxt)

        

    return render(request, "confirm_password.html")

def pricefilter(request):
    if request.POST:
        min=request.POST['min']
        max=request.POST['max']
        print(int(min[1:]),int(max[1:]))
        pid=product.objects.filter(price__gte=int(min[1:]),price__lte=int(max[1:])) # price>=min,price<=max
        contaxt={
            "pid":pid
            }
        return render(request, "shop.html",contaxt)
        
    return render(request, "shop.html")


def add_to_cart(request,id) :
    pid=product.objects.get(id=id)
    uid=user.objects.get(email=request.session['email'])
    aid=add_cart.objects.filter(product=pid,user=uid).exists()
    qty=1
    if request.POST:
        qty=request.POST['qty']
        print(qty)
        
    if aid:
        aid=add_cart.objects.get(product=pid,user=uid)
        aid.qty+=int(qty)
        aid.total=aid.price*aid.qty
        aid.save()
    else:   
        print(qty)
        add_cart.objects.create(product=pid,user=uid,name=pid.name,img=pid.img,price=pid.price,qty=qty,total=pid.price*qty)

    return redirect("shop_cart")           


def cart_plus(request,id) :
    aid=add_cart.objects.get(id=id)
    aid.qty+=1
    aid.total=aid.price*aid.qty
    aid.save()
    return redirect("shop_cart")  

def cart_minus(request,id) :
    aid=add_cart.objects.get(id=id)
    aid.qty-=1
    aid.total=aid.price*aid.qty
    aid.save()    
    if aid.qty==0:
        aid.delete()
    return redirect("shop_cart")  


def cart_remove(request,id) :
    aid=add_cart.objects.get(id=id)
    aid.delete()
    return redirect("shop_cart") 

def billing_address(request):

    if request.POST:
        Firstname=request.POST['Firstname']
        Lastname=request.POST['Lastname']
        country=request.POST['country']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        Pastcode=request.POST['Pastcode']
        email=request.POST['email']
        phone=request.POST['phone']
       
        print(Firstname,Lastname,country,address,city,state,Pastcode,email,phone)
        billing_address1.objects.create(Firstname=Firstname,Lastname=Lastname,country=country,address=address,city=city,state=state,Pastcode=Pastcode,email=email,phone=phone)
    uid=user.objects.get(email=request.session['email'])
    aid=add_cart.objects.filter(user=uid)
    l1=[]
    sub_total=0
    total=0
    for i in aid:
        l1.append(i.total)
    sub_total=sum(l1)
    total=sub_total
    amount = total*100 #100 here means 1 dollar,1 rupree if currency INR
    client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
    print(response,"**************")
    contaxt={
        "aid":aid,
        "sub_total":sub_total,
        "total":total,
        "response":response,
    }

    return render(request,"checkout.html",contaxt) 

