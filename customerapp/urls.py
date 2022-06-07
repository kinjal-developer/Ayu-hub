"""aryuveda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include


from.import views
urlpatterns = [

# about
    path("about/", views.about, name="about"),
#     blog
    path("blog/", views.blog, name="blog"),
#     blog -single
    path("blog_single/", views.blog_single, name="blog_single"),
#     cart

    path("cart/", views.cart, name="cart"),
#     checkout
    path("checkout/", views.checkout, name="checkout"),
#     contact
    path("contact/", views.contact, name="contact"),
#     index
    path("", views.index, name="index"),
#     index2
    path("index2/", views.index2, name="index2"),
#     index3
    path("index3/", views.index3, name="index3"),
#     product-single
    path("product_single/", views.product_single, name="product_single"),
#     profile
    path("profile/", views.profile, name="profile"),
#     service
    path("service/", views.service, name="service"),
#     shop
    path("shop/", views.shop, name="shop"),

# registration

path("registration_page/", views.registration_page, name="registration_page"),

#
path("registration/", views.registration, name="registration"),


#login - page

path("login_page/", views.login_page, name="login_page"),

#login-evaluate
path("login_evaluate/", views.login_evaluate, name="login_evaluate"),

#logout
path("logout/", views.logout, name="logout"),

#forgot password
path("forgot_password/", views.forgot_password, name="forgot_password"),

#send otp

path("SEND_OTP/", views.SEND_OTP, name="SEND_OTP"),
path("reset/", views.reset, name="reset"),


#cartadd
path("cartadd/<int:pi>", views.cartadd, name="cartadd"),

#update cart
path("updatecart/<int:pid>", views.updatecart, name="updatecart"),

#delete data
path('delete_data/<int:dk>', views.delete_data, name='delete_data'),

#total
path('total/', views.total, name='total'),

#subtotal
# path('subtotal/', views.subtotal, name='subtotal'),

#checkoutpint
path('check_point/', views.check_point, name='check_point'),

#edit-data
path('edit_page/', views.edit_page, name='edit_page'),
path('edit_data/', views.edit_data, name='edit_data'),


#like product
path('fatchlike/<int:li>',views.fatchlike,name="fatchlike"),
path('likeitem/', views.likeitem, name='likeitem'),

]

