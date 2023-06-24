from django.urls import path
from .views import home_page, dashboard

"""
•	http://localhost:8000/ - home page
•	http://localhost:8000/dashboard/ - dashboard page
"""

urlpatterns = [
    path('', home_page, name='home-page'),
    path('dashboard/', dashboard, name='dashboard'),
]