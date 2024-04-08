from django.contrib import admin
from blog.models import Post, Comentario, Cadastro

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "date"]
    search_fields = ["titulo", "autor", "date"]
    list_filter = ["date"]

    class Meta:
        verbose_name = "Posts"
        ordering = ["-date"]


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ["usuario", "data2"]
    search_fields = ["usuario", "data2"]
    list_filter = ["data2"]

    class Meta:
        verbose_name = "Comentários"
        ordering = ["-data2"]


@admin.register(Cadastro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("nome_do_livro", "autor", "data_cadastro")
    list_filter = ("data_cadastro",)
