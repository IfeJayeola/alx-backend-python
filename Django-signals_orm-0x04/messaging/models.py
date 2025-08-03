from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=False)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(
        User,
        related_name='sent_messages',
        on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User,
        related_name='received_messages',
        on_delete=models.CASCADE)
    content = models.TextField()
    edited = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class Notification(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='sent_notifications',
        on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User,
        related_name='received_notifications',
        on_delete=models.CASCADE)
    message = models.ForeignKey(
        Message,
        related_name='notifications',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification from {self.sender} for message {self.message} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class MessageHistory(models.Model):
    message = models.ForeignKey(
        Message,
        related_name='history',
        on_delete=models.CASCADE)
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for {self.message} at {self.edited_at.strftime('%Y-%m-%d %H:%M:%S')}"
