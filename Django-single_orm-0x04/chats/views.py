from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
@cache_page(60)  # cache this view for 60 seconds
def conversation_messages(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id).select_related("sender", "receiver")
    return render(request, "chats/conversation.html", {"messages": messages})
