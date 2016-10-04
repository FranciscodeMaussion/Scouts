from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse

# Models Inscription
from inscription.models import Affiliate, Sections, Stages, Scout, Adult

# Django Forms
from .forms import AdultForm, ScoutForm

# Models accounts
from accounts.models import PersonalAccount


# Create your views here.
def add_affiliate(request):
    if request.method == 'POST':
        scout = ScoutForm(request.POST, request.FILES)
        if scout.is_valid():
            scout.save()
            """image = Affiliate(pic = request.FILES['pic'])
            image.save()"""
            return HttpResponse(status=200)
        else:
            print scout
            print scout.errors
            return HttpResponse(status=202)
    else:
        adulto = AdultForm()
        scout = ScoutForm()
    sections = Sections.objects.all()
    stages = Stages.objects.all()
    return render(request, 'addAfiliado.html',
                            {'adulto':adulto, 'scout':scout, 'stages':stages,'sections':sections})

def add_adulto(request):
    adulto = AdultForm(request.POST, request.FILES)
    if adulto.is_valid():
        adulto.save()
        return HttpResponse(status=201)
    return HttpResponse(status=202)

def admin_profile(request,afDni):
    affiliate = Affiliate.objects.get(dni=afDni)
    if request.user.myuser.rol == "ABM":
        return render(request, 'profile.html',{'afiliado':affiliate})
    else:
        return redirect('/')

# Lista de afiliados para mostrar tabla completa
def affiliates_list(request):
    affiliate = Affiliate.objects.all()
    if request.user.myuser.rol == "ABM":
        return render(request, 'affiliates_list.html',{'afiliados':affiliate})
    else:
        return redirect('/')
