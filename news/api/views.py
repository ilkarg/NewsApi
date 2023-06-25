from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def load_all_news_get(request):
	return Response({'response': 'News'})