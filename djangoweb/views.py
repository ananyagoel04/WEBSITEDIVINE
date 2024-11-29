from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from gallery.models import Gallery, maingallery
from about.models import aboutimg, about
from TC.models import Session, Class, Student
from Parents.models import Event, News
from home.models import Homeimg, VisionMission, Environment, Teacher, Program, Review

def class_students(request, class_id):
    # Get the class object based on class_id
    class_obj = get_object_or_404(Class, id=class_id)
    # Get all students in this class
    students = Student.objects.filter(class_obj=class_obj)
    
    # Render the template with the class and students data
    return render(request, 'class_students.html', {'class_obj': class_obj, 'students': students})

def Tc(request):
    sessions = Session.objects.order_by('session_name')
    return render(request, 'Tc.html', {'sessions': sessions})

def home(request):
    # Fetching data from the models
    homeimg = Homeimg.objects.first()
    vision_mission = VisionMission.objects.all()[:2]
    environment = Environment.objects.all()[:2]
    teachers = Teacher.objects.all()[:4]
    programs = Program.objects.all()  # Assuming multiple Program entries
    reviews = Review.objects.all()  # Assuming multiple Review entries

    # Passing data to the template
    context = {
        'homeimg': homeimg,
        'vision_mission': vision_mission,
        'environment': environment,
        'teachers': teachers,
        'programs': programs,
        'reviews': reviews,
    }
    return render(request, "index.html", context)

def logo(request):
    return render(request, "logo.html")

def parent(request):
    today = timezone.now().date()
    events = Event.objects.filter(date__gte=today).order_by('date')[:4]
    colors = ["#FDEECD", "#EAE1FC", "#FFEBEC", "#EAFDF7"]
    Newses = News.objects.all()
    
    colored_events = [
        {
            'event': event,
            'color': colors[i % len(colors)]
        }
        for i, event in enumerate(events)
    ]
    
    context = {
        'colored_events': colored_events,
        'newses': Newses,
    }
    return render(request, "parent.html", context)

def admission(request):
    return render(request, "admissions.html")

def personal(request):
    return render(request, "Personal Growth and Development.html")

def effective(request):
    return render(request, "Effective Interpersonal Skills.html")

def Communication(request):
    return render(request, "Effective Communication Skills.html")

def Deepened(request):
    return render(request, "Deepened Spiritual Values.html")

def Intellectual(request):
    return render(request, "Intellectual Growth.html")

def Respond(request):
    return render(request, "Respond Aesthetically.html")

def Occupation(request):
    return render(request, "Prepare for Occupation.html")

def Responsibility(request):
    return render(request, "Social Responsibility.html")

def Infrastructure(request):
    return render(request, "Infrastructure.html")

def Club(request):
    return render(request, "Clubs.html")

def Cbse(request):
    return render(request, "Cbse.html")

def test(request):
    return render(request, "Test.html")

def aboutpage(request):
    aboutimgdata = aboutimg.objects.all()[:6]
    about_data = [{'title': obj.image_title, 'url': obj.get_image_url()} for obj in aboutimgdata]
    objects = about.objects.all()
    objectsurl = [about_obj.get_pdf_url() for about_obj in objects]

    data = {
        'objects': objectsurl,
        'aboutimg': about_data,
    }

    return render(request, 'About.html', data)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name', '')
        email = request.POST.get('Email', '')
        phone = request.POST.get('Phone', '')
        message = request.POST.get('Message', '')

        # Validate the input data
        if name and email:
            # Show success message (without sending email)
            return render(request, 'contactus.html', {'success_message': True})
    return render(request, "contactus.html")

def gallerypage(request):
    galleryimgs = Gallery.objects.all()[:6]
    gallerytitle = Gallery.objects.values_list('image_title', flat=True)[:6]
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

    data = {
        'galleryimgs': gallery_urls,
        'gallerytitle': gallerytitle,
        'gallerytitle1': gallery_data,
        'count': total_entries
    }

    return render(request, 'gallery.html', data)
