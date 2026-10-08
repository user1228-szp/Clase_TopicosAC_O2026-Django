from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from catalogo.api_views import CancionViewSet, PlaylistViewSet

router = DefaultRouter()
router.register(r'canciones', CancionViewSet)
router.register(r'playlists', PlaylistViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalogo.urls")), #vistas HTML
    path("api/", include(router.urls)), #vistas API
    path("api-auth/", include("rest_framework.urls")),

]