from rest_framework import viewsets
from chats.models import Conversation as ConversationModel, Message as MessageModel
from .serializers import ConversationSerializer, MessageSerializer
#from rest_framework.response import Response

# Create your views here

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = ConversationModel.objects.all()
    serializer_class = ConversationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
