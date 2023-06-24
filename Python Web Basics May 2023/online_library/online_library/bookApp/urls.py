from django.urls import path
from .views import home_page, add_book, edit_book, details_book, delete_book

urlpatterns = [
    path('', home_page, name='home-page'),
    path('add/', add_book, name='add-book'),
    path('edit/<int:pk>', edit_book, name='edit-book'),
    path('details/<int:pk>', details_book, name='details-book'),
    path('delete/<int:pk>', delete_book, name='delete-book'),
]