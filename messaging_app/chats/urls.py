from rest_framework import routers
from .views import MessageViewSet, ConversationViewSet


router = routers.DefaultRouter()
router.register(r'message', MessageViewSet)
router.register(r'conversation', ConversationViewSet, basename='conversations')
urlpatterns = router.urls
