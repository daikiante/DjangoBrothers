from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    auther = models.CharField(max_length=100)
    images = models.ImageField(upload_to='既読')
    good = models.IntegerField()
    read = models.IntegerField()
    readtext = models.CharField(max_length=200)