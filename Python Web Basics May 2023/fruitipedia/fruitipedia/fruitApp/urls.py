from django.urls import path
from .views import create_fruit, details_fruit, edit_fruit, delete_fruit

urlpatterns = [
    path('create/', create_fruit, name='create_fruit'),
    path('<int:pk>/details/', details_fruit, name='details_fruit'),
    path('<int:pk>/edit/', edit_fruit, name='edit_fruit'),
    path('<int:pk>/delete/', delete_fruit, name='delete_fruit'),
]