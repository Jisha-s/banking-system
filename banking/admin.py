from django.contrib import admin

# Register your models here.

from banking.models import User, Transaction, BankAccountType, UserBankAccount

admin.site.register(BankAccountType)
admin.site.register(User)
admin.site.register(UserBankAccount)
admin.site.register(Transaction)
