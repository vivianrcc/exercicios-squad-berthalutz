from django import forms
from blog.models import Comentario, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ComentarioForm(forms.ModelForm):
    usuario = forms.CharField(
        label="Nome do usuário:",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    comentario = forms.CharField(
        label="Comentário:",
        required=True,
        max_length=500,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )

    class Meta:
        model = Comentario
        fields = ["usuario", "comentario"]


class CadastroForm(forms.ModelForm):
    titulo = forms.CharField(
        label="Nome do livro:",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    nota = forms.IntegerField(
        label="Nota do livro:",
        required=True,
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "min": "1", "max": "5"}
        ),
    )
    autor = forms.CharField(
        label="Autor:",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    preview = forms.CharField(
        label="Preview:",
        required=True,
        max_length=500,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    content = forms.CharField(
        label="Resenha:",
        required=True,
        max_length=500,
        widget=forms.Textarea(attrs={"class": "form-control mb-3"}),
    )

    class Meta:
        model = Post
        fields = ["titulo", "autor", "preview", "nota", "content"]

class CadastroUsuarioForm(forms.ModelForm):
    username= forms.CharField(
        label="Usuário:",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    email= forms.EmailField(
        label='Email:',
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    password= forms.CharField(
        label="Senha:",
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", "type": "password"}),
    )
    class Meta:
        model = User
        fields = ["username","email", "password"]

class LoginForm(forms.ModelForm):
    username= forms.CharField(
        label="Usuário:",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
        
    password= forms.CharField(
        label="Senha:",
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", "type": "password"}),
    )

    class Meta:
        model = User
        fields = ["username", "password"]