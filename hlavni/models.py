from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('AKTIVNI', 'Aktivní'),
        ('NEAKTIVNÍ', 'Neaktivní'),
        ('BLOKOVANÝ', 'Blokovaný')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AKTIVNI')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    TYP_CHOICES = [
        ('BEZNY', 'Bezny'),
        ('PREMIUM', 'Premium'),
    ]
    typ = models.CharField(max_length=10, choices=TYP_CHOICES, default='BEZNY')

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='category_logos/', null=True, blank=True)

    def __str__(self):
        return self.name

