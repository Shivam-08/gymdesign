from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime
from home.models import Contact
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'success.html')
        else:
            messages.success(request, 'Check the credentials!')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login')


def price(request):
    return render(request, 'pricing.html')

def handleSignup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #Check username
        if not username.isalnum():
            messages.warning(request, 'Username must be alphanumeric')
            return redirect('/signup')
        
        #Check password must be same
        if password1 != password2:
            messages.warning(request, 'Password must be same')
            return redirect('/signup')

        #Create user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, 'Your Account is Created.Check it by login below')
        return redirect('/login')    
    return render(request, 'signup.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name= name, email=email, phone=phone, desc=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Query has been Submitted!')
        return redirect('/contact')
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')