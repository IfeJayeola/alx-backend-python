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
        fields = ['id', 'participants', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender_id', 'conversation', 'content', 'created_at']

