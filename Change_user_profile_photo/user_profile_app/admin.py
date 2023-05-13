from django.contrib import admin
from .models import ImageUploader


# Register your models here.
@admin.register(ImageUploader)
class ImageUploaderModelAdmin(admin.ModelAdmin):
    list_display = ['photo']