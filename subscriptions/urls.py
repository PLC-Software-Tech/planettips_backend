from django.urls import path
from .views import *


urlpatterns =[
    path('all',view= AllSubscriptions.as_view()),
    path('create/', view=CreateSubscriptions.as_view()),
]

