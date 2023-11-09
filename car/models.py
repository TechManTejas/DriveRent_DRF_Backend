from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='car_images/')
    details = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.company} {self.model} ({self.number})"
