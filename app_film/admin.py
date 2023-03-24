from django.contrib import admin
from app_film.models import FilmModel, ActorModel, LikeModel, CommentModel

# Register your models here.
""" 
we use @ (decorator) because django suggest us our we must show our each admin class has to belong to a following model

"""

@admin.register(FilmModel) #if you do not write FilmModel properties of ModelAdmin then it can't access fields of ModelAdmin
class FilmAdmin(admin.ModelAdmin): # override that means you change value of property or behaviour of method main class
    list_display=('name','rating','views_count') # olimorphizm # list_display have been overrided
    list_filter=('pub_date',)
    list_editable=('rating',)
    search_fields=('name',)
    save_on_top= True
class LikeAdmin(admin.ModelAdmin):
    list_display=('name','surname')
    
@admin.register(ActorModel)
class ActorAdmin(admin.ModelAdmin):
     list_display=('name', 'surname')
     
@admin.register(CommentModel) 
class CommentAdmin(admin.ModelAdmin):
     list_display=['user','film']  

     

     
    
# admin.site.register(FilmModel,FilmAdmin)
# admin.site.register(ActorModel)
# admin.site.register(LikeModel)
# admin.site.register(CommentModel)



