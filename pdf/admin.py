from django.contrib import admin
from .models import Profile
# Register your models here.

class Cvshow(admin.ModelAdmin):
    list_display= ('name','title', 'email', 'phone',)

admin.site.register(Profile, Cvshow)