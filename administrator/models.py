from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

# Create your models here.

user_types = (
    ("GUEST", "Invitado"),
    ("SUPERUSER", "Master"),
    ("ABM", "Administrador"),
    ("ACCOUNT", "Contador"),
)

class MyUser(models.Model):
    rol = models.CharField(max_length=9,
                      choices=user_types,
                      default="GUEST")
    user = models.OneToOneField(User, unique=True)
