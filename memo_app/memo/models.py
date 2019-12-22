from django.db import models

class Memo(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='Photos')
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title