from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import user_form
from .models import user_model

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def Aboutpage(request):
    return render(request,'about.html')

def contact(request):
    return render(request, "contact.html")


def savedemo(request):
    if request.method=="POST":
        data=user_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect("/")
    else:
        fm=user_form()
        return render(request,'showform.html',{'form':fm})

def displaydata(request):
    data=user_model.objects.all()
    return render(request,'display.html',{'res':data})

def edit(request,id):
    data=user_model.objects.get(id=id)
    return render(request,'edit.html',{'res':data})

def updatedata(request,id):
    emp=user_model.objects.get(id=id)
    data=user_form(request.POST,instance=emp)
    if data.is_valid():
        data.save()
        return redirect("/display")

def deletedata(request,id):
    data=user_model.objects.get(id=id)
    data.delete()
    return redirect("/display")

