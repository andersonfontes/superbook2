from django.urls import path
from . import views
from .views import HeroListView

urlpatterns = [    
    path('lista/', views.lista_herois, name='lista_herois'),
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
    path('contato/', views.contato_view, name='contato'),
    path('novo/', views.criar_heroi, name='criar_heroi'),
    path('<int:pk>/editar/', views.editar_heroi, name='editar_heroi'),  
]