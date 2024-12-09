from django.urls import path
from .views import register, login, exchange_rates, convert


urlpatterns = [
    path('auth/register/', register, name='register'),
    path('auth/login/', login, name='login'),
    path('currency/exchange/', exchange_rates, name='exchange'),
    path('currency/convert/', convert, name='convert'),
]