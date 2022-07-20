from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    assigner_username = serializers.ReadOnlyField(source='assigner.username')
    assigner = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), required=True)
    class Meta:
        model = Task
        fields = (
            'id',
            'assigner_username',
            'task_name',
            'task_endtime',
            'assigner',
        )