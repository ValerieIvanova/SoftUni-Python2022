"""
URL configuration for gamesPlay project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
•	http://localhost:8000/ - home page
•	http://localhost:8000/profile/create - create profile page
•	http://localhost:8000/dashboard/ - dashboard page
•	http://localhost:8000/game/create/ - create game page
•	http://localhost:8000/game/details/<id>/ - details game page
•	http://localhost:8000/game/edit/<id>/ - edit game page
•	http://localhost:8000/game/delete/<id>/ - delete game page
•	http://localhost:8000/profile/details/ - details profile page
•	http://localhost:8000/profile/edit/ - edit profile page
•	http://localhost:8000/profile/delete/ - delete profile page

"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gamesPlay.commonApp.urls')),
    path('profile/', include('gamesPlay.profileApp.urls')),
    path('game/', include('gamesPlay.gameApp.urls')),
]
