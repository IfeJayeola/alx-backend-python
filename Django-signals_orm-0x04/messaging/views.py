from django.shortcuts import render
from rest_framework import viewset
from messaging.models import Message, Notification, User, MessageHistory
from .serializers import MessageSerializer, NotificationSerializer, MessageHistorySerializer, UserSerializer


# Create your views here.
class MessageViewset(viewset.ModelViewSet):
    queryset = MessageSerializer.objects.all()

    def 
