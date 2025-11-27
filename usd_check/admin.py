from django.contrib import admin
from .models import ExchangeRate

# Register your models here.
@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('rate', 'created_at', 'currency') 
    readonly_fields = ('created_at',) 
    list_filter = ('created_at',) 