from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, "board/index.html")

def register(req):
    return render(req, "board/register.html")

def login(req):
    return render(req, "board/login.html")