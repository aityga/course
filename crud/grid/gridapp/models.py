from django.db import models

# Create your models here.
class Employer(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField()
    contact = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.name} {self.email} {self.contact}"

    class Meta:
        db_table = "employers"