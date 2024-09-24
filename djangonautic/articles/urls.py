from django.urls import path
from . import views

app_name = 'articles'  # This defines the namespace

urlpatterns = [
    path('', views.article_list, name='list'),  # Add the 'name' attribute here
    path('<slug:slug>/', views.article_detail, name='detail'),
]
