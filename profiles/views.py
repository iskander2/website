from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect
from .forms import SignupForm,CommentForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def add_comment(request,pk):
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():    
            comment =form.save(commit=False)
            comment.user =request.user
            comment.save()
    return redirect('app:detail',pk=pk)