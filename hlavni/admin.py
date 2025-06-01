from django.contrib import admin
from .models import Category, User, Auction, Bids, Tracking, Review


admin.site.register(Category)
admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Bids)
admin.site.register(Tracking)
admin.site.register(Review)

