from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id':1,'name':"Let's learn Python"},
    {'id':2,'name':"Let's learn Java script"},
    {'id':1,'name':"Let's learn web Developmant"}

]

def hello(request):
    context = {'room':rooms}
    return render(request,'hello.html',context)

