from django.contrib import admin
# Register your models here.
from inscription.models import Affiliate, Sections, Stages, Scout, Adult

admin.site.register(Affiliate)
admin.site.register(Scout)
admin.site.register(Adult)
admin.site.register(Sections)
admin.site.register(Stages)
