from asyncore import read
from attr import field
from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class TaskSerializer(serializers.ModelSerializer):
    assigner_username = serializers.ReadOnlyField(source='assigner.username')
    performers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Task
        fields = (
            'id',
            'assigner_username',
            'task_name',
            'task_endtime',
            'performers',
        )