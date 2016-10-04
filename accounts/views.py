from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse

# User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from administrator.models import MyUser
# Forms
from .forms import SaleForm, ItemForm, TransactionsForm
# Accounts imports
from accounts.models import Event, Budget, Items, AccountStatus, PersonalAccount, Transactions, Wallet, Sale
from inscription.models import Affiliate

# Create your views here.
def create_transaction(request):
    context = RequestContext(request)
    a = Wallet.objects.all()
    form = TransactionsForm()

    if request.method == 'POST':
        form = TransactionsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = TransactionsForm()
            return HttpResponse(status=200)
        else:
            print form
            return HttpResponse(status=201)
    else:
        form = TransactionsForm()

    """if request.method=='POST':
        wallet_to_modify = Wallet.objects.get(id=int(request.POST['fromselect']))
        transaction = Transactions()
        transaction.name = request.POST['name']
        transaction.descripcion = request.POST['descripcion']
        transaction.amount = request.POST['amount']
        transaction.destination = wallet_to_modify
        transaction.save()"""
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
        return HttpResponse(status=200)
    return render(request, 'events.html')

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
            return HttpResponse(status=200)
        else:
            print form
            return HttpResponse(status=201)
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

# Creacion del balance (cierre de cuenta)

def balances(request):
    accounts = AccountStatus.objects.all()
    if request.method=='POST':
        cuenta = request.POST['balances']
        account = AccountStatus.objects.get(id = int(cuenta))
        if account.close != None:
            mensaje = "La cuenta ya estaba cerrada"
        else:
            mensaje = "Se ha cerrado la cuenta"
        total_transactions = account.get_account_balance()
        positive_transactions = account.get_armado_de_balances_positivos()
        negative_transactions = account.get_armado_de_balances_negativos()
        total_positivo = account.get_total_de_balances_positivos()
        total_negativo = account.get_total_de_balances_negativos()
        return render(request,'transacciones.html',{'total_transactions':total_transactions,'positive_transactions':positive_transactions,      'negative_transactions':negative_transactions,'total_positivo':total_positivo,'total_negativo':total_negativo,'mensaje':mensaje})
    return render(request, 'balances.html',{'accounts':accounts})

# Creacion del item
def addItem(request):
    context = RequestContext(request)
    budget = Budget.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            print "valid"
            form.save()
            return HttpResponse(status=200)
        return HttpResponse(status=201)
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


def modify_account(wallet_id, wallet_name, amount):
    wallet_being_modified = getAccount(wallet_id, wallet_name)
    if wallet_being_modified != None:
        wallet_being_modified.amount = wallet_being_modified.amount + am
        wallet_being_modified.save()
        return True
    else:
        return False
