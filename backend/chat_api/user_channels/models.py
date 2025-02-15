from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField('auth.User', related_name='user_channels')

class Message(models.Model):
    Channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

