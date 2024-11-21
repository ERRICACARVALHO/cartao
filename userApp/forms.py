from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    FIRST_NAME_CHOICES = [
        ('Administrativo','Administrativo'),
        ('Gerente','Gerente'),
        ('usuario','usuario')
    ]
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', ]
    username = forms.CharField(label ='Matricula:')
    email = forms.EmailField(label ='email:')
    last_name = forms.CharField(label ='Nome completo:')
    first_name = forms.ChoiceField(label ='Status:',
                                  choices=FIRST_NAME_CHOICES,
                                   widget=forms.Select(attrs={'class':'custom-select'}),
                                   initial='usuario'
                                   )
