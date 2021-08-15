from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "article_list.html"
    model = Article
    login_url = "login"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = "article_detail.html"
    model = Article
    login_url = "login"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "article_edit.html"
    model = Article
    fields = ("title", "body")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "article_delete.html"
    model = Article
    success_url = reverse_lazy("article_list")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article_new.html"
    model = Article
    fields = ("title", "body")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
