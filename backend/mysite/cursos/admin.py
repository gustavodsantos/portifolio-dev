from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from mysite.cursos.models import Curso


@admin.register(Curso)
class ModuloAdmin(OrderedModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
