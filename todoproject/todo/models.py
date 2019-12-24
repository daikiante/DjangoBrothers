from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title