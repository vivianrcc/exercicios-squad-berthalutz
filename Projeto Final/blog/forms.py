from django import forms
from blog.models import Comentario, Cadastro


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
    nome_do_livro = forms.CharField(
        label="Nome do livro:",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    nota_do_livro = nota_do_livro = forms.IntegerField(
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
    resenha = forms.CharField(
        label="Resenha:",
        required=True,
        max_length=500,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )

    class Meta:
        model = Cadastro
        fields = ["nome_do_livro", "nota_do_livro", "autor", "resenha"]
