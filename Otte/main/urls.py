from django.urls import include, path
from rest_framework import routers
from main.views import CommentViewSet, HomeViewSet,CategoryViewSet

router = routers.DefaultRouter()
router.register(r'comment/<int:pk>/', CommentViewSet)
router.register(r'home', HomeViewSet)
router.register(r'cate', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]