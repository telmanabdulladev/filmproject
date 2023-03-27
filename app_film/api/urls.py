from django.urls import path
from app_film.api import views
urlpatterns = [
    path('films/', views.FilmAPIView.as_view(), name='films'),
    path('actors/', views.ActorAPIView.as_view(), name='actors'),
    
]
