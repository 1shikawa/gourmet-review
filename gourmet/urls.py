from django.urls import path, include
from . import views

app_name = 'gourmet'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.Search, name='search'),
    path('shop_info/<str:restid>/', views.ShopInfo, name='shop_info'),
]
