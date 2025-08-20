from django.urls import path
from game import views

urlpatterns = [
    path('', views.game_view, name='game'),
    path('api/play/', views.GameAPIView.as_view(), name='game_api_play'),
]