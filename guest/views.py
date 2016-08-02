from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse

# User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from inscription.models import Member

# Admin = django User. Scout leader:

#Inicializacion

def inup(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)

# LogIn
def adminLogIn(request):
    context = RequestContext(request)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(status=200)
            else:
                #return render_to_response('adminLogIn.html', context,status=201)
                return HttpResponse(status=201)
        else:
            #return render_to_response('adminLogIn.html', context,status=202)
            return HttpResponse(status=202)
    return render_to_response('adminLogIn.html', context)

# LogOut
def adminLogOut(request):
    context = RequestContext(request)
    logout(request)
    return redirect('/')

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
    return render_to_response('adminRegister.html',context)

# Cierra Admin

# Lista de afiliados para mostrar tabla completa
def affiliatesList(request):
    context = RequestContext(request)
    affiliate = Member.objects.all()
    return render_to_response('affiliates_list.html',{'afiliados':affiliate}, context)

def profile(request,afDni):
    context = RequestContext(request)
    affiliate = Member.objects.get(dni=afDni)
    return render_to_response('profile.html',{'afiliado':affiliate}, context)


#Template Eventos

def eventos(request):
    context = RequestContext(request)
    return render_to_response('template_eventos.html', context)
