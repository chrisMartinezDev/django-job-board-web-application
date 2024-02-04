from django.shortcuts import render, HttpResponse

# Create your views here.

def HomePage(request):
    return render(request, "index.html")

def JobListings(request):
    return render(request, "index.html")