from django.contrib import admin
from AppTwo.models import Topic, Webpage, AccessRecord, Users
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Users)
