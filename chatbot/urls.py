from django.urls import path
from . import views
urlpatterns = [
    path('', views.chatbots , name='chatbots'),
]
