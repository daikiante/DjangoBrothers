from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    upload_at = models.DateTimeField(auto_now_add=True)