from django.urls import path
from .views import SnacksList

urlpatterns = [
    path('', SnacksList.as_view(),name='snack'),
    
]