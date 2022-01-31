from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
# Create your views here.


def contact(request):
    if request.method == "POST":
        Fname = request.POST['name']
        Lname = request.POST['lastName']
        mobile = request.POST['mobile']
        email = request.POST['email']
        message = request.POST['message']
        contacts = Contact(firstName= Fname, lastName= Lname, email= email, mobile= mobile, message= message)
        contacts.save()
        messages.info(request, "Your message has been delivered to forn bits")
        return redirect('contact')
    else:
        return render(request, 'contact.html')
