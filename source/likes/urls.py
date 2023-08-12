from django.urls import path

from likes.views import LikeCreate, LikeDeleteView

app_name = 'likes'

urlpatterns = [
    path('like_add/<int:pk>', LikeCreate.as_view(), name='like'),
    path('like_delete/<int:pk>', LikeDeleteView.as_view(), name='unlike'),
]
