from rest_framework import serializers
from . models import *


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id','image']


    def save(self, **kwargs):
        self.instance = PostImage.objects.create(post_id = self.context['post_id'], **self.validated_data)
        return self.instance

class AddPostSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['title']

    
    def save(self, **kwargs):
        self.instance = Post.objects.create(author = self.context["user"], **self.validated_data)

        return self.instance 

class PostSerializer (serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    images = PostImageSerializer(many = True)
    class Meta:
        model = Post
        fields = ['id', 'author','title','images','date_created']

    def get_author(self, post):
        author = post.author.username
        return author



class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields = ['name', 'email', 'text', 'date_created']


    def save(self, **kwargs):
        self.instance = Comment.objects.create(post_id = self.context['post_id'], **self.validated_data)
        return self.instance