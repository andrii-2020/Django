from django.urls import path

from .views import owner, animals, home
urlpatterns = [
    path('', home),
    path('own', owner),
    path('anim', animals)
]