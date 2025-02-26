from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 'home' funksiyasını birbaşa views-dən istifadə edin
    path('api/posts/', views.PostListView.as_view(), name='post-list'),  # ListView
    path('api/posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # DetailView
]
