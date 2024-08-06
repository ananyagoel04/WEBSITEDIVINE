"""
URL configuration for djangoweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from djangoweb import views

admin.site.site_header ="DIVINE WISDOM"
admin.site.site_title = "DWS-COMMITTED TO EXCELLENCE IN EDUCATION"
admin.site.index_title = "Divine Wisdom Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('parent/', views.parent),
    path('about/', views.aboutpage,name='about',),
    path('contact/', views.contact),
    path('gallery/', views.gallerypage),
    path('admissions/', views.admission),
    path('Personal Growth and Development/', views.personal),
    path('Effective Interpersonal Skills/', views.effective),
    path('Effective Communication Skills/', views.Communication),
    path('Deepened Spiritual Values/', views.Deepened),
    path('Intellectual Growth/', views.Intellectual),
    path('Respond Aesthetically/', views.Respond),
    path('Prepare for Occupation/', views.Occupation),
    path('Social Responsibility/', views.Responsibility),
    path('Infrastructure/', views.Infrastructure),
    path('Club/', views.Club),
    path('Cbse/', views.Cbse),
    path('Tc/', views.test_view, name='test_view'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)