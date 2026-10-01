# catalogo/views.py (reemplaza el contenido completo del archivo)
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Cancion


def lista_canciones(request):
    q = request.GET.get("q", "").strip()
    canciones = Cancion.objects.all()
    if q:
        canciones = canciones.filter(Q(titulo__icontains=q) | Q(artista__icontains=q))
    contexto = {
        "canciones": canciones[:50],
        "total": canciones.count(),
        "q": q,
    }
    return render(request, "catalogo/lista.html", contexto)


def detalle_cancion(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    return render(request, "catalogo/detalle.html", {"cancion": cancion})