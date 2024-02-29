from django.http import HttpResponse,HttpResponseRedirect
from gallery.models import Gallery, maingallery
from django.shortcuts import render,redirect
from about.models import about
from django.core.mail import send_mail, EmailMessage





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
    return render (request,"parent.html")

def aboutpage(request):
    objects = about.objects.all()
    objectsurl = [about_obj.get_pdf_url() for about_obj in objects]

    data = {'objects': objectsurl}

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
