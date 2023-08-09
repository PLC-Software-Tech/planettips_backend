from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from social_django.utils import psa
from requests.exceptions import HTTPError
from rest_framework import generics
from rest_framework.response import Response
from .models import Subscription
from .serializers import SubscriptionSerializer

class AllSubscriptions(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class CreateSubscriptions(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer