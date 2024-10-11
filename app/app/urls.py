from django.contrib import admin
from django.urls import path , include
from django.views.generic import RedirectView
from . import views
from .views import editar_curso, excluir_curso, listar_cursos, registrar, logar, adicionar_curso
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.home), name='home'),
    path('busca/', login_required(views.busca), name='busca'),
    # path('', views.loginview, name='login'),
    path('cadastrar_pedido/', views.cadastrar_pedido, name='cadastrar_pedido'),
    path('cadastrar_curso/', views.cadastrar_curso, name='cadastrar_curso'),
    path('listar_cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/editar/<int:id>/', editar_curso, name='editar_curso'),
    path('cursos/excluir/<int:id>/', excluir_curso, name='excluir_curso'),
    path('registrar/', registrar, name='registrar'),
    path('logar/', logar, name='logar'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('cursos/adicionar/', adicionar_curso, name='adicionar_curso'),
    path('', RedirectView.as_view(url='logar/', permanent=False), name='index'),
]