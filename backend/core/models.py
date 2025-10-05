from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    Name = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.CharField
    contact = models.CharField(max_length=10)
    linked_Bank_Accounts = models.DecimalField(max_digits=20,decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)

class TaxRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    financial_year = models.CharField(max_length=10)  # e.g., 2024-25
    total_income = models.DecimalField(max_digits=12, decimal_places=2)
    total_tax_paid = models.DecimalField(max_digits=12, decimal_places=2)
    deductions = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax_due = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Tax Record ({self.financial_year}) - {self.user.username}"

class Transaction(models.Model):
    InvestmentId = models.CharField(max_length=100)
    Date = models.DateField
    Amount = models.DecimalField(max_digits=10,decimal_places=2)
    Mode = models.CharField( max_length=50)


class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_type = models.CharField(max_length=100)  # e.g., Mutual Fund, Stock, FD
    name = models.CharField(max_length=150)
    amount_invested = models.DecimalField(max_digits=12, decimal_places=2)
    current_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    date_invested = models.DateField(null=True, blank=True)
    maturity_date = models.DateField(null=True, blank=True)
    risk_level = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    def __str__(self):
        return f"{self.name} - {self.investment_type}"

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_investments = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_returns = models.DecimalField(max_digits=12, decimal_places=2, default=0)


