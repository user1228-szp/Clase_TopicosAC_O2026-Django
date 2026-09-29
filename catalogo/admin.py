from django.contrib import admin
from .models import Cancion, Playlist

# Register your models here.

admin.site.register(Cancion) #generar formulario
admin.site.register(Playlist) 