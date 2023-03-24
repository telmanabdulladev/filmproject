from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app_film.models import FilmModel, LikeModel, CommentModel 
from django.contrib import messages
from app_film.forms import FilmForm  #form located app_film module(file) so we have to appy for app_film.form
from django.views import generic
from django.db.models import Q 
# from django.http import HttpResponse
# function-based view and class-based view
# def index(request):
#     films=FilmModel.objects.all()   
#     context={
#         'films':films,
#     }
#     return render (request,'index.html',context)
# class based views
class IndexView(generic.View):
    def get(self,request,*args, **kwargs):
          films=FilmModel.objects.order_by("-id")
          query=request.GET.get("query")
          if query:
             films=films.filter(
                 Q(name__contains=query) | Q(about__contains=query))
          context={
        'films':films,
    }
          return render (request,'index.html',context)
      
    
# def detail(request,id):
#     film=FilmModel.objects.get(id=id)
#     film.views_count+=1
#     film.save()
    
#     context={
#         'film': film,
#     }
    
#     if request.method=='POST':
#         choice = request.POST.get("choice")
#         if choice =="like":
            
#             if not LikeModel.objects.filter(user=request.user).exists():
                
#                 LikeModel.objects.create(
#                 user=request.user,
#                 film=film,
#          )
#                 messages.success(request,'Liked')
#             else:
#                 messages.info(request,'Already liked')
#         elif choice=="comment":
#             comment=request.POST.get("comment")
#             CommentModel.objects.create(
#                 user=request.user,
#                 film=film,
#                 comment=comment,
                
#             )    
#     return render (request,'detail.html',context)

class DetailView(generic.View):
    def get(self,request,id,*args, **kwargs):
        film=FilmModel.objects.get(id=id)
        film.views_count+=1
        film.save()
    
        context={
            'film': film,
        }
        return render(request, 'detail.html',context)
    
    def post(self,request,id,*args, **kwargs):
        self.film=FilmModel.objects.get(id=id)
        choice = request.POST.get("choice")
        context = {'film': self.film}
        if choice =="like":
            
                 
            
            if not LikeModel.objects.filter(user=request.user).exists():
                
                
                LikeModel.objects.create(
                    user=request.user,
                    film=self.film,
                 )
                messages.success(request,'Liked')
            else:
                messages.info(request,'Already liked')
        elif choice=="comment":
                  comment=request.POST.get("comment")
                  CommentModel.objects.create(
                  user=request.user,
                  film=self.film,
                  comment=comment,
                
                )    
        return render (request,'detail.html',context)
        
        
        
# def createFilm(request):
#     form=FilmForm()                 #you can also write like this context {'form': FilmForm()}
#     context={
#         'form': form,
#     }
#     if request.method=='POST':
#         # request.POST = {     } is dictionary
#         form=FilmForm(request.POST, files=request.FILES)
#         """
#         request.POST = simple data given through
#         files=request.FILES = files such instance of video, photo etc given through
#         """
#         if form.is_valid():   
#             FilmModel.objects.create(
#                 name=form.cleaned_data.get("name"),
#                 poster=form.cleaned_data.get("poster"),
#                 video=form.cleaned_data.get("video"),
#                 rating=form.cleaned_data.get("rating"),
#                 pub_date=form.cleaned_data.get("pub_date"),
#                 views_count=form.cleaned_data.get("views_count"),
#                 about=form.cleaned_data.get("about"),
#             )
            
#     """ 
#     context = {
#         'form': FilmForm()
#     }
#     """
#     return render(request,'create-film.html',context)
class CreateView(generic.View):
    def get(self,request,*args, **kwargs):
        form=FilmForm()   
        context={
        'form': form,
         }
        return render(request,'create-film.html',context)
    
    def post(self,request,*args, **kwargs):
        
        form=FilmForm(request.POST, files=request.FILES)
          
        # context = {
        #         'form': form
        #         }
          
        """
        request.POST = simple data given through
        files=request.FILES = files such instance of video, photo etc given through
        """
        if form.is_valid():   
            # FilmModel.objects.create(
            # name=form.cleaned_data.get("name"),
            # poster=form.cleaned_data.get("poster"),
            # video=form.cleaned_data.get("video"),
            # rating=form.cleaned_data.get("rating"),
            # pub_date=form.cleaned_data.get("pub_date"),
            # views_count=form.cleaned_data.get("views_count"),
            # about=form.cleaned_data.get("about"),
            # )
        # you can also write in this form 
            name=form.cleaned_data.get("name")
            poster=form.cleaned_data.get("poster")
            video=form.cleaned_data.get("video")
            rating=form.cleaned_data.get("rating")
            pub_date=form.cleaned_data.get("pub_date")
            views_count=form.cleaned_data.get("views_count")
            about=form.cleaned_data.get("about")
            
            film = FilmModel.objects.create(
                name=name,
                poster=poster,
                video=video,
                rating=rating,
                pub_date=pub_date,
                views_count=views_count,
                about=about
            ) 
            
        # context = {
        #         'form': form
        #         }   
    
        return redirect('app_film:index')
    
    
    # users = User.objects.all()
    # films = FilmModel.objects.all()
    
    
    # context={
    #     'title': 'Index Page',
    #     'name': 'Hello World',
    #     'text':'I am learning django',
    #     'students':['stud1','stud2','stud3'],
    #     'numbers':[1,2,9,3,7,6,5,8],
    #     'users'  : users, 
    #     'films' :films, 
    # }
    # # POST request
    # sum=''
    # if request.method=='POST':
    #     # print(request.POST)
    #     f=request.POST.get('first') #bir 
    #     s=request.POST.get('second') #iki
    #     sum= f + ' ' + s
        
    # context['sum']=sum
        
       
    
    

    #pull data from database
    #transform
    #send email

# Create your views here.

