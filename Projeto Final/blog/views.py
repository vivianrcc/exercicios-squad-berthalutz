from django.shortcuts import render, redirect
from blog.models import Post, Comentario, Cadastro
from blog.forms import ComentarioForm, CadastroForm


# View da página inicial
def index_html(request):
    posts = Post.objects.all()  # o valor de posts é uma lista de objetos
    return render(
        request, "post_preview.html", {"posts1": posts}
    )  # você pega o valor da chave no HTML


# View do conteúdos total das páginas com resenhas. Ela pega o livro, o comentário, o id do livro e o formulário de comentário
def resenha_do_livro(request, id):
    id_do_livro = id
    posts = Post.objects.get(
        pk=id
    )  # aqui tbm é uma lista de objetos, que traz só 1 item
    comentarios = Comentario.objects.order_by("-data2").filter(id_livro_id=id)
    sucesso = False
    form = ComentarioForm()
    dataToBePassed = {
        "posts": posts,
        "form": form,
        "sucesso": sucesso,
        "id_do_livro": id_do_livro,
        "comentarios": comentarios,
    }
    if request.method == "GET":
        return get_resenha(request, dataToBePassed)
    elif request.method == "POST":
        return post_resenha(request, dataToBePassed)


# view da resenha do livro (função chamada acima)
def get_resenha(request, dataToBePassed):
    return render(request, "post1.html", dataToBePassed)


# view do formulário de comentários (função chamada acima)
def post_resenha(request, dataToBePassed):
    form = ComentarioForm(request.POST)
    if form.is_valid():
        dataToBePassed["sucesso"] = True
        post_instance = Post.objects.get(id=dataToBePassed["id_do_livro"])

        new_comment = Comentario(
            usuario=form["usuario"].value(),
            comentario=form["comentario"].value(),
            id_livro=post_instance,
        )
        new_comment.save()

        return render(request, "post1.html", dataToBePassed)


# view da barra de pesquisa
def pesquisar_livro(request):
    if request.method == "GET":
        try:
            pesquisa = request.GET.get("pesquisa", None)
            print("pesquisa", pesquisa)

            if type(pesquisa) == str or None:
                consulta = (
                    Post.objects.filter(titulo__icontains=pesquisa)
                    | Post.objects.filter(autor__icontains=pesquisa)
                    | Post.objects.filter(content__icontains=pesquisa)
                )
                print("consulta", consulta[0].id)
            return render(
                request,
                "resultado_pesquisa.html",
                {"pesquisa": pesquisa, "consulta": consulta},
            )
        except ValueError:
            consulta = Post.objects.all()
            return render(
                request,
                "resultado_pesquisa.html",
                {"pesquisa": pesquisa, "consulta": consulta},
            )


def realizar_cadastro(request):
    sucesso = False
    if request.method == "GET":
        form = CadastroForm()
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()
        return render(
            request,
            "cadastro_logado.html",
            {"cadastros": Cadastro.objects.all()},
        )
    contexto = {"form": form, "sucesso": sucesso}
    return render(request, "cadastro.html", contexto)
