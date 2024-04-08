from django.db import models

# Create your models here.
class Post(models.Model): 
    nota_livro = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    titulo= models.CharField(blank=False, max_length=100, null=False )
    autor= models.CharField(blank=False, max_length=70, null=False ) 
    date= models.DateTimeField(auto_now_add=True)
    preview= models.TextField(blank=False, max_length=200, null=False)

    nota = models.IntegerField(blank=True, choices=nota_livro)
    content = models.TextField(blank=False, null=False)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.nota}"


class Comentario(models.Model):
    usuario = models.CharField(max_length=50, blank=True)
    comentario = models.TextField(blank=False, max_length=200)
    data2 = models.DateTimeField(auto_now_add=True)
    id_livro = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Comentário de {self.usuario}"


class Cadastro(models.Model):
    nome_do_livro = models.CharField(max_length=100, blank=False, null=False)
    nota_do_livro = models.IntegerField(
        blank=False, null=False, choices=[(i, i) for i in range(1, 6)]
    )
    autor = models.CharField(max_length=100, blank=False, null=False)
    resenha = models.TextField(blank=False, null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.nome_do_livro} - {self.autor}"

    # class Meta:
    #     verbose_name = "Cadastro"
    #     verbose_name_plural = "Cadastros"
    #     ordering = ["-data_cadastro"]
