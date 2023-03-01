
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Article, Comment
from django.views.generic import ListView, UpdateView, DeleteView,DetailView, CreateView
from .forms import CommentForm
from django.http import JsonResponse
# Create your views here.

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'mainHtml/article_new.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})


class ArticleListView(LoginRequiredMixin , ListView):
    model = Article
    template_name = 'mainHtml/article_list.html'
    context_object_name = 'articles'
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title','body')
    template_name = 'mainHtml/article_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'mainHtml/article_detail.html'
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'mainHtml/article_delete.html'
    success_url = reverse_lazy('article_list')
    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class CommentListView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'mainHtml/comment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(article=context['article'])
        return context

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('comment_list', args=[self.kwargs['pk']])

@login_required
@csrf_exempt
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author or request.user.is_superuser or request.user == comment.article.author:
        comment.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
