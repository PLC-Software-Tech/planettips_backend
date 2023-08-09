
from django.urls import path
from .views import *

urlpatterns = [
    path('all/', view=FetchDataAPIView.as_view()),
  
    # path('call/', view=fetch_data_view.as_view()),

]
