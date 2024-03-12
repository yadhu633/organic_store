from django.shortcuts import render,HttpResponse,redirect
from.models import *
from django.contrib import  messages
import razorpay
import datetime
from django.shortcuts import redirect

# Create your views here.

def index(re):
    data = additem.objects.all()
    return render(re,'index.html',{'data':data})
def home(re):
    data = additem.objects.all()
    return render(re,'home.html',{'data':data})
def booking(re):
    return render(re,'booking.html')
def shops(re):
    data=regshop.objects.all()
    return render(re,'shops.html',{'data':data})
def contact(re):
    return render(re,'contact.html')
def shopdetails(re):
    return render(re,'shop-details.html')
def shopgrid(re):
    if re.method == 'POST':
        price = re.POST['price']
    data=additem.objects .all()
    data1=additem.objects.filter(category="vegetable")
    data2=additem.objects.filter(category="fruit")
    data3=additem.objects.filter(category="nuts")
    return render(re,'shop-grid.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
# def shopcart(re):
#     if re.method == 'POST':
#         price = re.POST['price']
#         data = additem.objects.all()
#     return render(re,'shoping-cart.html',{'data':data})

def blogdetails(re):
    return render(re,'blog-details.html')
def blog(re):
    return render(re,'blog.html')
def admin(re):
    return render(re,'admin.html')

def login(re):
    if re.method == 'POST':
        u = re.POST['username']
        p = re.POST['password']
        try:
            data = reguser.objects.get(username=u)
            if data.password == p:
                re.session['user'] = u
                return redirect(home)
            else:
                messages.add_message(re, messages.INFO, "password incorrect")
                return redirect(login)
        except Exception:
            if u == 'admin' and p == 'admin':
                # re.session['id1']=u
                return redirect(admin)
            else:
                messages.info(re, 'invaid username')
                return redirect(login)
            # messages.add_message(re, messages.INFO, "user incorrect")
            # return redirect(login)

    else:
        return render(re, 'login.html')

    # return render(re, 'login.html')


def regguser(request):
    if request.method == 'POST':
        a = request.POST['yourname']
        b = request.POST['username']
        c = request.POST['email']
        d = request.POST['password']
        e = request.POST['re-password']
        try:
            data = reguser.objects.create(yourname=a, username=b,email=c,password=d,repassword=e)
            data.save()

            messages.success(request, "registration success")
            return redirect(login)
        except:
            messages.success(request, "username already exist")
            return render(request, 'reguser.html')


    else:
        return render(request, 'reguser.html')
def shoplogin(re):

    if re.method == 'POST':
        u = re.POST['shopname']
        p = re.POST['password']
        print(u,p)
        try:
            data = regshop.objects.get(shopname=u)
            # print(data)
            # print(data.password)
            if data.password == p:
                if data.status==False:
                  re.session['shop'] = u
                  messages.success(re, "login success")

                  return redirect(shophome)
                else:
                    messages.error(re, "waiting for approval")
                    return redirect(shoplogin)

            else:
                messages.add_message(re, messages.INFO, "password incorrect")
                return redirect(shoplogin)
        except Exception:
            if u == 'admin' and p == 'admin':
                # re.session['id1']=u
                return redirect(admin)
            else:
                messages.info(re, 'invaid shopname')
                return redirect(shoplogin)
            # messages.add_message(re, messages.INFO, "user incorrect")
            # return redirect(login)

    else:
        return render(re,'shoplogin.html')
def reggshop(request):
    if request.method == 'POST':
        f = request.FILES['profile']
        a = request.POST['ownername']
        b = request.POST['shopname']
        c = request.POST['email']
        d = request.POST['password']
        ee= request.POST['re_password']
        try:
            # if regshop.objects.status=="approved":

            data = regshop.objects.create(profile=f,ownername=a, shopname=b, email=c, password=d, re_password=ee)
            data.save()

            messages.success(request, "registration success")
            return redirect(shoplogin)

        except:
            messages.success(request, "shop already exist")
            return redirect(reggshop)
    else:
        return render(request, 'regshop.html')
def shophome(re):
    # data = re.session['id']
    # data = regshop.objects.all()
    if 'shop' in re.session:
        data = regshop.objects.get(shopname=re.session['shop'])
        return render(re,'shophome.html',{'data':data} )
def addproducts(re):
    if re.method == 'POST':
        product_id = re.POST['product_id']
        product_name = re.POST['product_name']
        price = re.POST['price']
        stock = re.POST['stock']
        image = re.FILES['image']
        category=re.POST['category']
        user = regshop.objects.get(shopname=re.session['shop'])
        data = additem.objects.create(product_id=product_id, product_name=product_name, price=price, stock=stock, image=image,category=category,shopname=user)
        data.save()
        return render(re,'addproduct.html')
    else:
        return render(re, 'addproduct.html')


def itemdisplay(re):
    data=additem.objects.all()
    return render(re,'itemdisplay.html',{'data':data})
def edititem(re,id1):
    if re.method=='POST':
        a=re.POST['product_id']
        b=re.POST['product_name']
        c=re.POST['price']
        d=re.POST['stock']
        additem.objects.filter(pk=id1).update(product_id=a, product_name=b, price=c, stock=d)
        try:
            e = re.FILES['image']
            data=additem.objects.get(pk=id1)
            data.image=e
            data.save()
        except:
            additem.objects.filter(pk=id1).update(product_id=a, product_name=b, price=c, stock=d)
        return redirect(displayproduct)
        # return HttpResponse('data update')
    else:
        data=additem.objects.get(pk=id1)
        return render(re,'edititem.html',{'data':data})

def deleteitem(re,id1):
    data=additem.objects.filter(pk=id1)
    data.delete()
    return redirect(displayproduct)
def displayproduct(re):
    # data=additem.objects.all ()
    # if 'shop' in re.session:
        # data=regshop.objects.filter(shopname=regshop.objects.get(shopname=re.session['id']))
        user=regshop.objects.get(shopname=re.session['shop'])
        data=additem.objects.filter(shopname=user)


        return render(re,'displayproduct.html',{'data':data})
def addcart(re,product_name):
    if 'user' in re.session:
        u=reguser.objects.get(username=re.session['user'])
        # print('#'*100)
        print(u)
        item=additem.objects.get(pk=product_name)
        print(item)
        data=cart( product_name=item,username=u,total_price=item.price)
        data.save()
        # crt=cart.objects.filter(username=u)
        # return render(re, 'shoping-cart.html', {'crt': crt})
        # messages.success(re.'cart added sucessfully')

        return redirect(re.META.get('HTTP_REFERER', 'products/<id>'))


def checkout(re,id):
    data = additem.objects.filter(pk=id)
    print(data)
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    return render(re,'checkout.html',{'data':data})
    return redirect(re.META.get('HTTP_REFERER', 'products/<id>'))


def checkout1(re,id):
    cartitems= cart.objects.filter(pk=id)
    print(cartitems)
    amount = 5000
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    return render(re,'checkout.html',{'cartitems':cartitems})
def displaycart(re):
    if 'user' in re.session:
        u = reguser.objects.get  (username=re.session['user'])
        # print('#'*100)
        cartitems=cart.objects.filter(username=u)
        print(cartitems)
        amt=cart.objects.filter(username=u).count()
        total=0
        for i in cartitems:
            total+=i.product_name.price*i.quantity
        return render(re,"displaycart.html",{'cartitems':cartitems,'amt':amt,'total':total})
    else:
        return render(shops)
def remove(re,id):
    data = cart.objects.filter(pk=id)
    print("cart remove",data)
    data.delete()
    return redirect(displaycart)

# def add_to_cart(request, product_id):
#     product =additem.objects.get(id=product_id)
#
#     # Check if the item is already in the cart
#     existing_item = cart.objects.filter(product=product).first()
#
#     if existing_item:
#         existing_item.quantity += 1
#         existing_item.save()
#     else:
#         cart.objects.create(product=product, quantity=1)
#
#     return redirect('product_list')
#
# def view_cart(request):
#     cart_items = cart.objects.all()
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
# def displaycart(re):
#     cartitems=cart.objects.all()
#     return render(re,"displaycart",{'cartitems':cartitems})
def crttotal(re):
    if 'user' in re.session:
        u = reguser.objects.get  (username=re.session['user'])
        amt=cart.objects.filter(username=u)
        total=0
        for i in amt:
             price=i.product_name.price
             print(price)
             total+=price



        return render(re, "crttotal.html", {'amt':amt})

def increment_quantity(re,id):
    if 'user' in re.session:
        cartitems = cart.objects.get(pk=id)
        if cartitems.product_name.stock > 1:
            cartitems.quantity =cartitems.quantity + 1
            cartitems.total_price = cartitems.quantity * cartitems.product_name.price
            cartitems.save()
        return redirect (displaycart)
    else:
        return redirect(login)


def decrement_quantity(re,id):
    if 'user' in re.session:
        cartitems = cart.objects.get(pk=id)
        if cartitems.product_name.stock > 1:
            cartitems.quantity = cartitems.quantity - 1
            cartitems.total_price = cartitems.quantity * cartitems.product_name.price
            cartitems.save()
        return redirect(displaycart)
    else:
        return redirect(login)


def placeorder(re):
    print("in place")
    if 'user' in re.session:
        u = reguser.objects.get(username=re.session['user'])
        cartitems=cart.objects.filter(username=u)
        total = 0
        for i in cartitems:
            total+=i.product_name.price*i.quantity

        for i in cartitems:
            if i.quantity > i.product_name.stock:
                messages.info(re, f'Stock Limit Exceeded for {i.product_name.product_name}')
                return redirect(displaycart)
        amount = total * 100
        order_currency = 'INR'
        client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))

        return render(re, 'booking.html', {'cartitems': cartitems,'total':total,'amount':amount})

    else:
        return redirect(login)
def placeorder1(re):
    print("in place")
    if 'user' in re.session:
        u = reguser.objects.get(username=re.session['user'])
        cartitems=additem.objects.filter(username=u)
        total = 0
        for i in cartitems:
            total+=i.product_name.price*i.quantity

        for i in cartitems:
            if i.quantity > i.product_name.stock:
                messages.info(re, f'Stock Limit Exceeded for {i.product_name.product_name}')
                return redirect(displaycart)
        amount = total * 100
        order_currency = 'INR'
        client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))

        return render(re, 'booking.html', {'cartitems': cartitems,'total':total,'amount':amount})

    else:
        return redirect(login)

def message(re):
    messages.info(re, 'please login first')
    return redirect(index)

def success(re):
    if 'user' in re.session:
        user=reguser.objects.get(username=re.session['user'])
        items=cart.objects.filter(username=user)
        a=datetime.datetime.now().strftime("%Y-%m-%d")
        for i in items:
            item=additem.objects.get(pk=i.product_name.pk)
            data=order.objects.create(user=user,product=item,quantity=i.quantity,total_price=i.total_price,date=a)
            data.save()
            item.stock=item.stock-i.quantity
            item.save()
        cart.objects.all().delete()
        messages.success(re,'All cart items are booked')
        return redirect(shops)
    else: 
        return redirect(login)
def success1(re,id):
    if 'user' in re.session:
        user=reguser.objects.get(username=re.session['user'])
        items=additem.objects.get(pk=id)
        total=items.price
        a=datetime.datetime.now().strftime("%Y-%m-%d")
        data=order.objects.create(user=user,product=items,quantity=1,total_price=total,date=a)
        data.save()
        items.stock=items.stock-1
        items.save()
        messages.success(re,'All cart items are booked')
        return redirect(shops)
    else:
        return redirect(login)
def shoporders(re,id):
    if 'shop' in re.session:
        products = additem.objects.get(pk=id)
        bookings = order.objects.filter(product=products)
        return render(re, 'shoporders.html', {'bookings': bookings})
    else:
        return redirect(login)
def userorders(re):
    if 'user' in re.session:
        user = reguser.objects.get(username=re.session['user'])
        data = order.objects.filter(user=user)
        return render(re,'userorders.html',{'data':data})
    else:
        return redirect(login)

def logout(re):
    re.session.flush()
    return redirect(index)
def products(re,id):
    if 'user' in re.session:
        user = regshop.objects.get(pk=id)
        print(user,'isssi')
        data = additem.objects.filter(shopname=user)
        return render(re, 'products.html', {'data': data})
    else:
        return redirect(products)

def viewshop(re):
    data=regshop.objects.all()
    return render(re,'viewshop.html',{'data':data})
def viewuser(re):
    data=reguser.objects.all()
    return render(re,'viewuser.html',{'data':data})
def viewitem(re):
    data=additem.objects.all()
    return render(re,'viewitem.html',{'data':data})

def approve(re,id):
    status=regshop.objects.filter(pk=id)
    for shop in status:
        shop.status=False
        shop.save()
        return redirect(viewshop)
    return redirect(login)
def reject(re,id):
    status = regshop.objects.filter(pk=id)
    for shop in status:
        shop.status = True
        shop.save()
        return redirect(viewshop)
    return redirect(login)

def Feedback(re,shopname):
    if re.method=='POST':
        feed=re.POST['feed']
        print(feed)
        user=reguser.objects.get(username=re.session['user'])
        print(user,id,"id")
        if 'user' in re.session:
            data=regshop.objects.get(shopname=shopname)
            print(data,"data")
            print(data,"hjjh")
            data2=feedback.objects.create(feed=feed,shop=data,user=user)
            data2.save()
            return redirect(shops)
    else:
        return redirect(home)
def getfeedback(re):
    print("@@@@@@@@@@@")
    print(re.session['shop'])
    data=regshop.objects.get(shopname=re.session['shop'])
    print(data)
    data2=feedback.objects.filter(shop=data)
    print(data2)
    return render(re,'feedback.html',{'data2':data2})

def viewfeedback(re):
    data=feedback.objects.all()
    return render(re,'viewfeedback.html',{'data':data})

def addfeedback(re,id):
    if re.method=='POST':
        feed=re.POST['feed']
        print(feed)
        user=reguser.objects.get(username=re.session['user'])
        print(user,id,"id")
        if 'user' in re.session:
            data=regshop.objects.get(pk=id)
            print(data,"data")
            print(data,"hjjh")
            data2=feedback.objects.create(feed=feed,shop=data,user=user)
            data2.save()
            return redirect(shops)
    else:

        return render(re,'addfeedback.html')