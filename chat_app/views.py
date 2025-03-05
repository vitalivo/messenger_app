from rest_framework import viewsets
from .models import User, Message, Chat, GroupChat
from .serializers import UserSerializer, MessageSerializer, ChatSerializer, GroupChatSerializer
from django.shortcuts import render

def group_chat(request):
    return render(request, 'group_chat.html')  # замените '1' на нужный идентификатор чата


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class GroupChatViewSet(viewsets.ModelViewSet):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer

