from __future__ import unicode_literals

from django.db import models
#from #accounts.models import Personal#Account

# Create your models here.
class Sections(models.Model):
    class Meta:
        verbose_name="Etapa Etaria"
        verbose_name_plural="Etapas Etarias"

    name = models.CharField(u'Name', max_length=10)
    def __str__(self):
        return self.name

class Stages(models.Model):
    class Meta:
        verbose_name="Rango"
        verbose_name_plural="Rangos"

    name = models.CharField(u'Name', max_length=15)
    def __str__(self):
        return self.name

class Member(models.Model):
    class Meta:
        verbose_name="Afiliado"
        verbose_name_plural="Afiliados"

    scout = models.BooleanField(u'Adulto', default=True) #Adult or Scout
    name = models.CharField(u'Name', max_length=15)
    lastname = models.CharField(u'Lastname', max_length=15)
    dni = models.CharField(u'Dni', max_length=10, primary_key=True)
    sex = models.CharField(u'Sexo', max_length=1)
    birthday = models.DateField()
    phone = models.CharField(u'Phone', max_length=15)
    adress = models.CharField(u'Adress', max_length=30)
    tutor = models.CharField(u'Tutor',blank=True, max_length=20) #Only Socut
    section = models.ForeignKey(Sections,null=True, blank=True) #Only Socut
    stage = models.ForeignKey(Stages,null=True, blank=True) #Only Socut
    pic = models.FileField(u'ScoutPic', upload_to= 'usuario', default='null', blank=True) #Only Socut
    email = models.CharField(u'Email', max_length=30)
    formation = models.CharField(u'Formation', max_length=30, blank=True) #Only Adult
    #account = models.ForeignKey(PersonalAcount)
    def __str__(self):
        return str(self.dni)
