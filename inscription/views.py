from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext

# Models Inscription
from inscription.models import Affiliate, Sections, Stages, Scout, Adult

# Django Forms
from .forms import AdultForm, ScoutForm

# Models accounts
from accounts.models import PersonalAccount


# Create your views here.
def add_affiliate(request):
    context = RequestContext(request)
    if request.method == 'POST':
        adulto = AdultForm(request.POST, request.FILES)
        scout = ScoutForm(request.POST, request.FILES)
        if scout.is_valid():
            print "scout valido"
            scout.save()
            """image = Affiliate(pic = request.FILES['pic'])
            image.save()"""
        else:
            print "invalido "+ str(scout.errors)
        if adulto.is_valid():
            print "adulto valido"
            adulto.save()
        else:
            print "invalido "+ str(adulto.errors)
    adulto = AdultForm()
    scout = ScoutForm()
    sections = Sections.objects.all()
    stages = Stages.objects.all()
    return render(request, 'addAfiliado.html',
                            {'adulto':adulto, 'scout':scout, 'stages':stages,'sections':sections})

def admin_profile(request,afDni):
    context = RequestContext(request)
    affiliate = Affiliate.objects.get(dni=afDni)
    if request.user.myuser.rol == "ABM":
        return render(request, 'adminProfile.html',{'afiliado':affiliate})
    else:
        return redirect('/')
