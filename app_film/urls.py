from django.urls import path,include
from .import views
app_name='app_film'
urlpatterns=[
    path('index/', views.IndexView.as_view(),name='index'),
    path('detail/<int:id>/',views.DetailView.as_view(),name='detail'),
    path('create-film/',views.CreateView.as_view(), name='create-film'),
]
"""www.example.com/film/detail/5"""
