from rest_framework.routers import DefaultRouter
from .views import OrderViewSet


router = DefaultRouter()
router.registry('', OrderViewSet)


urlpatterns = []
urlpatterns.extend(router.urls)
