from django.urls import path
from .views import EmojiAPIView

urlpatterns = [
    path('emoji/', EmojiAPIView.as_view()),
]