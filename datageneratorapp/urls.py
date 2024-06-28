from django.urls import path
from . import views
from datageneratorapp.views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('ChannelAPIView', ChannelAPIView.as_view(), name='ChannelAPIView'),
]