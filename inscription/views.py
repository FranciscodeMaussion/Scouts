from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext

# Models Inscription
from inscription.models import Member, Sections, Stages

# Django Forms
from .forms import Members

# Models accounts
from accounts.models import PersonalAccount


# Create your views here.
def addAfiliado(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = Members(request.POST, request.FILES)
        if form.is_valid():
            """image = Member(pic = request.FILES['pic'])
            image.save()"""
            form.save()
            form = Members()
            mem = Member.objects.last()
            pa = PersonalAccount()
            pa.name = mem.name+"_"+mem.pk
            pa.save()
    else:
        form = Members()
        """member = Member()
        section = Sections.objects.get(name=request.POST['section'])
        stage = Stages.objects.get(name=request.POST['stage'])
        if request.POST['scout'] == "false" :
            #si es Scout
            member.pic = request.POST['pic']
            member.section = section
            member.stage = stage
            member.tutor = request.POST['tutor']
            member.scout = False
        else:
            #si es Adulto
            member.scout = True
            member.formation = request.POST['formation']
        member.name = request.POST['name']
        member.lastname = request.POST['last_name']
        member.dni = request.POST['dni']
        member.birthday = request.POST['birthday']
        member.phone = request.POST['phone']
        member.adress = request.POST['adress']
        member.email = request.POST['email']
        member.save()
        return render_to_response('addAfiliado.html',
                              context)
    else:
        section = Sections.objects.all()
        stage = Stages.objects.all()"""
    return render_to_response('addAfiliado.html',
                                {'form':form},
                                context)
