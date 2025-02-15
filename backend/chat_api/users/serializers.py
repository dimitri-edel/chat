# Serializer for User model

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserStatus
from .models import Invitation

class UserSerializer(serializers.ModelSerializer):
    online = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'online')

    def get_online(self, obj):
        user_status = UserStatus.objects.filter(user=obj).first()
        return user_status.online if user_status else False
    
# Serializer for Invitation model

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'
