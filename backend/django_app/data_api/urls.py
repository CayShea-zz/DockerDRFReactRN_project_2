from rest_framework import routers
from .views import ThingarooViewSet, TripViewSet

router = routers.DefaultRouter()
router.trailing_slash = "/?"

router.register(r'thingaroo', ThingarooViewSet)
router.register(r'trip', TripViewSet)

urlpatterns = router.urls