from django.urls import reverse_lazy,reverse
from .models import Article
from django.views.generic import ListView, UpdateView, DeleteView,DetailView, CreateView

# Create your views here.

class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body','author')
    template_name = 'mainHtml/article_new.html'
    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})
class ArticleListView(ListView):
    model = Article
    template_name = 'mainHtml/article_list.html'
    context_object_name = 'articles'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title','body')
    template_name = 'mainHtml/article_edit.html'
    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'mainHtml/article_detail.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'mainHtml/article_delete.html'
    success_url = reverse_lazy('article_list')




