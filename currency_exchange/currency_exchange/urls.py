from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Welcome to the Currency Exchange API</h1>"
                        "<p>Use /auth/register/ or /auth/login/ or /currency/exchange/ "
                        "or /currency/convert/ to interact with the API.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include('currency.urls')),  # Подключение маршрутов приложения currency
]