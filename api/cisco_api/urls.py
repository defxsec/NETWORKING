from django.urls import path, include
from .views import blogApiView, categoryApiView, CategoryPostApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('blogs', blogApiView, basename='blogs')
router.register('category', blogApiView, basename='category')
router.register('categoryBaseBlogs', blogApiView, basename='categoryBaseBlogs')

urlpatterns = [
    path('', include(router.urls))
]
