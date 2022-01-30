from django.db import models
from django.utils.timezone import now
# Create your models here.

#contact model

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=150)
    message = models.TextField()
    time = models.DateTimeField(default= now)
    def __str__(self):
        return self.firstName