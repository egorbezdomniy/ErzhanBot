from django.db import models


class PodBrand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='podbrands/', null=True, blank=True)
    def __str__(self):
        return self.name


class SnusBrand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='podbrands/', null=True, blank=True)
    def __str__(self):
        return self.name


class SingleBrand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='podbrands/', null=True, blank=True)
    def __str__(self):
        return self.name


class ConsumablesBrand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='podbrands/', null=True, blank=True)
    def __str__(self):
        return self.name


class LiquidBrand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='podbrands/', null=True, blank=True)

    def __str__(self):
        return self.name


class Pod(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.PositiveIntegerField()
    brand = models.ForeignKey('PodBrand', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Snus(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.PositiveIntegerField()
    brand = models.ForeignKey('SnusBrand', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Single(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.PositiveIntegerField()
    brand = models.ForeignKey('SingleBrand', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Consumable(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.PositiveIntegerField()
    brand = models.ForeignKey('ConsumablesBrand', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Liquid(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.PositiveIntegerField()
    brand = models.ForeignKey('LiquidBrand', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

