from blog.models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import PostUserWritePermission
class PostList(generics.ListCreateAPIView):
  # going to return all the posts with the status published
  queryset = Post.postobjects.all()
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]


class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [PostUserWritePermission]