"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mysite import views

urlpatterns = [
    path('',views.homePage),
    path('admin/', admin.site.urls),
    path('contact/',views.contact,name='contact'),
    path('saveenquiry/',views.saveEnquiry,name='saveenquiry'),
    path('about/',views.about),
    path('form/',views.form),
    path('test/',views.test),
    path('calculator/',views.calculator),
    path('oddeven/',views.oddeven),
    path('marksheet/',views.marksheet),
    path('services/',views.services,name='services'),

    #path('newsdetails/<newsId>',views.newsDetails), sending data from slug instead of id
    path('newsdetails/<slug>',views.newsDetails),

    
    #path('contact/<int:intId>',views.int),
    #path('contact/<str:stringId>',views.string),
    path('contact/<slug:slugId>',views.slug),


    
]
