from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=140)
    create_at = models.DateTimeField(auto_now_add=True)