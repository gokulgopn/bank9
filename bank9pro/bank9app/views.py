from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('loginn')
        else:
            messages.info(request, "Password not matching|")
            return redirect('register')
        # return redirect('/')
    return render(request, 'register.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('loginn')
    return render(request, 'login.html')

def new(request):
    return render(request, 'new.html')

def form(request):
    return render(request, 'form.html')

def final(request):
    return render(request, 'final.html')

def home(request):
    return render(request, 'home.html')

def redirect_idukki(request):
    return redirect("https://en.wikipedia.org/wiki/Idukki_district")
def redirect_kottayam(request):
    return redirect("https://en.wikipedia.org/wiki/Kottayam")
def redirect_malappuram(request):
    return redirect("https://en.wikipedia.org/wiki/Malappuram")
def redirect_palakkad(request):
    return redirect("https://en.wikipedia.org/wiki/Palakkad")
def redirect_kochi(request):
    return redirect("https://en.wikipedia.org/wiki/Kochi")
