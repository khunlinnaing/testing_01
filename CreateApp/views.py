from django.shortcuts import render, HttpResponse, redirect
from .models import UserInfo, Role
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .validation import registervalidation

def index(request):
    if request.user.is_authenticated:
        user = User.objects.all()
        return render(request, 'index.html', {'datas': user})
    else:
        return render(request, 'index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            if len(registervalidation(request.POST)) != 0:
                return render(request, 'Auth/register.html',{'message': registervalidation(request.POST), 'status': 0})
            else:
                username = request.POST['firstname']+request.POST['lastname']
                email = request.POST['email']
                password1 = request.POST['password1']
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                address = request.POST['address']
                phone = request.POST['phone']
                birthday = request.POST['birthday']
                print(username)
                if 'photo' in request.FILES:
                    photo = request.FILES['photo']
                else:
                    photo = 'logo.png'
                if User.objects.filter(username=username).exists():
                    return render(request, 'Auth/register.html',{'message': 'Username already exists!', 'status': 0})

                if User.objects.filter(email=email).exists():
                    return render(request, 'Auth/register.html',{'message': 'Email already exists!', 'status': 0})

                if UserInfo.objects.filter(phone=phone).exists():
                    return render(request, 'Auth/register.html',{'message': 'Phone already exists!', 'status': 0})

                user = User.objects.create_user(username=username, email=email, password=password1, is_staff=True, first_name=firstname, last_name=lastname)
                user.save()
                UserInfo.objects.create(user=user, address=address, phone=phone, birthday=birthday, photo=photo, role_id=1)
                return render(request, 'Auth/register.html',{'message': 'Your account has been created!', 'status': 1})
        else:
            return render(request, 'Auth/register.html')
    

def CustomLogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to a success page.
            else:
                return render(request, 'Auth/login.html', {'message': 'username or password is invalid.'})
        else:
            return render(request, 'Auth/login.html')

def CustomLogOut(request):
    logout(request)
    return redirect('/')