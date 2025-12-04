from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('catequese_infantil', views.catequese_infantil, name='catequese_infantil'),
    path('procure-secretaria/', views.procure_secretaria, name='procure_secretaria'),
]