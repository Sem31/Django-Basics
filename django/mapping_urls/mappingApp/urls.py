from django.conf.urls import url
from django.urls import path
from mappingApp import views

urlpatterns = [
    path('',views.index1),
]