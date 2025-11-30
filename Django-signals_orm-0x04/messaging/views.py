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

    # Recursive function to fetch threaded replies
    def get_replies(msg):
        replies = msg.replies.all().select_related("sender", "receiver")
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


def send_message(request, receiver_id, parent_id=None):
    if request.method == "POST":
        receiver = get_object_or_404(User, id=receiver_id)
        parent_message = None
        if parent_id:
            parent_message = get_object_or_404(Message, id=parent_id)

        Message.objects.create(
            sender=request.user,   # ✅ important fix
            receiver=receiver,
            content=request.POST.get("content"),
            parent_message=parent_message
        )
