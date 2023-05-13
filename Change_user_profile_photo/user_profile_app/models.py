from django.db import models



# Create your models here.
class ImageUploader(models.Model):
    photo = models.ImageField(upload_to="AllImages")