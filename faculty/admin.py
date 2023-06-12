from django.contrib import admin
from . import models
# register your models here.

admin.site.register(models.Department)
admin.site.register(models.InventoryCategory)
admin.site.register(models.InventorySubCategory)
admin.site.register(models.Faculty)
admin.site.register(models.Student)
admin.site.register(models.Projects)
admin.site.register(models.Domain)
admin.site.register(models.Inventory)
admin.site.register(models.Streams)
admin.site.register(models.InventoryStatus)
