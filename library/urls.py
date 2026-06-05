from django.urls import path
from library import views

urlpatterns = [
    path('', views.get_all_books, name = 'home'),
    path('create/',views.create_book, name = 'create'),
    path('read/<int:pk>/', views.read_book, name='read'),
    path('update/<int:pk>/', views.update_book, name='update'),
    path('delete/<int:pk>/', views.delete_book, name='delete'),
]