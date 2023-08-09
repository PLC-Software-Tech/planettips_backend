from django.db import models
from users.models import CustomUser
# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser,related_name='user' ,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()

