from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, "generator/home.html", {"password": "liangchen"})


def password(request):
    password = ""
    characters = list("abcdefghijklmnopqrstuvwxyz")
    length = 10
    thepassword = ""
    for x in range(length):
        password += random.choice(characters)

    return render(request, "generator/password.html", {"password": password})
