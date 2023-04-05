from django.db import models

# Create your models here.
class Announcements(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    paragraph = models.TextField()


class Comment(models.Model):
    email = models.EmailField()
    comment = models.TextField()