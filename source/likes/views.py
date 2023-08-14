from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from accounts.models import User
from webapp.models import Article

from webapp.models import Comment


def get_all_likes():
    articles = Article.objects.all()
    comments = Comment.objects.all()
    article_list = []
    for article in articles:
        article_list.append({article.pk: article.get_total_like()})
    comment_list = []
    for comment in comments:
        comment_list.append({comment.pk: comment.get_total_like()})

    return JsonResponse({"article": article_list, "comment": comment_list})


class LikeView(View):

    def get(self, request, *args, **kwargs):
        return get_all_likes()


class ArticleLikeCreate(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
        article.like.add(current_user)
        return get_all_likes()


class ArticleLikeDelete(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
        article.like.remove(current_user)
        return get_all_likes()


class CommentLikeCreate(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        article = get_object_or_404(Comment, pk=self.kwargs.get("pk"))
        article.like.add(current_user)
        return get_all_likes()


class CommentLikeDelete(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        article = get_object_or_404(Comment, pk=self.kwargs.get("pk"))
        article.like.remove(current_user)
        return get_all_likes()
