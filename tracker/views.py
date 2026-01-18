from django.shortcuts import render, redirect
from .models import CurrentBalance, TransactionHistory
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        current_balance = CurrentBalance.objects.get(id=1)
        desc = request.POST.get('desc')
        amount = float(request.POST.get('amount'))
        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)

        if amount == 0:
            messages.warning(request, 'Amount must not be Zero')
            return redirect('/')

        expense_type = 'CREDIT'
        if amount < 0:
            expense_type = 'DEBIT'
        
        TransactionHistory.objects.create(
            description = desc, 
            amount = amount, 
            expense_type = expense_type, 
            current_balance = current_balance
        )

        #updated Current balance
        current_balance.balance += amount
        current_balance.save()

        #Calculation Income vs Expenses
        
        messages.success(request, 'Transaction completed Successfully')
        return redirect('/')
    
    current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
    income,expense = 0,0

    for trans in TransactionHistory.objects.all():
            if trans.expense_type == "CREDIT":
                income += trans.amount
            else:
                expense += trans.amount
    expense = abs(expense)
    
    context = {
        'current_balance' : current_balance.balance, 
        'income' : income, 
        'expense' : expense,
        'history' : TransactionHistory.objects.all()
    }
    return render(request, 'index.html', context=context)

def delete(request, id):
    transaction = TransactionHistory.objects.filter(id = id)
    if transaction.exists():
        transaction = transaction[0]
        current_balance = CurrentBalance.objects.get(id=1)
        current_balance.balance -=  float(transaction.amount)
        current_balance.save()
        transaction.delete()
    return redirect('/')

    