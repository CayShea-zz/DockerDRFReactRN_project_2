from rest_framework import routers
from .views import ThingarooViewSet

router = routers.DefaultRouter()
router.trailing_slash = "/?"

router.register(r'thingaroo', ThingarooViewSet)

urlpatterns = router.urls