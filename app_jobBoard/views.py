from django.shortcuts import render, HttpResponse

# Create your views here.

def HomePage(request):
    return render(request, "base.html")