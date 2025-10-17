from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from heroes.models import Hero
from .forms import PostForm
from comments.forms import ComentarioForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/lista_posts.html'
    context_object_name = 'posts'
    ordering = ['-criado_em']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

    def form_valid(self, form):
        try:
            hero = self.request.user.hero
        except Hero.DoesNotExist:
            messages.error(self.request, "Crie seu perfil de herói antes de publicar.")
            return redirect('criar_heroi')
        form.instance.autor = hero
        messages.success(self.request, "Post criado com sucesso.")
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

    def test_func(self):
        obj = self.get_object()
        try:
            return self.request.user.is_authenticated and obj.autor == self.request.user.hero
        except Hero.DoesNotExist:
            return False

    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para editar este post.")
        return redirect('lista_posts')

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')

    def test_func(self):
        obj = self.get_object()
        try:
            return self.request.user.is_authenticated and obj.autor == self.request.user.hero
        except Hero.DoesNotExist:
            return False

    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para excluir este post.")
        return redirect('lista_posts')

def detalhe_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all().order_by('criado_em') if hasattr(post, 'comentarios') else []

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            messages.success(request, "Comentário adicionado.")
            return redirect('detalhe_post', pk=post.pk)
    else:
        form = ComentarioForm()

    return render(request, 'posts/detalhe_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })