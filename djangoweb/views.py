from django.http import HttpResponse,HttpResponseRedirect
from gallery.models import Gallery, maingallery
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
    galleryimgs = Gallery.objects.all()[:6]
    gallerytitle = Gallery.objects.values_list('image_title',flat=True)[:6]
    gallerytitle1_instances = maingallery.objects.all()
    total_entries = maingallery.objects.count()
    gallery_urls = [galleryimgs.get_image_url() for galleryimgs in galleryimgs]
    gallery_data = []
    for gallery_instance in gallerytitle1_instances:
        instance_data = {
            'image_url1': gallery_instance.get_image_url1(),
            'image_title1': gallery_instance.image_title1,
            'image_filter1': gallery_instance.imagefilter1,
            # Add other fields as needed
        }
        gallery_data.append(instance_data)    
    data={
        'galleryimgs':gallery_urls,
        'gallerytitle':gallerytitle,
        'gallerytitle1':gallery_data,
        'count':total_entries
    }
    return render(request, 'gallery.html',data)
