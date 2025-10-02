from django import forms
from .models import Villain

class VilaoForm(forms.ModelForm):
    class Meta:
        model = Villain
        fields = ["codinome", "nome_real", "poder_principal", "cidade", "historia"]
        widgets = {
            "historia": forms.Textarea(attrs={"rows": 5}),
        }

