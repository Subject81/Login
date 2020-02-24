from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):

    return render(request,"index.html")

def new(request):
    return render(request,'welcome.html')

def create(request):
    print(request.POST)
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],password=request.POST['password'],confirm=request.POST['confirm'])
    return redirect('/')



def welcome(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['user'])
            }
    return render(request,'welcome.html',context)

def registration(request):
    #basic_validator is from class UserManager
    #                               def basic_validaotor....
    errors = User.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) >0:
        #errors is a variable set at the top of this function
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
        #hashes pw and encrypts
    pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser =  User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],password=pwhash)#this is special for password due to bcrypt(pwhash is a variable)
    request.session['user'] = newUser.id
    return redirect('/welcome')
    print(pwhash)
    print(request.POST)
    
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print(request.POST)
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user'] = user.id
    print(request.session['user'])
    print(User.objects.get(id=request.session['user']).first_name)
    return redirect('/welcome')

def logout(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        request.session.clear()
    return redirect('/')