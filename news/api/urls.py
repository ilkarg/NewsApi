from django.urls import path
from . import views

urlpatterns = [
    path('load_all_news/', views.load_all_news_get)
]