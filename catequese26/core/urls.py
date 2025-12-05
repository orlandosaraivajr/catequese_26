from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('catequese_infantil', views.catequese_infantil, name='catequese_infantil'),
    path('crisma', views.crisma, name='crisma'),
    path('perseveranca', views.perseveranca_mej, name='perseveranca_mej'),
    path('catequese_adulto', views.catequese_adulto, name='catequese_adulto'),
    path('procure-secretaria', views.procure_secretaria, name='procure_secretaria'),
    # Secretaria
    path('secretaria', views.listar_fichas, name='secretaria'),
    path('listar-fichas/', views.listar_fichas, name='listar_fichas'),
    path('listar-todas-fichas/', views.listar_todas_fichas, name='listar_todas_fichas'),
    path('imprimir-ficha', views.imprimir_ficha, name='imprimir_ficha'),
    path('imprimir-ficha-crisma', views.imprimir_ficha_crisma, name='imprimir_ficha_crisma'),
    path('imprimir-ficha-perseveranca-mej', views.imprimir_ficha_perseveranca_mej, name='imprimir_ficha_perseveranca_mej'),
    path('imprimir-ficha-adulto', views.imprimir_ficha_adulto, name='imprimir_ficha_adulto'),
]