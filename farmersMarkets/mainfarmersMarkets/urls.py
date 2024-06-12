from django.urls import path
from . import views
from .views import MarketListView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('markets/', MarketListView.as_view(), name='market_list'),
    path('market_detail/<int:id>/', views.market_detail, name='market_detail'),
    path('farmer markets list/', MarketListView.as_view(), name='farmer_markets_list'),
]