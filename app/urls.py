from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('skills', views.skills, name='skills'),
    # path('designs', views.designs, name='designs')
]