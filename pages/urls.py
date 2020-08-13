from django.urls import path
from .views import hompPageView

urlpatterns = [
    path('', hompPageView, name='home')
]
