from django.contrib import admin
from first_app.models import Topic,Webpages,AccessRecords

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpages)
admin.site.register(AccessRecords)
