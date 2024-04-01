from django.shortcuts import render
# from django.http import HttpResponse
from blog.models import Post, Comentario
from blog.forms import ComentarioForm
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.shortcuts import redirect


# View da página inicial 
def index_html(request):
    posts = Post.objects.all() #o valor de posts é uma lista de objetos
    return render(request, 'post_preview.html', {'posts1': posts}) #você pega o valor da chave no HTML 


def resenha_do_livro(request, id):
    print("id", id)
    id_do_livro = id
    posts = Post.objects.get(pk=id) #aqui tbm é uma lista de objetos, que traz só 1 item
    comentarios= Comentario.objects.order_by("-data2").filter(id_livro_id= id)
    sucesso = False
    print("request", request)
    form = ComentarioForm()
    dataToBePassed = {
        'posts': posts,
        'form': form,
        'sucesso': sucesso,
        "id_do_livro": id_do_livro, 
        'comentarios': comentarios
    }
    if request.method == 'GET':
        return get_resenha(request, dataToBePassed)
    elif request.method == 'POST':
        return post_resenha(request, dataToBePassed)

def get_resenha(request, dataToBePassed):
    return render(request, 'post1.html', dataToBePassed)

def post_resenha(request, dataToBePassed):
    form = ComentarioForm(request.POST)
    if form.is_valid():
        form.save()
        dataToBePassed['sucesso'] = True
        return render(request, 'post1.html', dataToBePassed)




