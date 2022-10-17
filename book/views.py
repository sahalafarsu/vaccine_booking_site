
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from django.shortcuts import render, redirect, get_object_or_404
from .models import District, Center, People


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('booking')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)

            user.save();
            print('user created')
        else:
            # print('password not matched')
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('booking')
    return render(request, 'register.html')

def booking(request,d_slug=None):
    d_page=None
    centers_list=None
    if d_slug!=None:
        d_page=get_object_or_404(District,slug=d_slug)
        centers_list=Center.objects.all().filter(district=d_page,available=True)
    else:
        centers_list=Center.objects.all().filter(available=True)
    paginator=Paginator(centers_list,9)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        centers=paginator.page(page)
    except (EmptyPage,InvalidPage):
        centers=paginator.page(paginator.num_pages)
    return render(request,'about.html',{'district':d_page,'centers':centers})

def centDetail(request, d_slug, center_slug):
    try:
        center=Center.objects.get(district__slug=d_slug,slug=center_slug)
    except Exception as e:
        raise e
    return render(request,'blog.html',{'center':center})

# def bookingslot(request):
#     return render(request,'bookingslot.html')

def bookingslot(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        house_name = request.POST['house_name']
        city = request.POST['city']
        district = request.POST['district']
        pincode = request.POST['pincode']
        book = People.objects.create(first_name=first_name, last_name=last_name,birthday=birthday,
                                        gender=gender, email=email, phone=phone, house_name=house_name,
                                        city=city, district=district,pincode=pincode)
        book.save();
        print('user created')
        return redirect('success')
    return render(request, 'bookingslot.html')

def success(request):
    return render(request,'success.html')

