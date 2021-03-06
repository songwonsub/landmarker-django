"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.landmarker, name='landmarker')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='landmarker')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from View.home import home

urlpatterns = [
    path('landmarker/', home.home, name='home'),
    path('landmarker/main.do', home.main, name='main'),
    path('landmarker/error404.do', home.error404, name='error404'),
    path('landmarker/about.do', home.about, name='about'),
    path('landmarker/contact.do', home.contact, name='contact'),
    path('landmarker/propertyAgent.do', home.propertyAgent, name='propertyAgent'),
    path('landmarker/propertyList.do', home.propertyList, name='propertyList'),
    path('landmarker/propertyType.do', home.propertyType, name='propertyType'),
    path('landmarker/testImonial.do', home.testImonial, name='testImonial'),
]
