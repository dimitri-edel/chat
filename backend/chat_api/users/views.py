from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserStatus
from .models import Invitation

class UserListView(generics.ListAPIView):
    ''' Get a list of all users including their online status '''

    queryset = User.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        user_statuses = UserStatus.objects.all()
        users_data = []
        for user in queryset:
            user_status = user_statuses.filter(user=user).first()
            users_data.append({
                "user_id": user.id,
                "username": user.username,
                "online": user_status.online if user_status else False
            })
        return Response(users_data)

