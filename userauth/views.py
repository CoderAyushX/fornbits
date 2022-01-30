from tkinter import E
from django.contrib import auth, messages
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        user = auth.authenticate(username =username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/auth')
        else:
            messages.info(request,"User not exist")
            return redirect('login')
    else:
      return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        firstname = ""
        lastname = ""
        namelist = username.split()
        lname = namelist[len(namelist) - 1]
        if namelist[0] == lname:
            firstname += namelist[0]
            lastname += " "
        else:
            firstname += namelist[0]
            lastname += lname
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User name is taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email alredy in use")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                user.save()
                return render(request, 'login.html')

    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return render(request, 'nuser.html')

def editProfile(request):
    if request.method == 'POST':
        oldUsername = request.POST['oldusername']
        userName =  request.POST['username']
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        email = request.POST['email']
        print(oldUsername, userName ,firstName, lastName, email)
        if User.objects.filter(username=userName).exists() or User.objects.filter(email=email).exists():
            messages.info(request, "Username or email is taken")
            return render(request, 'editprofile.html')
        else:
            user = User.objects.get(username = oldUsername)
            user.username = userName
            user.first_name = firstName
            user.last_name = lastName
            user.email = email
            user.save()
            messages.info(request, "Profile updated")
            return render(request, 'editprofile.html')
    return render(request, 'editprofile.html')
def nproflie(request):
    return render(request, 'nuser.html')
