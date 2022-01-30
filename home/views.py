from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def index(request):    
    return render(request, 'index.html')