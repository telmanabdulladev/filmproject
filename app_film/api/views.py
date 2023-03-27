from rest_framework import generics 
from app_film.models import FilmModel
from app_film.models import ActorModel

from app_film.api.serializers import FilmSerializer
from app_film.api.serializers import ActorSerializer


class FilmAPIView(generics.ListAPIView):
    queryset=FilmModel.objects.all()
    serializer_class = FilmSerializer
class ActorAPIView(generics.ListAPIView):
    queryset=ActorModel.objects.all()
    serializer_class = ActorSerializer   
        