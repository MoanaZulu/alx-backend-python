from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only authenticated users
    and only participants of a conversation to send, view, update, and delete messages.
    """

    def has_permission(self, request, view):
        # User must be authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow safe methods (GET, HEAD, OPTIONS) for participants
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.conversation.participants.all()

        # Explicitly check for PUT, PATCH, DELETE
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return request.user in obj.conversation.participants.all()

        # For POST (sending messages), also require participant
        if request.method == "POST":
            return request.user in obj.conversation.participants.all()

        return False

<<<<<<< HEAD
=======
from rest_framework import permissions
from .models import Conversation

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only authenticated users
    and only participants of a conversation to access it.
    """

    def has_permission(self, request, view):
        # User must be authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # obj here will be a Conversation or Message instance
        if hasattr(obj, "participants"):
            return request.user in obj.participants.all()
        elif hasattr(obj, "conversation"):
            return request.user in obj.conversation.participants.all()
        return False
>>>>>>> 1f54a196b418ddb2ff1d19a3aceceef06924b56e
