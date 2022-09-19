from pipes import Template
import re
from django.shortcuts import render,redirect
from .forms import AuthenticationForm,UserForm,PostForm
from .models import User,Post,UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    posts = Post.objects.all()
    profiles = UserProfile.objects.all()
    form = PostForm()
    
    if request.user.is_authenticated:
      profile = request.user.userprofile
    if request.method == 'POST':
         form = PostForm(request.POST)
         if form.is_valid():
           post = form.save(commit=False)
           post.author = profile
           post.save()
         return redirect('home')

    context = {'posts':posts,
               'profiles':profiles,
               'form':form}
    return render(request,'core/home.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')

        else:
             messages.error(request, 'Username or password does not exist')

    context = {'form':form}
    return render(request, 'core/login.html', context)

def registerPage(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request,user)
            return redirect('home')

        else:
             messages.error(request, 'An error has occured during registration')

    context = {'form':form}
    return render(request, 'core/register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def profilePage(request,user_id):
    profile = UserProfile.objects.get(user_id=user_id)
    context = {'profile':profile}
    return render(request,'core/profile.html',context)