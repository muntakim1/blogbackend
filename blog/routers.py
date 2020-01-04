from rest_framework import routers
from blog.ViewSet import UserViewSet
router = routers.DefaultRouter()
router.register(r'blog', UserViewSet)