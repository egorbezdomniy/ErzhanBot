from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.PodBrand)
admin.site.register(models.Pod)

admin.site.register(models.Snus)
admin.site.register(models.SnusBrand)

admin.site.register(models.Single)
admin.site.register(models.SingleBrand)

admin.site.register(models.Consumable)
admin.site.register(models.ConsumablesBrand)

admin.site.register(models.Liquid)
admin.site.register(models.LiquidBrand)


