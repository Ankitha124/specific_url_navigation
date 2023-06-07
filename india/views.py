from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sewhag(request):
    return render(request,'sewhag.html')

def akt(request):
    return HttpResponse('<h1> This String response')

