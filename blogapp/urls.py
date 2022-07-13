from django.urls import path
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from .views import *

router = DefaultRouter()

router.register('post', PostViewSet)

post_router =  NestedDefaultRouter(router, 'post', lookup = 'post')

post_router.register('image', PostImageViewSet, basename='post-images')
post_router.register('comments', CommentViewSet, basename='post-comments')



urlpatterns = router.urls + post_router.urls
