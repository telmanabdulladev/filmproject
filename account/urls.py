from django.urls import path
from account import views

app_name='account'
urlpatterns = [
  path('register/', views.register, name='register'), 
  path('login/',views.loginUser, name='login'),
  path('logout/',views.logoutUser,name='logout'),
   
]
