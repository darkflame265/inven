from django.urls import path
from . import views

urlpatterns = [
    path('', views.go_home, name='go_home'),
    path(r'index/', views.index, name='index'),
    path(r'item_menu1/', views.item_menu1, name='item_menu1'),
    path(r'item_menu2/', views.item_menu2, name='item_menu2'),
    path(r'item_menu3/', views.item_menu3, name='item_menu3'),
    path('form/', views.create, name='create'),
]