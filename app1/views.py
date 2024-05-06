from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    return HttpResponse('hello world')

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:    
            return render (request, 'home.html')
        else:
            return redirect('login_user')
    return ('login_user')

def logout(request):
    pass