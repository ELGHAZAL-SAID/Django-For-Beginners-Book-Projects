from django.urls import path
from .views import (
    ArticleCreateView, 
    ArticleListView,
    ArticleDeleteView, 
    ArticleUpdateView, 
    ArticleDetailView,
    ArticleCreateView,
    CommentListView,
    delete_comment,
    edit_comment,
)


urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('newArticle', ArticleCreateView.as_view(),name = 'new_article'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/comments/', CommentListView.as_view(), name='comment_list'),
    path('comments/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('edit/<int:comment_id>/', delete_comment, name='edit_comment'),
    
]
