from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, "generator/home.html", {"password": "liangchen"})


def password(request):
    password = ""
    characters = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("Specialcharacters"):
        characters.extend(list("!@#$%^&*()"))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    length = int(request.GET.get("length"), 12)
    for x in range(length):
        password += random.choice(characters)

    return render(request, "generator/password.html", {"password": password})


def about(request):
    return render(request, "generator/about.html")
