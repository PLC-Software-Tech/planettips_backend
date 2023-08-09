from django.urls import path
from .views import *


urlpatterns = [
    path('tips',view=MatchTipsView.as_view()),
    path('tips/history',view=MatchTipsHistoryView.as_view()),
    path('vip',view=VIPTipsView.as_view()),
    path('vip/history',view=VIPTipsHistoryView.as_view()),
    path('create',view=CreateMatchTipsView.as_view()),
]
