"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from blog.views import index_html
from blog.views import resenha_do_livro, pesquisar_livro, realizar_cadastro_de_livro, editar_um_livro, ir_para_o_admin, cadastrar, fazer_login, excluir, tabela_de_livros, logoff


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_html),
    path("livro/<int:id>", resenha_do_livro, name="resenha"),
    path("pesquisar/", pesquisar_livro, name="pesquisa"),
    path("cadastrar_livro/", realizar_cadastro_de_livro, name="cadastrar_livro"),
    path("tabela_de_livros/", tabela_de_livros, name='editar_livros'),
    path("editar_livros/<int:id>", editar_um_livro, name='editar_um_livro'),
    path("excluir/<int:id>/", excluir, name='excluir'),
    path("login/", fazer_login, name='login'),
    path("cadastro/", cadastrar, name='cadastro'), 
    path("logoff/", logoff, name='logoff'),
]
