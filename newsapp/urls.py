from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views



app_name = 'newsapp'


urlpatterns = [
    path('', views.news_view, name='news'),
]