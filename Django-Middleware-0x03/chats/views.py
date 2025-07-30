from rest_framework import viewsets
from chats.models import Conversation as ConversationModel, Message as MessageModel
from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipant
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from .pagination import MessagePagination
# Create your views here


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = ConversationModel.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipant]
    pagination_class = MessagePagination

    @action(detail=True, methods=['post'], url_path='send-message')
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
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipant]
    pagination_class = MessagePagination

    def get_queryset(self):
        conversation_id = self.kwargs.get('conversation_pk')
        return MessageModel.objects.filter(conversation__id=conversation_id)
