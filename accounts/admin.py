from django.contrib import admin
from accounts.models import AccountStatus, Transactions, Event, Items, Budget, Sale, PersonalAccount

admin.site.register(AccountStatus)
admin.site.register(Transactions)
admin.site.register(Event)
admin.site.register(Items)
admin.site.register(Budget)
admin.site.register(Sale)
admin.site.register(PersonalAccount)
