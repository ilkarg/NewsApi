from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News

@api_view(['GET'])
def load_all_news_get(request):
    # Написать сериализатор для возврата всех новостей
    return Response({'response': 'News'})

@api_view(['POST'])
def add_news_post(request):
    news = News(title=request.data.get('title'), body=request.data.get('body'))
    news.save()
    # Написать сериализатор для возврата объекта модели
    return Response({'response': 'News success created'})