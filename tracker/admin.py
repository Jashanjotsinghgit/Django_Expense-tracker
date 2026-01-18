from django.contrib import admin
from tracker.models import CurrentBalance, TransactionHistory, RequestLogs
# Register your models here.

admin.site.site_title = "Expense Tracker"
admin.site.site_header = "Expense Tracker"
admin.site.index_title = "Tracker"

class RequestAdmin(admin.ModelAdmin):
    search_fields = ['request_method', 'request_path']
    list_filter = ['request_method']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['amount', 'expense_type', 'description']
    
admin.site.register(CurrentBalance)
admin.site.register(TransactionHistory, TransactionAdmin)
admin.site.register(RequestLogs, RequestAdmin)

