from rest_framework import routers
from .views import TripViewSet

router = routers.DefaultRouter()
router.trailing_slash = "/?"

router.register(r'trips', TripViewSet)

urlpatterns = router.urls