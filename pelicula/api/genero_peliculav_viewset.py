from rest_framework import viewsets, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from pelicula.models import Genero_Pelicula


class GeneroPeliculaVSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero_Pelicula
        fields = '__all__'

class GeneroPeliculaVViewset(viewsets.ModelViewSet):
    serializer_class = GeneroPeliculaVSerializer
    queryset = Genero_Pelicula.objects.all()
    permission_classes = [IsAuthenticated]

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