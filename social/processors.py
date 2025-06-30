''' creamos un contexto para poder usarlo en los tamplates'''
from .models import Link
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx 
