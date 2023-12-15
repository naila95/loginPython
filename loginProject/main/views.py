from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User

# Create your views here.


def login(request):
    return render(request, "main/login.html")


def block_user(request,id):
    
    data = User.objects.get(id=id)
    data.is_active = False
    data.save()
    messages.info(request,data.username+" blok edildi")
    
    return redirect("profile")


def activate_user(request,id):
    
    data = User.objects.get(id=id)
    data.is_active = True
    data.save()
    messages.info(request,data.username+" aktiv edildi")
    
    return redirect("profile")