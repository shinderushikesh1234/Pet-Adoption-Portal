from django.db import models
from django.contrib.auth.models import User
class pet(models.Model):
    image=models.ImageField( upload_to="pets/",)
    Name=models.TextField()
    Location=models.TextField()
    Breed=models.TextField()
    description=models.TextField()
    status=models.TextField(default="Available")
    def __str__(self):
        return self.Name
class petadopted(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Pet=models.OneToOneField(pet, on_delete=models.CASCADE)    
