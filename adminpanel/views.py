from django.shortcuts import render
from customerapp.models import Customer,User,Product
from.models import *
# Create your views here.

def icons(request):
    return render(request,"adminpanel/examples/icons.html")
def rtl(request):
    return render(request,"adminpanel/adminpanel/examples/rtl.html")

def tables(request):
    pid=Product.objects.all()
    ccid=Customer.objects.all()
    # print("dipen",ccid.firstname)
    return render(request,"adminpanel/examples/tables.html",{'ccid':ccid,'pid':pid})

def map(request):
    return render(request,"adminpanel/examples/map.html")
def maps(request):
    return render(request,"adminpanel/examples/maps.html")
def notifications(request):
    return render(request,"adminpanel/examples/rtl.html")
def typography(request):
    return render(request,"adminpanel/examples/typography.html")
def upgrade(request):
    return render(request,"adminpanel/examples/upgrade.html")
def user(request):
    return render(request,"adminpanel/examples/user.html")
def template(request):
    return render(request,"adminpanel/template.html")

def delete(request,dik):
    cid = Customer.objects.get(user_id=dik)
    cid.delete()
    pid = Product.objects.all()
    ccid = Customer.objects.all()
    return render(request,"adminpanel/examples/tables.html" ,{'ccid':ccid,'pid':pid})

def deleteproduct(request,dip):
    cid = Product.objects.get(id=dip)
    cid.delete()
    pid = Product.objects.all()
    ccid = Customer.objects.all()
    return render(request,"adminpanel/examples/tables.html" ,{'ccid':ccid,'pid':pid})

def add_product(request):
    name=request.POST['productname']
    price=request.POST['price']
    image=request.POST['image']
    available=request.POST['available']
    pnid=Product.objects.create(name=name, price=price, itemimage=image,available=available)
    pid = Product.objects.all()
    ccid = Customer.objects.all()
    return render(request,"adminpanel/examples/tables.html" ,{'ccid':ccid,'pid':pid})