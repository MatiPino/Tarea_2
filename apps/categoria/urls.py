from django.urls import path
from . import views

urlpatterns = [
    path('categoria/', views.index, name='categoria')
]
