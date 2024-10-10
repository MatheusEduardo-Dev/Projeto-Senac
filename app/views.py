from django.shortcuts import render , redirect, get_object_or_404
from .models import Produto, Pedido, Curso
from .forms import PedidoForm, ProdutoForm, CursoForm, RegistroForm, LoginForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render (request, 'listar_cursos.html', {'cursos':cursos})

def home(request):
    cursos = Curso.objects.all()
    return render (request, 'listar_cursos.html', {'cursos':cursos})

def cadastrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CursoForm
    return render (request,'cadastro.html', {'form':form})

def cadastrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PedidoForm
    return render (request,'cadastro.html', {'form':form})
    
def busca(request):
    if 'nome' in request.POST:
        nome = request.POST['nome']
        produtos = Curso.objects.filter(nome__icontains=nome)
        return render (request, 'buscar.html', {'produtos':produtos})
    else:
        produtos = Curso.objects.all()
        return render (request, 'buscar.html', {'produtos':produtos})
    
def excluir_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')  # Redireciona para a lista de cursos
    return render(request, 'excluir_curso.html', {'curso': curso})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')  # Redireciona para a lista de cursos
    else:
        form = CursoForm(instance=curso)
    return render(request, 'editar_curso.html', {'form': form, 'curso': curso}) 

# def loginview(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data = request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request,'registration/login.html', {'form':form, 'hide_menu': True})

def logout_view(request):
    logout(request)
    return redirect('login')

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('home')  # Redirecionar para a página inicial
    else:
        form = RegistroForm()
    return render(request, 'registrar.html', {'form': form})

def logar(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Você está logado!')
                return redirect('home')  # Redirecionar para a página inicial
            else:
                messages.error(request, 'Nome de usuário ou senha inválidos.')
    else:
        form = LoginForm()
    return render(request, 'logar.html', {'form': form})

def adicionar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')  # Redireciona para a lista de cursos
    else:
        form = CursoForm()
    return render(request, 'adicionar_curso.html', {'form': form})
