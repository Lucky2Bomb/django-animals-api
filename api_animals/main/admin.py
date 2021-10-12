from django.contrib import admin

from . import models


class MoveTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
    ordering=("id",)


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
    ordering=("id",)


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'domesticated', 'lifetime', 'weight', 'height', 'number_of_individuals',
              'description', 'image', 'family_id', 'move_type_id', 'protection_status_id')
    
    ordering=("id",)


class ProtectionStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
    ordering=("id",)




admin.site.register(models.MoveType, MoveTypeAdmin)
admin.site.register(models.Family, FamilyAdmin)
admin.site.register(models.Animal, AnimalAdmin)
admin.site.register(models.ProtectionStatus, ProtectionStatusAdmin)
