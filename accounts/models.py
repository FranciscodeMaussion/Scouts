from __future__ import unicode_literals

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from django.core.validators import MinValueValidator
from django.db import models
from datetime import date

from datetime import datetime

class AccountStatus(models.Model):
    class Meta:
        verbose_name="Estado de Cuenta"
        verbose_name_plural="Estados de cuenta"

    name = models.CharField(u'Nombre del estado de cuenta', max_length=30, unique=True)
    start = models.DateField(u"Dia de creacion del estado de cuenta", auto_now_add=True)
    close = models.DateField(u"Dia de cierre del estado de cuenta", null=True, blank=True)
    wallet = models.OneToOneField('Wallet')


    def __str__(self):
        return self.name

    def close_account(self):
        self.close = date.today()
        self.save()
        return True

    def get_account_balance(self):
        if self.close != None:
            account_transactions = Transactions.objects.filter(destination=self.wallet)
            account_balance = 0
            for the_transaction in account_transactions:
                account_balance += the_transaction.amount
            return account_balance
        else:
            return False

class Wallet(models.Model):
    class Meta:
        verbose_name="Cuenta"
        verbose_name_plural="Cuentas"

    name = models.CharField(u'Nombre de la cuenta', max_length=30, unique=True)
    creation = models.DateField(u"Dia de creacion de la cuenta", auto_now_add=True)
    amount = models.DecimalField(u'Saldo actual de la cuenta', default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Transactions(models.Model):
    class Meta:
        verbose_name="Transaccion"
        verbose_name_plural="Transacciones"

    name = models.CharField(u'Nombre del movimiento', max_length=30)
    description = models.TextField(u'Descripcion del movimiento', max_length=150, blank=True)
    date = models.DateField(u"Dia que se efectuo el movimiento", auto_now_add=True)
    amount = models.DecimalField(u'Monto del dinero en movimiento', editable=False, max_digits=9, decimal_places=2)
    destination = models.ForeignKey('Wallet')

    def __str__(self):
        return self.name

class Event(models.Model):
    class Meta:
        verbose_name="Evento"
        verbose_name_plural="Eventos"

    name = models.CharField(u'Nombre del evento', max_length=30, unique=True)
    description = models.TextField(u'Descripcion del evento', max_length=150, blank=True)
    start = models.DateField(u"Dia de inicio del evento")
    close = models.DateField(u"Dia de cierre del evento", blank=True, null=True)

    def __str__(self):
        return self.name

class Items(models.Model):
    class Meta:
        verbose_name="Item"
        verbose_name_plural="Items"

    name = models.CharField(u'Nombre del Item', max_length=30)
    description = models.TextField(u'Descripcion del item', max_length=150, blank=True)
    cost = models.DecimalField(u'Costo del item', default=0, editable=False, max_digits=7, decimal_places=2)
    presupuesto = models.ForeignKey('Budget')
    quantity = models.PositiveIntegerField(u'Cantidad de items que se usan', default=0)

    def __str__(self):
        return self.name

class Budget(models.Model):
    class Meta:
        verbose_name="Presupuesto"
        verbose_name_plural="Presupuestos"

    name = models.CharField(u'Nombre del presupuesto', max_length=30)
    description = models.TextField(u'Descripcion del Presupuesto', max_length=150, blank=True)
    event = models.OneToOneField('Event')

    def __str__(self):
        return self.name


    def aplicar_gasto_transaccion(budget_transaction):
        account_status = AccountStatus.objects.get(name = budget_transaction.event.name + "_" + budget_transaction.event.start )
        all_items = Item.objects.filter(budget =budget_transaccion.id)
        for item in all_items:
            suma_items = all_items.cost[item] * all_items.quantity[item]
            costo_total += suma_items
        transaction = Transactions()
        transaction.wallet = account_status.wallet
        transaction.description = "Gastos del evento " + budget_transaction.event.name + " de " + budget_transaction.event.start
        transaction.amount = costo_total
        transaction.date = date.today()
        transaccion.save()



class Sale(models.Model):
    class Meta:
        verbose_name="Venta"
        verbose_name_plural="Ventas"

    name = models.CharField(u'Nombre de la venta', max_length=50)
    seller = models.OneToOneField('PersonalAccount')
    event = models.OneToOneField('Event')
    transaction = models.OneToOneField('Transactions')
    amount = models.DecimalField(u'Monto de la venta', default=0.01, max_digits=7, decimal_places=2, validators=[MinValueValidator(0.01)])
    quantity = models.PositiveIntegerField(u'Cantidad de items que se vendieron', default=0)

    def __str__(self):
        return self.name

class PersonalAccount(models.Model):
    class Meta:
        verbose_name="Cuenta Personal"
        verbose_name_plural="Cuentas Personales"

    name = models.CharField(u'Nombre de la Cuenta', max_length=50)
    start = models.DateField(u"Dia de creacion de la cuenta", auto_now_add=True)
    amount = models.DecimalField(u'Saldo actual de la cuenta', default=0, max_digits=7, decimal_places=2)
    inscription = models.BooleanField(u'Pago inscripcion?', default=False)

    def __str__(self):
        return self.name

# Aca las signals
@receiver(pre_save, sender=Event)
def create_account_status_for_event(sender, instance, **kwargs):
    account = AccountStatus()
    account.name = instance.name + "_" + str(instance.start)
    account.start = instance.start
    account.close = instance.close
    account.save()

@receiver(pre_save, sender=AccountStatus)
def create_wallet_for_account_status(sender, instance, **kwargs):
    if instance._state.adding:
        wallet = Wallet()
        wallet.creation = instance.start
        wallet.name = instance.name + "_wallet"
        wallet.save()
        instance.wallet = wallet
#signals
@receiver(pre_save, sender=Sale)
def create_transactions_for_sale(sender, instance, **kwargs):
    personal_account = instance.seller
    total = instance.amount * instance.quantity
    personal_account.amount += total
    transaction = Transactions()
    the_wallet = Wallet.objects.get(name = instance.event.name + "_" + str(instance.event.start) + "_wallet")
    print the_wallet
    transaction.destination = the_wallet
    transaction.description = instance.seller.name + " vendio " + str(instance.quantity) + " " + instance.name
    transaction.date = date.today()
    transaction.amount = total
    transaction.save()
    print transaction
    instance.transaction = transaction
    instance.seller.amount = instance.seller.amount + total

@receiver(post_save, sender=Transactions)
def apply_transactions_amount_for_wallet(sender, instance, **kwargs):
    instance.destination.amount += instance.amount
