from rest_framework import serializers
from app_film.models import FilmModel
from app_film.models import ActorModel


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmModel 
        fields = "__all__"
        #exclude=('name',) will display apart from name
        
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = "__all__"