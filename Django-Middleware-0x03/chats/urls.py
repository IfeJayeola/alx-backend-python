from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from django.urls import path, include
from .views import MessageViewSet, ConversationViewSet


router = routers.DefaultRouter()
router.register(r'conversation', ConversationViewSet, basename='conversation')
conversation_router = NestedDefaultRouter(router, r'conversation', lookup='conversation')
conversation_router.register(r'message', MessageViewSet, basename='conversation-messages')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversation_router.urls)),
]
