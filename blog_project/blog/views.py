from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


# API endpoint to get a list of posts
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# API endpoint to get a single post by its ID
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
