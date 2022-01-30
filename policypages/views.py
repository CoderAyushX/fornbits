from django.shortcuts import render

# Create your views here.
def policy(request):    
    return render(request, 'policypages.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def terms(request):
    return render(request, 'terms.html') 

def disclaimer(request):
    return render(request, 'disclaimer.html')

def aboutus(request):
    return render(request, 'aboutus.html')