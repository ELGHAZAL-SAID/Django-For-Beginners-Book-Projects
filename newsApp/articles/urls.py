from django.urls import path
from .views import (
    ArticleCreateView, 
    ArticleListView,
    ArticleDeleteView, 
    ArticleUpdateView, 
    ArticleDetailView,
    ArticleCreateView,
)


urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('newArticle', ArticleCreateView.as_view(),name = 'new_article'),
    path('', ArticleListView.as_view(), name='article_list'),
]
