from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from account.models import Account
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
# Create your views here.
def register(request):
    if request.method=='POST':
        #HTML-den gelen melumatlar
        username=request.POST.get('username')
        password=request.POST.get('password')
        avatar=request.FILES.get('avatar')
        
        """ 
        request.POST = {
            'username': 'telman'
            'password': 'telman12345'
        }
        
        request.POST = {
            'avatar': 'photo.png'
        }
        """
        
        if username and password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                username=username,
                password=password,
            )
                
                Account.objects.create(
                user=user,
                avatar=avatar,
            )
                messages.success(request,'User created')
                return redirect('app_film:index')
                     
            else:
                messages.info(request,'Please, use another username')
        else:
            if not username:
                
                messages.info(request,'Please enter username')
            if not password:
                messages.info(request,'Please enter password')
            # if not avatar:
            #     messages.info(request,'Please choose an avatar')                        
    return render(request,'register.html')

def loginUser(request):
    if request.method=='POST':
        username=username.POST.get('username')
        password=password.POST.get('password')
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,'you logged in')
            
        else:
            messages.info(request,'Please enter correct username and password')
        
        return redirect('app_film:index')     
    return render(request, 'login.html')

def logoutUser(request):
    
    logout(request)
    
    return redirect('account:login')
    
    
    
            
            
