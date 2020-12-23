from django.urls import path

from .views import owner, animals, home, cal
urlpatterns = [
    path('', home),
    path('<int:calc><str:string><int:cal>', cal, name='calcu'),
    path('own', owner),
    path('anim', animals),


]