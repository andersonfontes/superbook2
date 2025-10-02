from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Villain
from .forms import VilaoForm

class VilaoListView(ListView):
    model = Villain
    template_name = "villains/lista_viloes.html"
    context_object_name = "viloes"
    ordering = ["codinome"]

class VilaoDetailView(DetailView):
    model = Villain
    template_name = "villains/detalhe_vilao.html"
    context_object_name = "vilao"

class VilaoCreateView(CreateView):
    model = Villain
    form_class = VilaoForm
    template_name = "villains/form_vilao.html"
    success_url = reverse_lazy("lista_viloes")

class VilaoUpdateView(UpdateView):
    model = Villain
    form_class = VilaoForm
    template_name = "villains/form_vilao.html"
    success_url = reverse_lazy("lista_viloes")

class VilaoDeleteView(DeleteView):
    model = Villain
    template_name = "villains/confirmar_exclusao.html"
    success_url = reverse_lazy("lista_viloes")

