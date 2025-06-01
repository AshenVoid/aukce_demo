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


class Auction(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='auction_photos/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    minimal_bid = models.DecimalField(max_digits=10, decimal_places=2)
    buyout_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    propagation = models.BooleanField(default=False)
    locality = models.CharField(max_length=200)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    views = models.PositiveIntegerField(default=0)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bids(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.bid} on {self.auction}"
