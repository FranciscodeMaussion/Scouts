from django.contrib import admin

# Register your models here.
from inscription.models import Member, Sections, Stages

admin.site.register(Member)
admin.site.register(Sections)
admin.site.register(Stages)
