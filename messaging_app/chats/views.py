from rest_framework import viewsets
from chats.models import Conversation as ConversationModel, Message as MessageModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Conversation

from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.response import Response

# Create your views here

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = ConversationModel.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        user = request.user
        return ConversationModel.objects.filter(participants__in=[user])


    def perform_create(self, serializer):
        serializer.save(participants=[self.request.user])


    def send_message(self,request, PK=None):
        conversation = self.get_object()
        data =  {
            'conversation': conversation.id,
            'sender': request.user.id,
            'content': request.data.get('content')
        }
        serializers = MessageSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        conversation_id = self.kwargs.get('conversation_pk')
        return MessageModel.objects.filter(conversation__id=conversation_id)
