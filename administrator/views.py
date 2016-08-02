from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext

# User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from administrator.models import MyUser
from inscription.models import Member

# Create your views here.
user_types = (
    ("SUPERUSER", "Master"),
    ("ABM", "Administrador"),
    ("ACCOUNT", "Contador"),
)

#Template Administrador

def templateAdmin(request):
    context = RequestContext(request)
    return render_to_response('templateAdmin.html', context)


# Register
def adminRegister(request):
    context = RequestContext(request)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        n_u=User()
        n_u.username=username
        n_u.set_password(password)
        n_u.save()
        miuser = MyUser()
        miuser.user=n_u
        hola=request.POST['rolselect']
        print hola
        miuser.rol=hola
        miuser.save()
    return render_to_response('adminRegister.html',{user_types:'users'},context)

def adminProfile(request,afDni):
    context = RequestContext(request)
    affiliate = Member.objects.get(dni=afDni)
    if request.user.myuser.rol == "ABM":
        return render_to_response('adminProfile.html',{'afiliado':affiliate}, context)
    else:
        return redirect('/')
