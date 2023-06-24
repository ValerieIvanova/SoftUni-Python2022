from django.urls import path
from .views import create_game, details_game, edit_game, delete_game

"""
•	http://localhost:8000/game/create/ - create game page
•	http://localhost:8000/game/details/<id>/ - details game page
•	http://localhost:8000/game/edit/<id>/ - edit game page
•	http://localhost:8000/game/delete/<id>/ - delete game page

"""


urlpatterns = [
    path('create/', create_game, name='create-game'),
    path('details/<int:pk>/', details_game, name='details-game'),
    path('edit/<int:pk>/', edit_game, name='edit-game'),
    path('delete/<int:pk>/', delete_game, name='delete-game'),
]