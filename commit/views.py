from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


def cenima_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('readmovie')
    else:
        form = MovieForm()
    return render(request, 'create.html', {'form': form})

def cenima_read(request):
    movie_list= Movie.objects.all()
    return render(request,'retrieve.html',{'movie_list':movie_list})

def cenima_update(request,pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST' :
        form = MovieForm(request.POST,instance=movie)
        if form.is_valid():
         form.save()
        return redirect('readmovie')
    else:
        form = MovieForm(instance=movie)
    return render(request,'update.html' , {'form':form})



def cenima_delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST' :
        movie.delete()
        return redirect('readmovie')
    
    return render(request,'delete.html' , {'movie':movie})


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return redirect('readmovie')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})




from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login 


def home_page(request):
    return render(request,'index.html') 

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('readmovie')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }
    return render(request, 'logout.html', context)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/login/')
def aboutUs(request):
    return render(request,'aboutUs.html')
