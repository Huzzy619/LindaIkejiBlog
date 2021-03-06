from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework.backends import DjangoFilterBackend

from .models import *
from .paginators import PostPaginator
from .serializers import *

# Create your views here.



class PostViewSet (ModelViewSet):

    http_method_names = ['get', 'post', 'patch', 'head', 'options']

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    search_fields = ['author', 'title']
    ordering_fields = ['date_created', 'author']
    pagination_class = PostPaginator
    


    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return AddPostSerializer

        return PostSerializer
        


    def get_serializer_context(self):
        
        return {"user": self.request.user}

    # @action(detail=True, methods=['post', 'get'])
    # def comments(self, request, pk):
    #     serializer = CommentSerializer()
        
    #     return Response(serializer.data)



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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            if self.request.user.is_authenticated:
                return AuthCommentSerializer

            else:
                return AnonCommentSerializer

        else:
            return CommentSerializer

    def get_serializer_context(self):
        return {

            'post_id': self.kwargs['post_pk'], 
            'user': self.request.user
        }


    # def create(self, request):
    #     if self.request.user.is_authenticated:

    #         serializer = AuthCommentSerializer(request.data)
    #     else:
    #         serializer = AnonCommentSerializer(request.data)


    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
        
    #     serializer = CommentSerializer

    #     return Response(serializer.data, status= status.HTTP_100_CONTINUE) 
