from django.db import models


class PlantDisease(models.Model):
    name = models.CharField(max_length=255, unique=True)
    symptoms = models.TextField()
    cause = models.TextField()
    treatment = models.TextField()
    prevention = models.TextField()
    image = models.ImageField(
        upload_to='disease_images/', blank=True, null=True)

    def __str__(self):
        return self.name
