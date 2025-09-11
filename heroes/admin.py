from django.contrib import admin
from .models import Hero

# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'criado_em'] # campos exibidos na listagem
    list_filter = ['cidade'] # campo disponivel para filtrar os dados
    search_fields = ['codinome', 'nome_real', 'cidade']  # campos a serem pesquisados na busca

    fieldsets = (   # divide em seções
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações Gerais', {
            'fields': ('poder_principal', 'cidade', 'historia' )
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
        ('Informações de Contato', {
            'fields': ('email_contato',)
        }),
    )
    
    readonly_fields = ['criado_em']    