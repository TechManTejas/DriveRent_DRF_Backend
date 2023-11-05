from django.db import models

class Car(models.Model):
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f"{self.company} {self.model} ({self.number})"
