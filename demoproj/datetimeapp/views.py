from django.shortcuts import render
from .models import User
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    context={'datetime':now}
    return render(request, 'current_datetime.html', context)

def homes(request):
    return render(request, 'homes.html')

def userreg(request):
    return render(request, "userreg.html",{})

def insertuser(request):
    vuid=request.POST['tuid'];
    vuname=request.POST['tuname'];
    vuemail=request.POST['tuemail'];
    vucontact=request.POST['tucontact'];
    us=User(uid=vuid, uname=vuname, uemail=vuemail, ucontact=vucontact);
    us.save();
    return render(request, 'current_datetime.html',{})
