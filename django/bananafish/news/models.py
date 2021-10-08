from django.db import models


# Create your models here.

class Banana(models.Model):
    name = models.CharField(max_length=150)
    wiki = models.TextField(blank=True)
    photos = models.ImageField(upload_to='photos/%Y/%m/%d')
    life = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
