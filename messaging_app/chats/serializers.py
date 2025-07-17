from rest_framework import serializers
from .models import  Conversation, Message, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email','password', 'phone_number', 'role', 'created_at']
        extra_kwargs = {
    'password': {'write_only': True}
}

class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
            many =True,
            queryset = User.objects.all(),
            allow_empty = False)
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'conversation', 'message_body', 'sent_at']

