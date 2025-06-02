from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='hlavni/login.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('aukce/<int:id>/', views.auction_detail, name='aukce_detail'),
    path('aukce/<int:id>/bid/', views.bid, name='bid'),
    path('logout/', views.logout_view, name='logout'),
]