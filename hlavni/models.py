from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


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

    groups = models.ManyToManyField(
        Group,
        related_name='main_users',
        blank=True,
        help_text='The groups this user belongs to. ',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='main_users_permissions',
        blank=True,
        help_text='Specific permissions for this user. ',
        verbose_name='user permissions',
    )

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


class Tracking(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} is tracking {self.auction}"


class Review(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    reviewed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewed')
    comment = models.TextField()
    review = models.IntegerField()

    def __str__(self):
        return f"{self.reviewer} adds a review to {self.reviewed}"

