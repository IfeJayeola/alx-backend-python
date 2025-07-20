from rest_framework import viewsets
from chats.models import Conversation as ConversationModel, Message as MessageModel

from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.response import Response

# Create your views here

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = ConversationModel.objects.all()
    serializer_class = ConversationSerializer

    def send_message(self,request, PK=None):
        conversatiom = self.get_object()
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
