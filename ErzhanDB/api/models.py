from django.db import models

# Create your models here.
class Liquid(models.Model):
    CHOICES = (
        ('Hotspot', 'Hotspot'),
        ('Psycho', 'Psycho'),
    )
    brand = models.CharField(max_length=64, choices=CHOICES)
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name
