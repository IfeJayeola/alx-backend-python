from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def message_saved(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            sender=instance.sender,
            receiver=instance.receiver,
            message=instance)
        print(f"New message created: {instance}")
    else:
        print(f"Message updated: {instance}")


@receiver(post_save, sender=Message)
def message_edited(sender, instance, **kwargs):
    if instance.edited:
        MessageHistory.objects.create(
            message=instance,
            old_content=instance.content)
        print(f"Message edited: {instance}")

@receiver(post_delete, sender=User)
def user_deleted(sender, instance, **kwargs):
    MessageHistory.objects.filter(message=instance).delete()
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    Notification.objects.filter(sender=instance).delete()
    User.objects.filter(user_id=instance).delete()

