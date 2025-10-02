from django.urls import path
from . import views

urlpatterns = [
    path("", views.VilaoListView.as_view(), name="lista_viloes"),
    path("novo/", views.VilaoCreateView.as_view(), name="novo_vilao"),
    path("<int:pk>/editar/", views.VilaoUpdateView.as_view(), name="editar_vilao"),
    path("<int:pk>/excluir/", views.VilaoDeleteView.as_view(), name="excluir_vilao"),
    path("<int:pk>/", views.VilaoDetailView.as_view(), name="detalhe_vilao"),
]