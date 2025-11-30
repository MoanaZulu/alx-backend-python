from django.shortcuts import render, get_object_or_404
from .models import Message

def conversation_view(request, message_id):
    # Optimize queries with select_related and prefetch_related
    message = (
        Message.objects
        .select_related("sender", "receiver", "parent_message")
        .prefetch_related("replies__sender", "replies__receiver")
        .get(id=message_id)
    )

    # Recursive function using Message.objects.filter
    def get_replies(msg):
        replies = (
            Message.objects
            .filter(parent_message=msg)
            .select_related("sender", "receiver")
        )
        return [
            {
                "message": reply,
                "replies": get_replies(reply)
            }
            for reply in replies
        ]

    context = {
        "message": message,
        "thread": get_replies(message)
    }
    return render(request, "messaging/conversation.html", context)
