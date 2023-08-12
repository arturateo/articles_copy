from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from accounts.models import User
from publications.models import Publications


class LikeCreate(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        post = get_object_or_404(Publications, pk=self.kwargs.get("pk"))
        post.like.add(current_user)
        return redirect("publications:home")


class LikeDeleteView(View):

    def post(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, pk=request.user.pk)
        post = get_object_or_404(Publications, pk=self.kwargs.get("pk"))
        post.like.remove(current_user)
        return redirect("publications:home")
