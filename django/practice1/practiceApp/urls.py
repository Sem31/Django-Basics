from django.conf.urls import url
from practiceApp import views
from django.urls import path

urlpatterns = [
    path('',views.temp),
]