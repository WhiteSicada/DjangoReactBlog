from blog.models import *
from rest_framework import generics
from .serializers import *

class PostList(generics.ListCreateAPIView):
  # going to return all the posts with the status published
  queryset = Post.postobjects.all()
  serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer