from mysite.cursos import facade

# from mysite.cursos.models import Curso


def listar_cursos(request):
    return {'CURSOS': facade.listar_cursos_ordenados()}
