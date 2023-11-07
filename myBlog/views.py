from typing import Any
from django.shortcuts import render, redirect
from .models import Post, Comment, AddArticle
from . forms import CommentForm, ArticleForm, RegisterForm, SignInForm
from myBlog.forms import UserCreationForm
from django.contrib.auth import login
from itertools import chain


def posts(request):
    home_page = True
    posts = Post.objects.all().order_by('-created')
    articles = AddArticle.objects.all().order_by('-created')

    all_entries = sorted(
        chain(posts, articles),
        key=lambda entry: entry.created,
        reverse=True 
    )

    return render(request, 'home.html', { 'home_page': home_page, 'all_entries': all_entries})

def info(request):
    return render(request, 'info.html')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'sign_up.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = RegisterForm()
        return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'sign_in.html', {'form': form})
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = SignInForm()
            return render(request, 'sign_in.html', {'form': form})


def post_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment')  
    else:
        form = CommentForm()

    comments = Comment.objects.all()
    return render(request, 'comment.html', {'form': form, 'comments': comments})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('home') 
    else:
        form = ArticleForm()
    
    return render(request, 'new_article_form.html', {'form': form}) 
