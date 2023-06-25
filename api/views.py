from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer

@api_view(['GET'])
def load_all_news_get(request):
    return Response(News.objects.values())

@api_view(['POST'])
def add_news_post(request):
    news = News(title=request.data.get('title'), body=request.data.get('body'))
    news.save()
    news_serialized = NewsSerializer(news)
    return Response({'title': news_serialized.data['title'], 'body': news_serialized.data['body']})

@api_view(['GET'])
def load_news_get(request, id):
    news = News.objects.get(id=id)
    return Response({'title': news.title, 'body': news.body})