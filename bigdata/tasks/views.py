from django.shortcuts import render
from requests import request
from rest_framework import viewsets
from yaml import serialize
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    @action(detail=False, name='my_tasks')
    def my_tasks(self, request):
        qs = Task.objects.filter(assigner=request.user)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
        
    def perform_create(self, serializer):
        serializer.save(assigner=self.request.user)

    