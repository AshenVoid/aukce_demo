from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Auction

def home(request):
    auctions = Auction.objects.all().order_by('-date_start')[:12]
    return render(request, 'hlavni/home.html', {'auctions': auctions})


def login_view(request):
    return render(request, 'hlavni/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'hlavni/register.html', {'form': form})


def auction_detail(request):
    return render(request, 'hlavni/detail.html', {'auction_id': id})


def bid(request):
    return render(request, 'hlavni/bid.html', {'auction_id': id})


def logout_view(request):
    logout(request)
    return redirect('index')
