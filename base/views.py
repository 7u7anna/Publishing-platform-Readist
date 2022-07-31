from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Article 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

class ArticleView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'base/homepage.html'
    ordering = ['-date_added']

class ArticleReadView(LoginRequiredMixin, DetailView):
    model = Article
    content_object_name = 'article'
    template_name = 'base/read_article.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    context_object_name = 'article'
    fields = ['title', 'category', 'sub_category', 'content']
    template_name = 'base/create_read.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article 
    context_object_name = 'article'
    fields = ['title', 'content', 'sub_category']
    template_name = 'base/update_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.category = self.request.category
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    context_object_name = 'article'
    template_name = 'base/article_confirm_delete.html'
    success_url = reverse_lazy('account')

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

# function based views

def about(request):
    return render(request, 'base/about.html')

def inspire(request):
    return render(request, 'base/inspire.html')

