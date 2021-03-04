from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.title

class Entry(models.Model):
    article = models.ForeignKey("Article",on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.text

class Photo(models.Model):
    entry = models.ForeignKey("Entry", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="images")
    description = models.CharField(max_length=500)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.description
    
