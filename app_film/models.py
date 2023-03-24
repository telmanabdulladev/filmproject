from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

class FilmModel(models.Model):
#    id=models.AutoField()
   name=models.CharField(max_length=256, help_text='please enter the film name')
   poster=models.ImageField(upload_to='posters/')
   video=models.FileField(upload_to='videos/') 
   rating=models.FloatField(default=0)
   pub_date=models.DateField(auto_now_add=True)
   views_count=models.IntegerField(default=0)
   about=models.TextField(blank=True,null=True)
   
   class Meta:
        #  ordering=("-id",) list films by descending orders, but we will set it in IndexView to be useful
         verbose_name='Film'
         verbose_name_plural='Films'
       
   def __str__(self):
        return self.name
      
class ActorModel(models.Model):
    films=models.ManyToManyField(FilmModel,related_name='actors')
    name=models.CharField(max_length=256)
    surname=models.CharField(max_length=256)
    about=models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name='Actor'
        verbose_name_plural='Actors'
   
    @property #property vermekde meqsed methodu propertiye (xusiyyete cevirmek) cevirmek
    def get_fullname(self):
        return self.name + ' ' + self.surname
    def __str__(self):
        return self.get_fullname
    
class LikeModel(models.Model):
        user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes') # on_delete=CASCADE - all likes will be removed once user deleted
        film=models.ForeignKey(FilmModel,on_delete=models.CASCADE,related_name='film_likes')

        
        class Meta:
        
    
          verbose_name='Like'
          verbose_name_plural='Likes'
        def __str__(self):
           return self.user.username + '|' + self.film.name
        
class CommentModel(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comments')
        film=models.ForeignKey(FilmModel,on_delete=models.CASCADE,related_name='film_comments')
        comment=models.TextField()
        pub_date=models.DateField(auto_now=True)
        
        class Meta:
          verbose_name='Comment'
          verbose_name_plural='Comments'
        def __str__(self):
          return self.user.username + '|' + self.film.name
            
        
        """
        auto_now=True - takes current date
        auto_now_add=True -takes date created initial 
        """
        
            
    
    
   
   
"""name, pub_date, id, rating, about"""
""" Film -many  Actor - many
many to many relation

"""

""" 
Film- model -User

Like -User - Film
Comment -User -Film

CommentModel:
pub_date, text, user, film
LikeModel:
user, film

Connections

user-like - OneToMany
like-film -OneToMany

"""

    


     
            
    
    