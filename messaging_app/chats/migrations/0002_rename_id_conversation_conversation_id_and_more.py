# Generated by Django 5.2.4 on 2025-07-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='id',
            new_name='conversation_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='message_body',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='id',
            new_name='message_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='created_at',
            new_name='sent_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
