from gc import get_objects

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from pelicula.api import PeliculaSerializer
from pelicula.api.genero_viewset import GeneroSerializer
from pelicula.models import Genero, Genero_Pelicula
from pelicula.models.pelicula import Pelicula

class GeneroPeliculaSerializer(serializers.ModelSerializer):
    #lgenero = GeneroSerializer(many=False, read_only=True)
    #lpelicula = PeliculaSerializer(many=False, read_only=True)
    class Meta:
        model = Genero_Pelicula
        fields = '__all__'

class GeneroPeliculaViewset(viewsets.ModelViewSet):
    serializer_class = GeneroPeliculaSerializer
    queryset = Genero_Pelicula.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        genero_pelicula = Genero_Pelicula.objects.all()
        return genero_pelicula

    @action(detail=True, methods=['get'], url_path='peliculas',
            permission_classes=([IsAuthenticated]))
    def get_genero_pelicula(self, request, pk):
        lista_peliculas = Genero_Pelicula.objects.filter(lgenero_id=pk)
        listapelicula = []
        for genero_pelicula in lista_peliculas:
            pelicula = Pelicula.objects.filter(pk=genero_pelicula.lpelicula.pk).get()
            listapelicula.append(pelicula)
        serializer = PeliculaSerializer(listapelicula, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)