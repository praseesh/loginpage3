from django.shortcuts import redirect, render
from django.contrib.auth import authenticate

def home(request):
    
    return render(request, 'home.html')

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
 
