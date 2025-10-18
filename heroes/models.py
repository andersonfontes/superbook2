
from django.db import models
from django.contrib.auth.models import User

class Hero(models.Model):
    # VINCULO COM USER: vamos permitir nulo por enquanto para
    # evitar erros chatos na migração, pois já temos alguns heróis:
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hero', null=True, blank=True, unique=True) 
    
    codinome = models.CharField(max_length=50, unique=True)
    nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder_principal = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    historia = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    email_contato = models.EmailField(blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos_herois/', blank=True, null=True)
    

    def __str__(self):
        return self.codinome

