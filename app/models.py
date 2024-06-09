from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    billingaddress = models.CharField(max_length=300)
    joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.name} "
