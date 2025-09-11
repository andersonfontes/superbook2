from django.urls import path
from . import views
from .views import PostListView, PostCreateView

urlpatterns = [    
    
    path('lista/', PostListView.as_view(), name='lista_posts'),
    path('novo/', PostCreateView.as_view(), name='novo_post'),    
]

