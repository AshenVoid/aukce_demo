from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('aukce/<int:id>/', views.auction_detail, name='auction_detail'),
    path('aukce/<int:id>/bid/', views.bid, name='bid'),
]