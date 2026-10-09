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
    artista = models.CharField(max_length=300, db_index=True)
    album = models.CharField(max_length=200, blank=True)
    # genero = models.CharField(max_length=100)
    popularidad = models.PositiveSmallIntegerField()
    duracion_ms = models.PositiveIntegerField()
    
    fecha_lanzamiento = models.CharField(max_length=10, blank=True)
    creada_en = models.DateTimeField(auto_now_add=True)
    #fecha_creacion = models.DateTimeField(auto_now_add=True)
    playlists = models.ManyToManyField(Playlist, related_name='canciones')
    
    class Meta:
        ordering = ['-popularidad']  #como se ordena la lista de canciones, en este caso por popularidad de mayor a menor
        verbose_name_plural = 'Canciones'
        
    def __str__(self):
        return f"{self.titulo} - {self.artista}" #aparecer titulo y artista en el admin de django

        # catalogo/models.py (dentro de la clase Cancion, después de __str__)
    @property
    def duracion(self):
        minutos, segundos = divmod(self.duracion_ms // 1000, 60)
        return f"{minutos}:{segundos:02d}"
        