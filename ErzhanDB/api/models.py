from django.db import models


# Create your models here.




class Liquid(models.Model):
    CHOICES = (
        ('HotSpot', 'HotSpot'),
        ('Psycho', 'Psycho')
    )
    brand = models.CharField(max_length=64, choices=CHOICES)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Pod(models.Model):
    CHOICES = (
        ('HotSpot', 'HotSpot'),
        ('Psycho', 'Psycho')
    )
    brand = models.CharField(max_length=64, choices=CHOICES)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class SingleUse(models.Model):
    CHOICES = (
        ('HotSpot', 'HotSpot'),
        ('Psycho', 'Psycho')
    )
    brand = models.CharField(max_length=64, choices=CHOICES)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Snus(models.Model):
    CHOICES = (
        ('HotSpot', 'HotSpot'),
        ('Psycho', 'Psycho')
    )
    brand = models.CharField(max_length=64, choices=CHOICES)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Consumable(models.Model):
    CHOICES = (
        ('HotSpot', 'HotSpot'),
        ('Psycho', 'Psycho')
    )
    brand = models.CharField(max_length=64, choices=CHOICES)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

