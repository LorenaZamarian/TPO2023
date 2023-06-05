from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
def index_administracion(request):
    variable='test variable'
    return render (request, 'administracion/index_administracion.html',{'variable':variable})

def base(request):
    return render(request, 'administracion/base.html')

def signin(request):
    return render(request, 'administracion/signin.html', {
        'form': AuthenticationForm,
        'error': 'Username and Password do not match'
    })

def signup(request):
    if request.method == 'GET':
        return render(request, 'administracion/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                        password=request.POST['password1'])
                user.save()
                return HttpResponse('User created successfully')
            except:
                return render(request, 'administracion/singup.html', {
                'form': UserCreationForm,
                'error': 'Username already exists'
            })
        return render(request, 'administracion/singup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })
                

def signout(request):
    return render(request, 'signout.html')