from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid



# Create your models here.
class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'User'
    GUEST = 'guest', 'Guest'

class User(AbstractUser):
    user_id = models.UUIDField(
            primary_key=True, 
            default=uuid.uuid4, 
            editable = False)
    first_name = models.CharField(
            max_length = 30,
            null = False)
    last_name=models.CharField(
            max_length=30,
            null=False)
    password=models.CharField(
            max_length=20,
            null=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
            max_length=20,
            blank=True,
            null=True)
    role = models.CharField(
            max_length=10,
            choices=Role.choices,
            default=Role.USER,)
    created_at = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    conversation_id = models.UUIDField(
            primary_key=True, 
            default=uuid.uuid4, 
            editable=False)
    participants = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    message_id = models.UUIDField(
            primary_key=True, 
            default=uuid.uuid4, 
            editable=False)
    sender_id = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='sent_messages')
    conversation = models.ForeignKey(
            Conversation,
            on_delete=models.CASCADE,
            related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)


