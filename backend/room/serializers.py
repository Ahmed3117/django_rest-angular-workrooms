from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.serializers import UserSerializer
from todo.serializers import TodoSerializer
from .models import Room

User = get_user_model()

class RoomSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'

