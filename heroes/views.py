from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Hero
from .forms import ContatoForm
from .forms import HeroForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

#CBV - CLASS-BASED VIEW - VIEW BASEADA EM CLASSE COM GENERIC LIST VIEW
class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista_herois.html"
    context_object_name = "herois"
    
#FBV - FUNCTION-BASED VIEW - VIEW BASEADA EM FUNCTION  

def lista_herois(request):
    herois = Hero.objects.all()

    # <-- NOVO: booleana segura p/ template (evita acessar request.user.hero direto)
    user_tem_heroi = False
    if request.user.is_authenticated:
        user_tem_heroi = Hero.objects.filter(usuario=request.user).exists()

    return render(
        request,
        "heroes/lista_herois.html",
        {"herois": herois, "user_tem_heroi": user_tem_heroi},
    )


class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista_herois.html"
    context_object_name = "herois"


def contato_view(request):
    form = ContatoForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        return render(request, "heroes/contato_sucesso.html")
    
    return render(request, "heroes/contato.html", {"form": form})

@login_required
def criar_heroi(request):
    hero = None
    try:
        hero = request.user.hero  # OneToOneField
    except Hero.DoesNotExist:
        pass

    if request.method == "POST":
        form = HeroForm(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            hero = form.save(commit=False)
            hero.usuario = request.user
            hero.save()
            messages.success(request, "Herói salvo com sucesso!")
            return redirect("lista_herois")
    else:
        form = HeroForm(instance=hero)

    return render(request, "heroes/form_heroi.html", {"form": form})

@login_required
def editar_heroi(request, pk):
    hero = get_object_or_404(Hero, pk=pk)

    # segurança: só o dono pode editar
    if hero.usuario_id != request.user.id:
        return HttpResponseForbidden("Você não tem permissão para editar este herói.")

    if request.method == "POST":
        form = HeroForm(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            form.save()
            messages.success(request, "Herói atualizado com sucesso!")
            return redirect("lista_herois")   # use o nome/namespace correto
    else:
        form = HeroForm(instance=hero)

    return render(request, "heroes/form_heroi.html", {"form": form})

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from heroes.models import Hero

@login_required
def redirect_after_login(request):
    """Redireciona o usuário conforme tenha herói ou não."""
    tem_heroi = Hero.objects.filter(usuario=request.user).exists()
    if tem_heroi:
        return redirect("lista_posts")
    return redirect("lista_herois")

