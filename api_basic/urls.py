from django.urls import path
from api_basic.views import ArticleAPIView, ArticleDetailAPIView, GenericArticleAPIView, GenericArticleDetailAPIView

urlpatterns = [
    path('articles/', ArticleAPIView.as_view(), name='article_list'),
    path('articles/generic/', GenericArticleAPIView.as_view(), name='generic_article_list'),
    path('articles/<int:article_id>/', ArticleDetailAPIView.as_view(), name="article_detail"),
    path('articles/generic/<int:pk>/', GenericArticleDetailAPIView.as_view(), name="generic_article_detail")
]
