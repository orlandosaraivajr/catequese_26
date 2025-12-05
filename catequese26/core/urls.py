from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('catequese_infantil', views.catequese_infantil, name='catequese_infantil'),
    path('procure-secretaria', views.procure_secretaria, name='procure_secretaria'),
    # Secretaria
    path('listar-fichas/', views.listar_fichas, name='listar_fichas'),
    path('listar-todas-fichas/', views.listar_todas_fichas, name='listar_todas_fichas'),
    path('imprimir-ficha', views.imprimir_ficha, name='imprimir_ficha'),
]