from django import forms
from userprofile.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('departamento', 'usuario', 'documento', 'fecha', )