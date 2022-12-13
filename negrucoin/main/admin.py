from django.contrib import admin
from main.models import Client, MoneyTransfer, MoneySaleOffer, MoneyPurchase

admin.site.register(Client)
admin.site.register(MoneyTransfer)
admin.site.register(MoneySaleOffer)
admin.site.register(MoneyPurchase)
