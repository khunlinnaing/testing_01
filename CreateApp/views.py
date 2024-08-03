from django.shortcuts import render, HttpResponse, redirect
from .models import UserInfo, Role
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        roles = Role.objects.all()
        user_info = UserInfo.objects.filter(user__in=users, role__in = roles)

        user_info_dict = {info.user_id: info for info in user_info}

        user_role_dict = {role.role_id: role for role in user_info}
        user_list = [
            {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone': user_info_dict.get(user.id).phone if user.id in user_info_dict else '',
                'address': user_info_dict.get(user.id).address if user.id in user_info_dict else '',
                'role': user_info_dict.get(user.id).role_id if user.id in user_info_dict else '',
                'role_value': user_role_dict.get(user.id).role_id if user.id in user_role_dict else '',
            }
            for user in users
        ]
        return render(request, 'index.html', {'users': user_list})
    else:
        return redirect('login')


def register(request):
    if request.method == 'POST':
        print('Hello world')
    else:
        return render(request, 'Auth/register.html')

def CustomLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('jjh')
    else:
        return render(request, 'Auth/login.html')

def CustomLogOut(request):
    logout(request)
    return redirect('/')