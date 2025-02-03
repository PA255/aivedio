from django.urls import path
from .views import UserConnectionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'connections', UserConnectionViewSet)

urlpatterns = router.urls