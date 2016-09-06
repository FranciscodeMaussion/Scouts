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
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        rol = request.POST['rolselect']
        new_user=User()
        new_user.username = username
        new_user.set_password(password)
        new_user.save()
        miuser = MyUser()
        miuser.user = new_user
        miuser.rol = rol
        miuser.save()
    return render(request, 'adminRegister.html',{user_types:'users'})
