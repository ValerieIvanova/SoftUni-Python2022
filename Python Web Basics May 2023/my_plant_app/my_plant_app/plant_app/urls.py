from django.urls import path
from .views import create_plant, details_plant, edit_plant, delete_plant

urlpatterns = [
    path('create/', create_plant, name='create-plant'),
    path('details/<int:pk>', details_plant, name='details-plant'),
    path('edit/<int:pk>', edit_plant, name='edit-plant'),
    path('delete/<int:pk>', delete_plant, name='delete-plant'),
]