"""ManyToMany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('addsub/',views.addsub,name='addsub'),
    path('savesub/',views.savesub,name='savesub'),
    path('dissub/',views.displaysub,name='displaysub'),
    path('deletesub/',views.deletesub,name='deletesub'),
    path('updatesub/',views.updatesubject,name='updatesub'),
    path('updatesave/',views.updatesave,name='updatesave'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('savestudent/',views.savestudent,name='savestudent'),
    path('disstudent/',views.displaystudent,name='displaystudent'),
    path('delete/',views.deletestudent,name='delete'),

]
