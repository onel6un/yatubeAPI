from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('v1/posts', PostAPI)
router.register('v1/group', GroupAPI)
router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentAPI, basename='comment')
router.register('v1/follow', FollowAPI, basename='follow')

urlpatterns = [
    path('', include(router.urls))
]
