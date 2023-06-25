from django.urls import path
from . import views

urlpatterns = [
    path('load_all_news/', views.load_all_news_get),
    path('add_news/', views.add_news_post),
    path('load_news/<id>', views.load_news_get)
]