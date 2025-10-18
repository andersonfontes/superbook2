from django.urls import path
from . import views
from .views import toggle_pow, PostListView, PostCreateView, PostUpdateView, PostDeleteView, detalhe_post

urlpatterns = [    
    
    path('', PostListView.as_view(), name='lista_posts'),
    path('novo/', PostCreateView.as_view(), name='novo_post'), 
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),   
    path('<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
    path('<int:pk>/', detalhe_post, name='detalhe_post'),
    path('<int:pk>/pow/', toggle_pow, name='toggle_pow'),  # NOVO
]

