from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Liquid)
admin.site.register(models.Pod)
admin.site.register(models.SingleUse)
admin.site.register(models.Snus)
admin.site.register(models.Consumable)

