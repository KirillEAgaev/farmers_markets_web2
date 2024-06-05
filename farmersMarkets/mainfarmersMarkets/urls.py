from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('markets/', views.market_list, name='market_list'),
    path('market_detail/', views.market_detail, name='market_detail'),
]