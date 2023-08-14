from django.urls import path

from likes.views import LikeView, ArticleLikeCreate, ArticleLikeDelete, CommentLikeCreate, CommentLikeDelete

app_name = 'likes'

urlpatterns = [
    path('like_view/', LikeView.as_view(), name='like_view'),
    path('article_like_add/<int:pk>', ArticleLikeCreate.as_view(), name='a_like'),
    path('article_like_delete/<int:pk>', ArticleLikeDelete.as_view(), name='a_unlike'),
    path('comment_like_add/<int:pk>', CommentLikeCreate.as_view(), name='c_like'),
    path('comment_like_delete/<int:pk>', CommentLikeDelete.as_view(), name='c_unlike'),
]
