from rest_framework import viewsets, status
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
