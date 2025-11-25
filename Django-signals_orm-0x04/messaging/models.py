from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="notifications")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

Objective: Log when a user edits a message and save the old content before the edit.

Instructions:

Add an edited field to the Message model to track if a message has been edited.

Use the pre_save signal to log the old content of a message into a separate MessageHistory model before it’s updated.

Display the message edit history in the user interface, allowing users to view previous versions of their messages.

Repo:

GitHub repository: alx-backend-python
Directory: Django-signals_orm-0x04
File: messaging/Models
