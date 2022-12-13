from django.contrib import admin

from payment.models import QIWIBill, WithdrawalRequest, Payment

admin.site.register(QIWIBill)
admin.site.register(WithdrawalRequest)
admin.site.register(Payment)
