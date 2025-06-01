from django.shortcuts import render
from .models import Auction

def home(request):
    auctions = Auction.objects.all().order_by('-date_start')[:12]  # posledních 12
    return render(request, 'hlavni/home.html', {'auctions': auctions})


def login_view(request):
    return render(request, 'hlavni/login.html')


def register_view(request):
    return render(request, 'hlavni/register.html')


def auction_detail(request):
    return render(request, 'hlavni/detail.html', {'auction_id': id})


def bid(request):
    return render(request, 'hlavni/bid.html', {'auction_id': id})
