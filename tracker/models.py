from django.db import models

# Create your models here.
class CurrentBalance(models.Model):
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.balance

class TransactionHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    amount = models.FloatField()
    on_delete = models.BooleanField(default=False)
    expense_type = models.CharField(choices=(('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')), max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expense_type


