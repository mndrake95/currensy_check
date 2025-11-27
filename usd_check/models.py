from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"USD to {self.currency}: {self.rate}"
