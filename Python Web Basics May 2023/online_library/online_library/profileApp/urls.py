from django.urls import path
from .views import profile_page, profile_edit, profile_delete

urlpatterns = [
    path('', profile_page, name='profile-page'),
    path('edit/', profile_edit, name='profile-edit'),
    path('delete/', profile_delete, name='profile-delete'),
]