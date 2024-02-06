from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
def home(request):
    return render (request,"index.html")
def logo(request):
    return render (request,"logo.html")
def parent(request):
    return render (request,"parent.html")