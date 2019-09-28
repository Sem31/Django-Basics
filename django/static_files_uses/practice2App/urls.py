from django.conf.urls import url
from practice2App import views
from django.urls import path

urlpatterns = [
    path('',views.index)
]