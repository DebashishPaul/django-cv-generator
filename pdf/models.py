from django.db import models

# Create your models here.
class Profile(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(max_length=254)
    about = models.TextField(max_length = 1000)
    previous_work = models.TextField()
    phone = models.IntegerField()
    university = models.CharField(max_length=100, blank=True, null=True)
    facebook_url = models.URLField(max_length=200)