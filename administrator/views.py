from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext

# User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from administrator.models import MyUser
from inscription.models import Affiliate
from accounts.models import Budget

# Create your views here.
user_types = (
    ("SUPERUSER", "Master"),
    ("ABM", "Administrador"),
    ("ACCOUNT", "Contador"),
)

# Register
def admin_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        rol = request.POST['rolselect']
        new_user=User()
        try:
            User.objects.get(username=username) #send toast ,status=202)
            messages = 'El usuario ya existe.'
        except User.DoesNotExist:
            new_user.username = username
            messages = 'Usuario '+username+' creado.'
        if messages != 'El usuario ya existe.':
            new_user.set_password(password)
            new_user.save()
            miuser = MyUser()
            miuser.user = new_user
            miuser.rol = rol
            miuser.save()
        return render(request, 'adminRegister.html',{'users':user_types, 'messages' : messages})
    return render(request, 'adminRegister.html',{'users':user_types, 'messages' : ''})

def admin_user_list(request):
    users = MyUser.objects.all()
    return render(request, 'adminUsers.html',{'users':users})

def the_user_profile(request, id_user):
    user = MyUser.objects.get(id = id_user)
    if request.method == 'POST':
        username = request.POST['usr']
        password = request.POST['pass']
        rol= request.POST['rolselect']
        user.rol = rol
        user.save()
        user = user.user
        users = MyUser.objects.all()
        if username != user.username:
            try:
                user = User.objects.get(username=username) #send toast
                return render(request, 'sectionAdminUser.html',{'users':users})
            except User.DoesNotExist:
                user.username = username
        if password != '':
            user.set_password(password)
        user.save()
        return render(request, 'sectionAdminUser.html',{'users':users})
    return render(request, 'theUser.html',{'user':user})
