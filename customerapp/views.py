from django.shortcuts import render
from.models import *
from django.core.mail import send_mail
from random import randint
from .utils import sendmail

# Create your views here.

# about
def about(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'customerapp/about.html',{'uid': uid})
    else:
        return render(request,"customerapp/about.html")

#     blog
def blog(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'customerapp/blog.html', {'uid': uid})
    else:
        return render(request, "customerapp/blog.html")


#     blog -single


def blog_single (request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'customerapp/blog-single.html', {'uid': uid})
    else:
        return render(request, "customerapp/blog-single.html")



#     cart
def cart(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        c1id = Cartitem.objects.all()
        pid=Product.objects.all()

        # for i in c1id:
        #     ccid=Cartitem.objects.get(product_id=i.id)
        #     ppid=Product.objects.get(name=ccid.name)
        #     ddki=ppid.itemimage
        #     ccid.itemimage=ddki
        #     ccid.save()
        cid = Cartitem.objects.all()


        return render(request, 'customerapp/cart.html', {'uid': uid,'cid':cid})
    else:
        return render(request,"customerapp/cart.html")



#
def cartadd(request,pi):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        email = request.session['email']
        # uid = User.objects.get(email=email)
        pid = Product.objects.get(id=pi)
        data = Product.objects.all()

        cid = Cartitem.objects.create(user_id=uid,product_id=pid, name=pid.name, price=pid.price,itemimage=pid.itemimage)
        return render(request, "customerapp/shop.html",{'uid':uid,'data':data})
    else:
        return render(request, "customerapp/shop.html")

#updatecart
def updatecart(request,pid):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        bid=Cartitem.objects.get(id=pid)
        number = request.POST['number']
        bid.number=number
        subtotal = float(number) * float(bid.price)
        bid.subtotal=subtotal
        bid.save()
        cid = Cartitem.objects.all()
        return render(request, 'customerapp/cart.html', {'uid': uid, 'cid': cid})
    else:
        return render(request, "customerapp/cart.html")


# sub total
def total(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        total = 0
        bid = Cartitem.objects.all()

        total1=0
        for i in bid:
            total1=total1 + i.subtotal

        for i in bid:
            i.total=total1
            i.save()

        # for the grand total

        for i in bid:
            i.grandtotal=int(i.total+20+(i.total * 18/100))
            i.save()

        dik=Cartitem.objects.all()
        ck=0
        for i in dik:
            print("id",i.id)
            st=i.total
            ck=i.grandtotal
            break
        # data=Cartitem.objects.subtotal()
        # total=0
        # for i in data:
        #     total=total+i.subtotal
        # data.total=total
        # data.save()
        cid = Cartitem.objects.all()
        return render(request, 'customerapp/cart.html', {'uid': uid, 'cid': cid,'ck':ck,'st':st})
    else:
        return render(request, "customerapp/cart.html")


# #subtotal
# def total(request):
#     if 'email' in request.session:
#         uid = User.objects.get(email=request.session['email'])
#         cid1=Cartitem.objects.all()
#         cid1 = Cartitem.objects.all()
#
#         cid = Cartitem.objects.all()
#         return render(request, 'customerapp/cart.html', {'uid': uid, 'cid': cid})
#     else:
#         return render(request, "customerapp/cart.html")
#

#delete cart item
def delete_data(request,dk):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        data1=Cartitem.objects.get(id=dk)
        data1.delete()
        cid=Cartitem.objects.all()
        print(" data :",cid)
        return render(request, "customerapp/cart.html",{'cid':cid,'uid':uid})
    else:
        return render(request, "customerapp/cart.html")


#     check out
def checkout(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid = Cartitem.objects.all()
        # print("dipen", cid)
        dik = Cartitem.objects.all()
        ck = 0
        for i in dik:
            print("id", i.id)
            ck = i.grandtotal
            # gt=i.grandtotal
            break
        print("dipen", ck)
        return render(request, 'customerapp/checkout.html', {'uid': uid, 'cid': cid, 'ck': ck})
    else:
        return render(request, "customerapp/checkout.html")

#     contact
def contact(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'customerapp/contact.html', {'uid': uid})
    else:
        return render(request, "customerapp/contact.html")

# index

def index(request):
    try:
        if 'email' in request.session:
            uid = User.objects.get(email=request.session['email'])
            pid=Product.objects.all()
            return render(request, 'customerapp/index.html', {'uid': uid,'pid':pid})
        else:
            pid = Product.objects.all()
            return render(request,"customerapp/index.html",{'pid':pid})
    except:
        pid = Product.objects.all()
        return render(request, "customerapp/index.html",{'pid':pid})


#     index2
def index2(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        data = Product.objects.all()
        return render(request, 'customerapp/index2.html', {'uid': uid ,'data':data})
    else:
        return render(request, "customerapp/index2.html")
#     index3
def index3(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        data = Product.objects.all()
        return render(request, 'customerapp/index3.html', {'uid': uid,'data':data})
    else:
        return render(request, "customerapp/index3.html")
#     product -single
def product_single (request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'customerapp/product-single.html', {'uid': uid})
    else:
        return render(request, "customerapp/product-single.html")
#     profile
def profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        ccid=Customer.objects.get(user_id=uid)
        aid=Address.objects.get(user_id=uid)
        print("dipen",aid)
        print("dipn",ccid.profile_pic.url)

        return render(request, 'customerapp/profile.html', {'uid': uid,'ccid':ccid,'aid':aid})
    else:
        return render(request, "customerapp/profile.html")
#     setrvice
def service(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'customerapp/service.html', {'uid': uid})
    else:
        return render(request, "customerapp/service.html")
#     shop def index(request):
def shop(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        data = Product.objects.all()
        cc1 = Product.objects.all().count()
        print("dipen", cc1)
        return render(request, 'customerapp/shop.html', {'uid': uid,'data':data,'cc1':cc1})
    else:
        data = Product.objects.all()
        cc1 = Product.objects.all().count()
        print("dipen", cc1)
        return render(request, 'customerapp/shop.html', {'data': data, 'cc1': cc1})





                     # registration_page detail

#     registration page:
def registration_page(request):
    return render(request,"customerapp/registration.html")

#registration
def registration(request):
    role = request.POST['role']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    e_mail = request.POST['email']
    p_ss = request.POST['password']
    uid = User.objects.create(firstname=firstname,lastname=lastname, email=e_mail, password=p_ss, role=role)
    if uid:
        k = "success"
        if role == "admin":
             sid = Admin.objects.create(firstname=firstname,lastname=lastname, email=e_mail, password=p_ss, user_id=uid)
             send_mail("conformation-message", "wel come to school", "dipenpatel898065@gmail.com", [e_mail])
             return render(request,'customerapp/login.html', {'key': k})
        elif role == "customer":
            cid = Customer.objects.create(firstname=firstname,lastname=lastname, email=e_mail, password=p_ss, user_id=uid)
            aid=Address.objects.create(user_id=uid,fullname=firstname)
            send_mail("conformation-message", "wel come to school", "dipenpatel898065@gmail.com", [e_mail])
            return render(request, 'customerapp/login.html', {'key': k})
        else:
            k = "unsucess"
            return render(request, 'customerapp/registration.html', {'key': k})

    else:
        k = "unsucess"
        return render(request, 'customerapp/registration.html', {'key': k})



 # login page
def login_page(request):
    return render(request,"customerapp/login.html")

# login-evaluate
def login_evaluate(request):
    role = request.POST['role']
    p_assword = request.POST['password']
    email = request.POST['email']
    uid = User.objects.get(email=email)
    if uid:
        if uid.role == "admin":
            aid = Admin.objects.get(user_id=uid)
            request.session['firstname'] = aid.firstname
            request.session['email'] = uid.email
            request.session['id'] = uid.id
            # print("-doctor ", aid.profile_pic)
            context = {
                'uid': uid,
                'aid': aid,
            }
            # print("----------------> context:",context.did.profile_pic.url)
            return render(request, "adminpanel/examples/tables.html", {'context': context, 'aid': aid})
        elif role == "customer":
            cid = Customer.objects.get(user_id=uid)
            request.session['firstname'] = cid.firstname
            request.session['email'] = uid.email
            request.session['id'] = uid.id
            context = {
                'uid': uid,
                'cid': cid
            }
            return render(request, "customerapp/index.html", {'context': context, 'cid': cid,'uid':uid})
        else:
            return render(request,  "customerapp/login.html")

    else:
        return render(request,  "customerapp/login.html")


#logout
def logout(request):
    if "email" in request.session:
        del request.session['firstname']
        del request.session['email']
        del request.session['id']
        return render(request, "customerapp/login.html")
    else:
        return render(request, "customerapp/login.html")

#forgot password

def forgot_password(request):
    return render(request, "customerapp/forgot-password.html")


#send-otp


def SEND_OTP(request):
    try:
        email=request.POST['email']
        uid=User.objects.get(email=email)
        if uid:
            otp=randint(1111,9999)
            uid.otp=otp #update otp
            uid.save()
            if uid.role=="admin":
                aid=Admin.objects.get(user_id=uid)
                context={
                    'aid':aid,
                    'otp':otp
                }

                sendmail("Forgot Password", "mail_template", email, {'context': context})
                return render(request, "customerapp/reset_password.html",{'email':email})
            elif uid.role=="customer":
                aid = Customer.objects.get(user_id=uid)
                context = {
                    'aid': aid,
                    'otp': otp
                }

                sendmail("Forgot Password", "mail_template", email, {'context': context})
                return render(request, "customerapp/reset.html", {'email': email})
            else:
                return render(request, "customerapp/forgot-password.html")

    except:
        e_mass="user does not exit"
        return render(request, "customerapp/forgot-password.html",{'e_mass':e_mass})

def reset(request):
    email=request.POST['email']
    otp = request.POST['otp']
    newpassword = request.POST['newpassword']
    repassword = request.POST['repassword']
    uid=User.objects.get(email=email)
    if str(uid.otp)==otp and newpassword==repassword:
        uid.password=newpassword
        uid.save()
        s_mass="succesful save"
        return render(request, "customerapp/index.html",{'s_mass':s_mass})
    else:
        e_mass = "unsuccesful save"
        return render(request, "customerapp/forgot-password.html",{'e_mass':e_mass},{'email':email})

#checkoutpoint
def check_point(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        email = request.session['email']
        fullname=request.POST['fullname']
        mobile = request.POST['mobile']
        address= request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        id= Address.objects.create(fullname=fullname,user_id=uid,mobile=mobile,state=state,city=city,pincode=pincode,a_ddress2=address)
        if id:

            cid=Cartitem.objects.all()
            # piid=Product.objects.all()
            for i in cid:
                print("id1",i.product_id_id)
                piid=Product.objects.get(id=i.product_id_id)
                piid.sold=piid.sold +i.number
                piid.available=piid.available-piid.sold
                piid.save()

                # pid=Product.objects.get(id=y)

            dik = Cartitem.objects.all()
            ck = 0
            for i in dik:
                # print("id", i.id)
                ck = i.grandtotal
                break
            print("dipen", ck)
            context = {
                'uid': uid,
                'cid':cid,
                'ck':ck,
                       }
            sendmail("bill for purchase", "mail_template2", email, {'context': context})
            did = Cartitem.objects.all()
            did.delete()
            return render(request, 'customerapp/index.html', {'uid': uid,'cid':cid,'ck':ck})
        else:
            return render(request, "customerapp/checkout.html")
    else:
        return render(request, "customerapp/checkout.html")

#edit_data =
def edit_data(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        aid=Address.objects.get(user_id=uid)
        fullname = request.POST['firstname']
        a_ddress2 = request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        password = request.POST['password']
        profile_pic = request.POST['image']
        aid.fullname=fullname
        aid.a_ddress2 =a_ddress2
        aid.state = state
        aid.city = city
        aid.pincode = pincode
        uid.password = password
        cid.profile_pic = profile_pic
        aid.save()
        uid.save()
        cid.save()


        return render(request, 'customerapp/index.html', {'uid': uid})
    else:
        return render(request, "customerapp/edit-page.html")


#edit - page
def edit_page(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])

        return render(request,'customerapp/edit-data.html', {'uid': uid})
    else:
        return render(request,"customerapp/index.html")



#like items

def likeitem(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        liid=Likeproduct.objects.all()
        return render(request,"customerapp/likeproduct.html",{'uid':uid,'liid':liid})
    else:
        return render(request, "customerapp/likeproduct.html")


#fatch like items

def fatchlike(request,li):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        pid = Product.objects.get(id=li)
        lid=Likeproduct.objects.create(name=pid.name,price=pid.price,itemimage=pid.itemimage)
        data = Product.objects.all()
        return render(request,"customerapp/shop.html",{'uid':uid,'data':data})
    else:
        return render(request, "customerapp/shop.html")


