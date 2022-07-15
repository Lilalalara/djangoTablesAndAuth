from django.urls import path
from . import views
from .views import ShowProducts

urlpatterns = [
    path('', ShowProducts.as_view(), name="home")
]
