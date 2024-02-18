from django.http import HttpResponse,HttpResponseRedirect
from gallery.models import Gallery
from gallery.models import maingallery
from about.models import about
from django.shortcuts import render,redirect
def home(request):
    return render (request,"index.html")
def logo(request):
    return render (request,"logo.html")
def parent(request):
    return render (request,"parent.html")
def aboutpage(request):
    aboutdata = about.objects.all()[:6]
    data={
        'aboutdata':aboutdata
    }
    return render (request,'About.html',data)

def contact(request):
    return render (request,"contactus.html")
# def gallerypage(request):
#     galleryimgs = Gallery.objects.values_list('image',flat=True)[:6]
    # gallerytitle = Gallery.objects.values_list('image_title',flat=True)[:6]
#     # datagallery = Gallery.objects.get()
#     # data={

#     # }
#     return render(request, 'gallery.html', {'galleryimgs': galleryimgs}, )

def gallerypage(request):
    galleryimgs = Gallery.objects.values_list('image',flat=True)[:6]
    gallerytitle = Gallery.objects.values_list('image_title',flat=True)[:6]
    gallerytitle1 = maingallery.objects.all()
    total_entries = maingallery.objects.count()
    data={
        'galleryimgs':galleryimgs,
        'gallerytitle':gallerytitle,
        'gallerytitle1':gallerytitle1,
        'count':total_entries
    }
    return render(request, 'gallery.html',data)
