from django.db import models

# Create your models here.
class Car(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30)

    #String Representation of the model
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"