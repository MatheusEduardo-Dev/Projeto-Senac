from django.contrib import admin
from .models import Produto, Curso, Pedido
# Register your models here.

admin.site.register(Produto)
admin.site.register(Curso)
admin.site.register(Pedido)