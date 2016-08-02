from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
# User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from administrator.models import MyUser

# Accounts imports
from accounts.models import Event, Budget, Items, Account, PersonalAccount, Movement

# Create your views here.
def createMovement(request):
    context = RequestContext(request)
    a = Account.objects.filter(close__isnull=True)
    if request.method=='POST':
        b = Account.objects.get(id=request.POST['toselect'])
        saveMovement(request.POST['name'], request.POST['descripcion'], request.POST['date'], request.POST['amount'], b.id, b.name, True)
    return render_to_response('createMovement.html',{'account':a}, context)

# Creacion del evento
def newEvent(request):
    context = RequestContext(request)
    if request.method=='POST':
        event = Event()
        event.name = request.POST['name']
        event.description = request.POST['description']
        event.start = request.POST['start']
        event.save()
        acc = Account()
        nom = event.name+"_"+str(event.id)
        acc.name = nom
        acc.start = event.start
        acc.wallet = 0
        acc.save()
    return redirect('/') #futuro template eventos ver

# Creacion del presupuesto
def newBudget(request):
    context = RequestContext(request)
    ev = Event.objects.all()
    if request.method=='POST':
        bud = Budget()
        bud.name = request.POST['name']
        bud.description = request.POST['description']
        bud.event =  Event.objects.get(id=request.POST['event'])
        bud.save()
        return redirect('/cuentas/crear_item/')
    return render_to_response('budget.html',{'events':ev}, context)

# Creacion del presupuesto
def newItem(request):
    context = RequestContext(request)
    bud = Budget.objects.last()
    if request.method=='POST':
        item = Items()
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.cost = request.POST['cost']
        item.presupuesto = bud
        item.quantity = request.POST['quantity']
        item.save()
    return render_to_response('items.html', context)

def getAccount(idAc, nameAc):
    try:
        account = Account.objects.get(id=idAc, name=nameAc)
    except Account.DoesNotExist:
        try:
            account = PersonalAccount.objects.get(id=idAc, name=nameAc)
        except PersonalAccount.DoesNotExist:
            account = None
    return account

def saveMovement(n, desc, d, am, dest, destName, stat):
    account = getAccount(dest, destName)
    if account != None:
        modified = modifyAccount(dest, destName, am, stat)
        if modified:
            movement = Movement()
            movement.name = n
            movement.description = desc
            movement.date = d
            movement.amount = am
            movement.status = stat
            movement.destination = account
            movement.save()
            return True
        else:
            return False
    else:
        return False

def modifyAccount(idAc, nameAc, am, stat):
    account = getAccount(idAc, nameAc)
    if account != None:
        if stat:
            account.wallet = account.wallet + am
            account.save()
        else:
            account.wallet = account.wallet - am
            account.save()
        return True
    else:
        return False
