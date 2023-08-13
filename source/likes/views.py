from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from accounts.models import User
from webapp.models import Article


def get_all_likes():
    articles = Article.objects.all()
    json_list = []
    for article in articles:
        json_list.append({article.pk: article.get_total_like() })
    return JsonResponse({"article": json_list})

class LikeView(View):

    def get(self, request, *args, **kwargs):
        return get_all_likes()


class LikeCreate(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
        article.like.add(current_user)
        return get_all_likes()


class LikeDeleteView(View):

    def get(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
        article.like.remove(current_user)
        return get_all_likes()
