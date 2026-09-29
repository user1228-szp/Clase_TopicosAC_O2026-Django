from django.db import models

class Playlist(models.Model):
    playlist_id = models.CharField(max_length=22, unique=True)
    nombre = models.CharField(max_length=300)
    genero = models.CharField(max_length=50)
    subgenero = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

    
class Cancion(models.Model):
    spotify_id = models.CharField(max_length=22, unique=True)
    titulo = models.CharField(max_length=300)
    artista = models.CharField(max_length=300)
    album = models.CharField(max_length=200, blank=True)
    # genero = models.CharField(max_length=100)
    popularidad = models.PositiveSmallIntegerField()
    duracion_ms = models.PositiveIntegerField()
    
    fecha_lanzamiento = models.CharField(max_length=10, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    playlists = models.ManyToManyField(Playlist, related_name='canciones')
    
    class Meta:
        ordering = ['-popularidad']  #como se ordena la lista de canciones, en este caso por popularidad de mayor a menor
        verbose_name_plural = 'Canciones'
        
    def __str__(self):
        return f"{self.titulo} - {self.artista}" #aparecer titulo y artista en el admin de django
        