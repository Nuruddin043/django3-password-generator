from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def about(request):
    return render(request,'generator/about.html')

def home(request):
    return render(request,'generator/home.html')



def password(request):
    thepassword=''
    charecters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        charecters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        charecters.extend(list('0123456789'))
    length=int(request.GET.get('length',12))

    for x in range(length):
        thepassword+=random.choice(charecters)
    return render(request,'generator/password.html',{'password':thepassword})
