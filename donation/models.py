from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Acceptor(AbstractUser):
    pass

class Donation(models.Model):
    donator = models.CharField(max_length=20, blank=True)
    acceptor = models.ForeignKey(Acceptor, related_name="donations", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)