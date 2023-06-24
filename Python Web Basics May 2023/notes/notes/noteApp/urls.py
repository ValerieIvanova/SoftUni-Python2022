from django.urls import path
from .views import index, add_note, edit_note, delete_note, details_note, profile, delete_profile

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_note, name='add_note'),
    path('edit/<int:pk>/', edit_note, name='edit_note'),
    path('delete/<int:pk>/', delete_note, name='delete_note'),
    path('details/<int:pk>/', details_note, name='details_note'),
    path('profile/', profile, name='profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]