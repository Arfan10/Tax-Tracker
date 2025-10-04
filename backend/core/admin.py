from django.contrib import admin
from .models import UserProfile, Investment, TaxRecord, Transaction

# Register your models here
admin.site.register([UserProfile,Investment,TaxRecord,Transaction,])
