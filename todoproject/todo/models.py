from django.db import models

# Create your models here.

PRIORITY = (('danger','high'),('info','normal'),('success','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )

    duedate = models.DateField()

    def __str__(self):
        return self.title