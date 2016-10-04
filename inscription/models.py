from __future__ import unicode_literals

from datetime import datetime

from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.db import models
from accounts.models import PersonalAccount

# Hacerlo unico al evento y account status (name)
class Sections(models.Model):
    class Meta:
        verbose_name="Rango"
        verbose_name_plural="Rangos"

    name = models.CharField(u'Name', max_length=10)
    def __str__(self):
        return self.name

class Stages(models.Model):
    class Meta:
        verbose_name="Etapa Etaria"
        verbose_name_plural="Etapa Etarias"

    name = models.CharField(u'Name', max_length=15)
    def __str__(self):
        return self.name

#diccionario de los tipos de generos disponibles
gender_type = (
    ("MASC","Masculino"),
    ("FEM","Femenino"),
)
class Affiliate(models.Model):
    class Meta:
        ordering=['dni']
        verbose_name="Afiliado"
        verbose_name_plural="Afiliados"

    name = models.CharField(u'Name', max_length=45)
    dni = models.CharField(u'Dni', max_length=10, primary_key=True)
    birthday = models.DateField()
    gender = models.CharField(u'Genero del afiliado', max_length=15, choices=gender_type, default="MASC")
    phone = models.CharField(u'Phone', max_length=15)
    adress = models.CharField(u'Adress', max_length=30)
    email = models.CharField(u'Email', max_length=30)

    def __str__(self):
        return self.dni + " - " + self.name

class Scout(Affiliate):
    class Meta:
        verbose_name="Scout"
        verbose_name_plural="Scouts"

    tutor = models.CharField(u'Tutor',blank=True, max_length=20) #Only Socut
    section = models.ForeignKey(Sections,null=True, blank=True) #Only Socut
    stage = models.ForeignKey(Stages,null=True, blank=True) #Only Socut
    picture = models.FileField(u'ScoutPic', upload_to= 'usuario', default='null', blank=True) #Only Socut
    account = models.OneToOneField(PersonalAccount)

class Adult(Affiliate):
    class Meta:
        verbose_name="Adulto"
        verbose_name_plural="Adultos"

    formation = models.CharField(u'Formation', max_length=30, blank=True) #Only Adult
    def __str__(self):
        return str(self.dni)


#signals
@receiver(pre_save, sender=Scout)
def create_personal_account(sender, instance, **kwargs):
    if instance._state.adding:
        personal_account = PersonalAccount()
        personal_account.name = instance.dni
        personal_account.open = datetime.now()
        personal_account.inscription = False
        personal_account.save()
        instance.account = personal_account
