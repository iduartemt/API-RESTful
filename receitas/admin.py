from django.contrib import admin
from .models import Ingrediente, Receita, Utilizador


admin.site.register(Utilizador)
admin.site.register(Ingrediente)
admin.site.register(Receita)
