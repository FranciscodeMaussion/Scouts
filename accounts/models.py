from __future__ import unicode_literals

from django.db import models
from inscription.models import Member

class Account(models.Model):
    class Meta:
        verbose_name="Cuenta"
        verbose_name_plural="Cuentas"

    name = models.CharField(u'Nombre de la cuenta', max_length=30)
    start = models.DateTimeField(u"Dia de creacion de la cuenta", auto_now_add=True)
    close = models.DateTimeField(u"Dia de cierre de la cuenta", null=True, blank=True)
    wallet = models.DecimalField(u'Saldo actual de la cuenta', default=0, max_digits=8, decimal_places=2)


    def __str__(self):
        return self.name

class Movement(models.Model):
    class Meta:
        verbose_name="Movimiento"
        verbose_name_plural="Movimientos"

    name = models.CharField(u'Nombre del movimiento', max_length=30)
    description = models.TextField(u'Descripcion del movimiento', max_length=150, blank=True)
    date = models.DateTimeField(u"Dia que se efectuo el movimiento", auto_now_add=True)
    amount = models.DecimalField(u'Monto del dinero en movimiento', default=0, editable=False, max_digits=8, decimal_places=2)
    status = models.BooleanField(u'Tipo de movimiento', editable=False)
    destination = models.ForeignKey('Account')

    def __str__(self):
        return self.name

class Event(models.Model):
    class Meta:
        verbose_name="Evento"
        verbose_name_plural="Eventos"

    name = models.CharField(u'Nombre del evento', max_length=30)
    description = models.TextField(u'Descripcion del evento', max_length=150, blank=True)
    start = models.DateTimeField(u"Dia y hora de inicio del evento")
    close = models.DateTimeField(u"Dia y hora de cierre del evento", blank=True, null=True)

    def __str__(self):
        return self.name

#@connectar(Event, 'creation')
#def create_account_for_event(instance_created, event):
#    Account.objects.create(dfsdfsdf)

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

class Sale(models.Model):
    class Meta:
        verbose_name="Venta"
        verbose_name_plural="Ventas"

    name = models.CharField(u'Nombre de la venta', max_length=50)
    seller = models.ForeignKey(Member)
    event = models.OneToOneField('Event')
    quantity = models.PositiveIntegerField(u'Cantidad de items que se vendieron', default=0)

    def __str__(self):
        return self.name

class PersonalAccount(models.Model):
    class Meta:
        verbose_name="Cuenta Personal"
        verbose_name_plural="Cuentas Personales"

    name = models.CharField(u'Nombre de la Cuenta', max_length=50)
    start = models.DateTimeField(u"Dia de creacion de la cuenta", auto_now_add=True)
    wallet = models.DecimalField(u'Saldo actual de la cuenta', default=0, max_digits=7, decimal_places=2)
    inscription = models.BooleanField(u'Pago inscripcion?', default=False)

    def __str__(self):
        return self.name
