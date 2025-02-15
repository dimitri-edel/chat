from django.db import models
from django.contrib.auth.models import User
from user_channels.models import Channel

class UserStatus(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    online = models.BooleanField(default=False)
    
# Create your models here.
class Invitation(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    sender = models.ForeignKey('auth.User', related_name='sent_invitations', on_delete=models.CASCADE)
    receiver = models.ForeignKey('auth.User', related_name='received_invitations', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('sender', 'receiver')
