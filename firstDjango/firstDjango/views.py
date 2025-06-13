from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Django!  HOME")
    return render(request, 'websites/index.html')
    
def about(request):
    return HttpResponse("Hello Django!  ABOUT")

def contact(request):
    return HttpResponse("Hello Django!  CONTACT")