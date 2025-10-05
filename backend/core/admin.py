from django.contrib import admin
from .models import UserProfile, Investment, TaxRecord, Transaction,Portfolio

# Register your models here
admin.site.register([UserProfile,Investment,TaxRecord,Transaction,Portfolio])
