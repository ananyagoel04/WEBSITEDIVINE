from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from gallery.models import Gallery, maingallery
from about.models import aboutimg, about
from TC.models import Session, Class, Student
from Parents.models import Event, News



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


def send_form_data_email(name, email, phone, resume, message):
    subject = "Resume"
    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    sender_name = "DIVINE WISDOM"
    sender_email = "info@divinewisdomschool.in"
    email_message = EmailMessage(
        subject,
        body,
        f'{sender_name} <{sender_email}>',
        ["ananyagoelps@gmail.com"],
        reply_to=[email],
    )

    # Attach the resume file to the email
    if resume:
        email_message.attach(resume.name, resume.read(), resume.content_type)

    # Send the email
    email_message.send()


def home(request):
    # send_email_example()
    return render (request,"index.html")
def logo(request):
    return render (request,"logo.html")
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
    return render (request,"admissions.html")
def personal(request):
    return render (request,"Personal Growth and Development.html")
def effective(request):
    return render (request,"Effective Interpersonal Skills.html")
def Communication(request):
    return render (request,"Effective Communication Skills.html")
def Deepened(request):
    return render (request,"Deepened Spiritual Values.html")
def Intellectual(request):
    return render (request,"Intellectual Growth.html")
def Respond(request):
    return render (request,"Respond Aesthetically.html")
def Occupation(request):
    return render (request,"Prepare for Occupation.html")
def Responsibility(request):
    return render (request,"Social Responsibility.html")
def Infrastructure(request):
    return render (request,"Infrastructure.html")
def Club(request):
    return render (request,"Clubs.html")
def Cbse(request):
    return render (request,"Cbse.html")
def test(request):
    return render (request,"Test.html")

def aboutpage(request):
    aboutimgdata = aboutimg.objects.all()[:6]
    about_data = [{'title': obj.image_title, 'url': obj.get_image_url()} for obj in aboutimgdata]
    objects = about.objects.all()
    objectsurl = [about_obj.get_pdf_url() for about_obj in objects]

    data = {'objects': objectsurl,
            'aboutimg':about_data,
            }

    if request.method == 'POST':
        name = request.POST.get('Name', '')
        email = request.POST.get('Email', '')
        phone = request.POST.get('Phone', '')
        resume = request.FILES.get('Resume', None)
        message = request.POST.get('Message', '')

        # Validate the input data before sending the email.
        if name and email and resume:
            # Call the function to send form data as an email
            send_form_data_email(name, email, phone, resume, message)

            # Show success message
            return render(request, 'About.html', {'objects': objectsurl, 'success_message': True})

    return render(request, 'About.html', data)




def send_contact(name, email, phone, message):
    subject = "MESSAGE FROM WEBSITE"
    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    sender_name = "DIVINE WISDOM"
    sender_email = "info@divinewisdomschool.in"
    email_message = EmailMessage(
        subject,
        body,
        f'{sender_name} <{sender_email}>',
        ["receptiondivinewisdom@gmail.com"],
        reply_to=[email],
    )

    # Send the email
    email_message.send()
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name', '')
        email = request.POST.get('Email', '')
        phone = request.POST.get('Phone', '')
        message = request.POST.get('Message', '')

        # Validate the input data before sending the email.
        if name and email:
            # Call the function to send form data as an email
            send_contact(name, email, phone, message)

            # Show success message
            return render(request, 'contactus.html', {'success_message': True})
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
