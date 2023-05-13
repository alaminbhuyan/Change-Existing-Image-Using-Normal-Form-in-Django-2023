from django.urls import path
from . import views


urlpatterns = [
    path(route="", view=views.upload_image, name="upload_image_page"),
    path(route="delete/<int:image_id>", view=views.delete_image, name="delete_data"),
    path(route="change/<int:image_id>", view=views.change_image, name="change_data"),
    # image_id coming from the template and we pass it to views.py file and then image_id will pass change_profile_image.html
    # template from views.py file
    path(route="change_profile/<int:image_id>", view=views.change_profile_image, name="change_profile"),
]
