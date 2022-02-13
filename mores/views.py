from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Rate,Feedback,whatsnew
# Create your views here.
def more(request):
    return render(request, 'more.html')

def editpro(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    return render(request, 'editprofile.html')

def rateus(request):
    if request.method == "POST":
        star = request.POST.get('star5')
        star2 = request.POST.get('star4')
        star3 = request.POST.get('star3')
        star4 = request.POST.get('star2')
        star5 = request.POST.get('star1')
        if star == "on":
            rate = Rate(stars= "1 star")
            rate.save()
        elif star2 == "on":
            rate = Rate(stars= "2 star")
            rate.save()
        elif star3 == "on":
            rate = Rate(stars= "3 star")
            rate.save()
        elif star4 == "on":
            rate = Rate(stars= "4 star")
            rate.save()
        elif star5 == "on":
            rate = Rate(stars= "5 star")
            rate.save()

        return redirect('more')
    return render(request, 'rateus.html')

def feedback(request):
    if request.method == "POST":
        sender = request.POST.get('sender')
        message = request.POST.get('message')
        feedback = Feedback(sender= sender, message= message)
        feedback.save()
        messages.info(request, "Your feedback has been delivered to forn bits")
        return redirect('feedback')
        
    return render(request, 'feedback.html')

def update(request):
    updates = whatsnew.objects.all().first()
    print(updates)
    return render(request, 'updates.html', {'updates' : updates})

def error_404(request, exception):
    return render(request, '404.html')
    
def error_500(request):
    return render(request, '500.html')