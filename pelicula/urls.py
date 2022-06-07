from django.urls import path, include
from rest_framework import routers

from pelicula.api import PeliculaViewset, UserViewset, GeneroPeliculaVViewset
from pelicula.api.genero_pelicula_viewset import GeneroPeliculaViewset
from pelicula.api.genero_viewset import GeneroViewset

router = routers.DefaultRouter()
router.register(r'pelicula', PeliculaViewset)
router.register(r'user', UserViewset)
router.register(r'genero', GeneroViewset)
router.register(r'pelicula-genero', GeneroPeliculaViewset)
urlpatterns = [
    path('', include(router.urls)),
]
