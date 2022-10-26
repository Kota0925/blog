from rest_framework import routers
from .views import UserViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
