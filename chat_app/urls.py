from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MessageViewSet, ChatViewSet, GroupChatViewSet, group_chat

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'groupchats', GroupChatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('group_chat/', group_chat, name='group_chat'),
]
