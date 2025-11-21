#!/usr/bin/env python3
"""
Custom permissions for conversations and messages
"""

from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allow only participants of a conversation to access its messages
    """

    def has_object_permission(self, request, view, obj):
        # obj can be a Conversation or a Message
        if hasattr(obj, "participants"):
            return request.user in obj.participants.all()
        if hasattr(obj, "conversation"):
            return request.user in obj.conversation.participants.all()
        return False

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
