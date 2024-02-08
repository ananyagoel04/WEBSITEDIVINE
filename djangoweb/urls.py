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
from djangoweb import views

admin.site.site_header ="DIVINE WISDOM"
admin.site.site_title = "DWS-COMMITTED TO EXCELLENCE IN EDUCATION"
admin.site.index_title = "Welcome to DWS Admin panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('parent/', views.parent),
    path('about/', views.about),
    path('contact/', views.contact),
    path('gallery/', views.gallery),
]
