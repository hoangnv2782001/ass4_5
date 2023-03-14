from django.db import models
from checkout.models import BaseOrderInfo
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(BaseOrderInfo):
    user = models.ForeignKey(User, unique=True,on_delete=models.CASCADE)

    def __unicode__(self):
        return 'User Profile for: ' + self.user.username
