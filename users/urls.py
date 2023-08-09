from django.urls import path
from .views import *


urlpatterns =[
    path('all', view=UsersView.as_view()),
    path('login', view=Login.as_view()),
    path('version', view=AppVersionApi.as_view()),
]