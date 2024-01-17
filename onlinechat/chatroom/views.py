from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from . models import User, Contacts, Chat
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'chatroom/index.html', {
            "username": request.user
        })
    return render(request, 'chatroom/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        phonenumber = request.POST['phonenumber']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password, phonenumber=phonenumber)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "chatroom/login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, 'chatroom/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        phonenumber = request.POST['phonenumber']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'chatroom/register.html', {
                'message': 'Passwords must match.'
            })
        if phonenumber in User.objects.values_list('phonenumber', flat=True):
            return render(request, 'chatroom/register.html', {
                'message': 'Phonenumber already exists.'
            })
        try:
            user = User.objects.create_user(username, password)
            user.phonenumber = phonenumber
            user.save()
        except IntegrityError:
            return render(request, 'chatroom/register.html', {
                'message': 'Username already taken.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'chatroom/register.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def add(request):
    if request.method == 'POST':
        username = request.POST['username']
        phonenumber = request.POST['phonenumber']
        if username != request.user.username:
            user2 = User.objects.get(phonenumber=phonenumber, username=username)
            if user2:
                user1 = User.objects.get(username=request.user.username)
                data = Contacts(user1=user1, user2=user2)
                data.save()
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'chatroom/form.html')

def contacts(request):
    contacts = Contacts.objects.filter(user1=request.user) | Contacts.objects.filter(user2=request.user)
    return JsonResponse([contact.serialize() for contact in contacts], safe=False)

@csrf_exempt
def chat(request, otherUser):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        data = Chat(sender=request.user, reciever=otherUser, message=message)
        data.save()
    chats = Chat.objects.filter(sender=request.user, reciever=otherUser) | Chat.objects.filter(reciever=request.user, sender=otherUser)
    return JsonResponse([chat.serialize() for chat in chats], safe=False)

def contactinfo(request, username):
    return render(request, 'chatroom/contactinfo.html')

@login_required
def changeusername(request):
    if request.method == 'POST':
        newusername = request.POST['newusername']
        password = request.POST['password']
        user = authenticate(request, username=request.user.username, password=password)
        if user is not None:
            newUser = User.objects.get(username=request.user.username)
            newUser.username = newusername
            newUser.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'chatroom/username.html')