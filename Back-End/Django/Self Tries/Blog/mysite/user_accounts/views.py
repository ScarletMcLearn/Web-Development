from django.shortcuts import render

from .models import *

# Create your views here.
def openLoginPage(request):
    return render (request, 'user_accounts/login.html')


def checkUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        Login.objects.get(username=username, password=password)
        return render (request, 'user_accounts/welcome.html', )
    except Login.DoesNotExist:
        return render (request, 'user_accounts/login.html', {'error': 'Invalid User', })
