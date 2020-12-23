from django.urls import path

from .views import owners, animals, home, owner

urlpatterns = [
    path('animals', home),
    path('own', owners),
    path('anim', animals),
    path('<int:id>', owner, name='owner')
]