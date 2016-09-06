from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
# User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from administrator.models import MyUser
# Forms
from .forms import SaleForm, ItemForm
# Accounts imports
from accounts.models import Event, Budget, Items, AccountStatus, PersonalAccount, Transactions, Wallet, Sale
from inscription.models import Affiliate

# Create your views here.
def create_transaction(request):
    context = RequestContext(request)
    a = Wallet.objects.all()
    if request.method=='POST':
        wallet_to_modify = Wallet.objects.get(id=request.POST['toselect'])
        save_transaction(request.POST['name'],
                         request.POST['descripcion'],
                         request.POST['date'],
                         request.POST['amount'],
                         wallet_to_modify.id,
                         wallet_to_modify.name,
                        )
    return render(request, 'createTransaction.html',{'all_wallets':a})

# Creacion del evento
def new_event(request):
    context = RequestContext(request)
    if request.method=='POST':
        event = Event()
        event.name = request.POST['name']
        event.description = request.POST['description']
        event.start = request.POST['start']
        event.save()
    return redirect('/') #futuro template eventos ver

# Creacion de venta
def new_sale(request):
    context = RequestContext(request)
    affiliates = Affiliate.objects.all()
    events = Event.objects.all()
    form = SaleForm()

    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = SaleForm()
        else:
            print form
    else:
        form = SaleForm()
    return render(request, 'createVenta.html',{'events':events, 'affiliates':affiliates, 'form':form})

# Creacion del presupuesto
def new_budget(request):
    context = RequestContext(request)
    ev = Event.objects.all()
    if request.method=='POST':
        budget = Budget()
        budget.name = request.POST['name']
        budget.description = request.POST['description']
        budget.event =  Event.objects.get(id=request.POST['event'])
        budget.save()
        return redirect('/cuentas/crear_item/')
    return render(request, 'budget.html',{'events':ev})

# Creacion del item
def addItem(request):
    context = RequestContext(request)
    budget = Budget.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            print "valid"
            form.save()
    else:
        print "invalid"
        form = ItemForm()
    return render(request, 'createItems.html',
                                {'form':form, 'budget':budget})


def get_wallet(wallet_id, wallet_name):
    try:
        destination_wallet = Wallet.objects.get(id=wallet_id, name=wallet_name)
        return destination_wallet
    except Wallet.DoesNotExist:
        return "No se encontro ninguna cuenta con ese nombre y id"

def save_transaction(name, description, day, amount, destination, destination_name):
    destination_wallet = get_wallet(destination, destination_name)
    if destination_wallet != None:
        modified = modifyAccount(dest, destName, am, stat)
        if modified:
            moving_transaction = Transactions()
            moving_transaction.name = name
            moving_transaction.description = description
            moving_transaction.date = day
            moving_transaction.amount = amount
            moving_transaction.destination = destination_wallet
            moving_transaction.save()
            return True
        else:
            return False
    else:
        return False

def modify_account(wallet_id, wallet_name, amount):
    wallet_being_modified = getAccount(wallet_id, wallet_name)
    if wallet_being_modified != None:
        wallet_being_modified.amount = wallet_being_modified.amount + am
        wallet_being_modified.save()
        return True
    else:
        return False
