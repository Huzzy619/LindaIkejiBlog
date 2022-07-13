from django.db import models
from django.conf import settings
# Create your models here.


class Post (models.Model):
   author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user' )
   title = models.CharField(max_length=500)
   date_updated = models.DateTimeField(auto_now=True)
   date_created = models.DateTimeField(auto_now_add=True)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to = 'post-pictures', )
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)