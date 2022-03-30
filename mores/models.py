from email import message
from django.db import models
from tinymce.models import HTMLField
from django.utils.timezone import now
# Create your models here.

#rate us model
class Rate(models.Model):
    stars = models.CharField(max_length=10)
    def __str__(self):
        return self.stars

class Feedback(models.Model):
    sender = models.CharField(max_length=150)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.sender

class whatsnew(models.Model):
    update = HTMLField()
    upload_time = models.DateTimeField(default= now)
    def __str__(self):
        return self.update[ :20]
class Writeblog(models.Model):
    content =  HTMLField()
    upload_time = models.DateTimeField(default= now)