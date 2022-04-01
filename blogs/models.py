from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
CONTENT_TYPE = (
    ("long", "Long"),
    ("short", "Short"),

)
#category modle
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField( max_length=150)
    description = models.TextField()
    url = models.CharField( max_length=150)
    image = models.URLField(max_length=350)
    timestamp = models.DateTimeField( auto_now_add=True , null=True)

    def __str__(self):
        return self.title

#post modle

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField( max_length=150)
    description = models.TextField()
    content = HTMLField()
    url = models.CharField( max_length=150)
    cType = models.CharField(
        max_length = 20,
        choices = CONTENT_TYPE,
        default = 'long'
        )
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.URLField(max_length=350)
    upload_time = models.DateTimeField(default= now)
    authorNmae = models.CharField( max_length=150)
    authorDescs = models.TextField()
    authorImage = models.CharField( max_length=250)
    tags = models.TextField()
    def __str__(self):
        return self.title

#blog comment

class blogpostComment(models.Model):
    IDno = models.AutoField(primary_key=True )
    comments = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null= True)
    timestamp = models.DateTimeField(default= now)
    def __str__(self):
        return self.comments[0:15] + "....."  + ' by ' + self.user.username