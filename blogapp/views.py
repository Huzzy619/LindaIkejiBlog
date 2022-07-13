from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.



class PostViewSet (ModelViewSet):

    http_method_names = ['get', 'post', 'patch', 'head', 'options']

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return AddPostSerializer

        return PostSerializer
        


    def get_serializer_context(self):
        
        return {"user": self.request.user}

    @action(detail=True)
    def comments(self, request, pk):
        return Response("ok")



class PostImageViewSet (ModelViewSet):
    
    serializer_class = PostImageSerializer

    def get_queryset(self):
        return PostImage.objects.filter(post_id = self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}


class CommentViewSet (ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id = self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}