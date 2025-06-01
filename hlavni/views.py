from django.shortcuts import render

def home(request):
    return render(request, 'hlavni/home.html')


def login_view(request):
    return render(request, 'hlavni/login.html')


def register_view(request):
    return render(request, 'hlavni/register.html')


def auction_detail(request):
    return render(request, 'hlavni/detail.html', {'auction_id': id})


def bid(request):
    return render(request, 'hlavni/bid.html', {'auction_id': id})
