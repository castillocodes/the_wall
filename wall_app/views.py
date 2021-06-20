from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request, "index.html")

def success(request):
    if 'user' not in request.sesssion:
        return redirect('/')
    context = {
        'wall_messages': Wall_Message.objects.all()
    }
    return render(request, "success.html", context)