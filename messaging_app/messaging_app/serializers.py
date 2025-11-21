#!/usr/bin/env python3
"""
Serializers for messaging app models
"""

from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "role",
            "created_at",
        ]


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for Message model"""

    sender = serializers.CharField(source="sender.email", read_only=True)

    class Meta:
        model = Message
        fields = [
            "message_id",
            "sender",
            "message_body",
            "sent_at",
        ]


class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for Conversation model with nested messages"""

    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    message_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = [
            "conversation_id",
            "participants",
            "messages",
            "message_count",
            "created_at",
        ]

    def get_message_count(self, obj):
        """Return number of messages in the conversation"""
        return obj.messages.count()

    def validate(self, data):
        """Custom validation example"""
        if not data.get("participants"):
            raise serializers.ValidationError("Conversation must have at least one participant")
        return data
