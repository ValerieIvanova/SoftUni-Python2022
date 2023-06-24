from django.urls import path
from .views import create_profile, details_profile, edit_profile, delete_profile
"""
•	http://localhost:8000/profile/create - create profile page
•	http://localhost:8000/profile/details/ - details profile page
•	http://localhost:8000/profile/edit/ - edit profile page
•	http://localhost:8000/profile/delete/ - delete profile page

"""


urlpatterns = [
    path('create/', create_profile, name='create-profile'),
    path('details/', details_profile, name='details-profile'),
    path('edit/', edit_profile, name='edit-profile'),
    path('delete/', delete_profile, name='delete-profile'),
]