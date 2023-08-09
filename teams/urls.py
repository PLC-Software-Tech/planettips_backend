
from django.urls import path
from .views import *

urlpatterns = [
    path('teams/', view=Teams.as_view()),
]