from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Announcements, Comment
from datetime import date

def announcements(request):
    announcements = Announcements.objects.all()
    if request.user.is_superuser:
        admin = 'SUIII'
        return render(request, 'announcements.html', {'announcements': announcements, 'admin':admin})
    else:
        return render(request, 'announcements.html', {'announcements': announcements})

def add(request):
    if request.method == "POST":
        title = request.POST['title']
        paragraph = request.POST['paragraph']
        new = Announcements.objects.create(title=title, paragraph=paragraph)
        return redirect('announcements')
    return render(request, 'add.html')

def main(request):
    if request.method == "POST":
        email = request.POST['email']
        comment = request.POST['comment']
        new = Comment.objects.create(email=email, comment=comment)
        return render(request, 'main.html', {'sent': 'SUIII'})
    return render(request, 'main.html')

def ourteam(request):
    return render(request, 'ourteam.html')

def header(request):
    return render(request, 'header.html')

# auth
def signupsystem(request):
    if request.method == "GET":
        return render(request, 'signupsystem.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'signupsystem.html',
                          {'form': UserCreationForm, 'error': 'Passwords don\'t match!'})
        else:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('announcements')
            except IntegrityError:
                return render(request, 'signupsystem.html',
                              {'form': UserCreationForm, 'error': 'Username is already taken!'})


def loginsystem(request):
    if request.method == "GET":
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('announcements')
        else:
            return render(request, 'login.html',
                          {'form': AuthenticationForm, 'error': 'Неверный логин и/или пароль'})

@login_required
def logoutsystem(request):
    if request.method == "GET":
        logout(request)
        return redirect('main')