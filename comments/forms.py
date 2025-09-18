
from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        labels = {'texto': 'Comentário'}
        widgets = {'texto': forms.Textarea(attrs={'rows': 3})}

