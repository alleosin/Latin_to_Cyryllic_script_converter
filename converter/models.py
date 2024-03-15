from django.db import models

# Create your models here.
class Donation(models.Model):
    donator = models.CharField(max_length=20, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    text = models.TextField(blank=True)
