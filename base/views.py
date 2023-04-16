from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Genration_01,Genration_02,Genration_03,Genration_04



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')    
        password = request.POST.get('password')


        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, username = username, password = password )

        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request, 'username  or  Password does not exist')

    # context= {'messages':messages}
    return render(request,'base/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required(login_url  = 'login_page')
def homepage(request):
    place = Genration_01.objects.all()
    
    context = {'rooms':place}
    return render(request,'base/home_page.html',context)



@login_required(login_url  = 'login_page')
def family(request,slug):
    fam = Genration_01.objects.get(slug = slug)
    memb = Genration_02.objects.all()
    context = {'room':memb,'check':fam,'Male':'M','Female':'F'}
    return render(request,'base/appalanaidugaru.html',context)

# def room(request,pk):
#     room = None
#     for i in rooms:
#         if i['id'] == int(pk):
#             room = i
#     context = {'room':room}
#     return render(request,'base/room.html',context)



@login_required(login_url  = 'login_page')
def bro(request,slug):
    fam = Genration_02.objects.get(slug = slug)
    memb = Genration_03.objects.all()
    context = {'room':memb,'check':fam,'Male':'M','Female':'F','gen_code':'hello'}
    return render(request,'base/mahalaxminaidu.html',context)


@login_required(login_url  = 'login_page')
def sis(request,slug):
    fam = Genration_03.objects.get(slug = slug)
    memb = Genration_04.objects.all()
    context = {'room':memb,'check':fam,'gen_code':fam.gen_code}
    return render(request,'base/mahalaxminaidu.html',context)