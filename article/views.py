from rest_framework import generics

from article.models import Article
from article.serializers import ArticleDetailSerializer
from article.serializers import ArticleListSerializer

from article.permissions import IsAdminUserOrReadOnly


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    # 权限
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
