from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse

# User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from inscription.models import Affiliate
from accounts.models import Event

# Admin = django User. Scout leader:

#Inicializacio
def view_index(request):
    context = RequestContext(request)
    return render(request, 'index.html')

# LogIn
def login_for_the_admin(request):
    context = RequestContext(request)
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(status=200)
            else:
                #return render(request, 'adminLogIn.html', context,status=201)
                return HttpResponse(status=201)
        else:
            #return render(request, 'adminLogIn.html', context,status=202)
            return HttpResponse(status=202)
    return render(request, 'adminLogIn.html')

# LogOut
def log_out(request):
    context = RequestContext(request)
    logout(request)
    return redirect('/')

# Register
def register_for_the_admin(request):
    context = RequestContext(request)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        new_user=User()
        new_user.username=username
        new_user.set_password(password)
        new_user.save()
    return render(request, 'adminRegister.html')

# Lista de afiliados para mostrar tabla completa
def affiliates_list(request):
    context = RequestContext(request)
    affiliate = Affiliate.objects.all()
    return render(request, 'affiliates_list.html',{'afiliados':affiliate})

# Perfil de afiliados
def affiliate_profile(request,afDni):
    context = RequestContext(request)
    affiliate = Affiliate.objects.get(dni=afDni)
    return render(request, 'profile.html',{'afiliado':affiliate})


#Template Eventos
def view_events(request):
    context = RequestContext(request)
    event = Event.objects.all()
    return render(request, 'template_eventos.html',{'events':event})
