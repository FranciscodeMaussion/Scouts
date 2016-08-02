from django.contrib import admin
from accounts.models import Account, Movement, Event, Items, Budget, Sale, PersonalAccount

admin.site.register(Account)
admin.site.register(Movement)
admin.site.register(Event)
admin.site.register(Items)
admin.site.register(Budget)
admin.site.register(Sale)
admin.site.register(PersonalAccount)
