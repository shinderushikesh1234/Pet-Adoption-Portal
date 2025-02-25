from django.contrib import admin
from .models import pet,petadopted
@admin.register(pet)
class petAdmin(admin.ModelAdmin):
    list_display = ['id']
@admin.register(petadopted)
class PetadoptedAdmin(admin.ModelAdmin):
    list_display = ['id']
