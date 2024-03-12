"""
URL configuration for organic_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('home', views.home),
    path('shops', views.shops),
    path('contact', views.contact),
    path('shopdetails', views.shopdetails),
    path('shopgrid', views.shopgrid),
    path('addcart/<product_name>', views.addcart),
    path('checkout/<id>', views.checkout),
    path('checkout1/<id>', views.checkout1),
    path('blogdetails', views.blogdetails),
    path('blog', views.blog),
    path('login', views.login),
    path('logout', views.logout),
    path('regguser', views.regguser),
    path('adminn', views.admin),
    path('shoplogin', views.shoplogin),
    path('reggshop', views.reggshop),
    path('shophome', views.shophome),
    path('addproducts', views.addproducts),
    # path('addproduct', views.addproducts),
    path('itemdisplay', views.itemdisplay),
    path('edititem/<id1>', views.edititem),
    path('displayproduct', views.displayproduct),
    path('remove/<id>', views.remove),
    path('displaycart', views.displaycart),
    path('crttotal', views.crttotal),
    path('booking', views.placeorder),
    path('booking1', views.placeorder),
    path('success', views.success),
    path('success1/<id>', views.success1),
    path('shoporders/<id>',views.shoporders),
    path('userorders',views.userorders),
    path('message', views.message),
    path('viewshop', views.viewshop),
    path('viewuser', views.viewuser),
    path('viewitem', views.viewitem),
    path('products/<id>', views.products),
    path('approve/<id>', views.approve),
    path('reject/<id>', views.reject),
    path('feedback/<shopname>', views.Feedback),
    path('getfeedback', views.getfeedback),
    path('viewfeedback', views.viewfeedback),
    path('addfeedback/<int:id>', views.addfeedback),
    path('deleteitem/<id1>',views.deleteitem),
    path('cart/increment/<int:id>/', views.increment_quantity, name='increment_quantity'),
    path('cart/decrement/<int:id>/', views.decrement_quantity, name='decrement_quantity'),


]
