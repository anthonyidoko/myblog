from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    email = models.EmailField()
    date_added = models.DateTimeField(default=datetime.now,null=True)

    def __str__(self):
        return self.title

class Entry(models.Model):
    article = models.ForeignKey("Article",on_delete=models.CASCADE)
    text = models.TextField()
    photo = models.ImageField(upload_to="images", blank=True, null=True)
    photo_description = models.CharField(max_length=500,blank =True,null=True)
    date_added = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.text
