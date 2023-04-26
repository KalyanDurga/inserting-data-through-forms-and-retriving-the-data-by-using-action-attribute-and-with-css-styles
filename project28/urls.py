"""project28 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),


    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_accessrecord/',insert_accessrecord,name='insert_accessrecord'),



    path('retrive_topic/',retrive_topic,name='retrive_topic'),
    path('retrive_topic_checkbox/',retrive_topic_checkbox,name='retrive_topic_checkbox'),
    path('retrive_topic_radio/',retrive_topic_radio,name='retrive_topic_radio'),



    path('retrive_webpage/',retrive_webpage,name='retrive_webpage'),
    path('retrive_webpage_checkbox/',retrive_webpage_checkbox,name='retrive_webpage_checkbox'),
    path('retrive_webpage_radio/',retrive_webpage_radio,name='retrive_webpage_radio'),



    path('retrive_accessrecord/',retrive_accessrecord,name='retrive_accessrecord'),
    path('retrive_accessrecord_checkbox/',retrive_accessrecord_checkbox,name='retrive_accessrecord_checkbox'),
    path('retrive_accessrecord_radio/',retrive_accessrecord_radio,name='retrive_accessrecord_radio'),

    path('update_topic/',update_topic,name='update_topic'),

]
