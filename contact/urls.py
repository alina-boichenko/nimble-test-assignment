from rest_framework import routers

from contact.views import UserViewSet

router = routers.DefaultRouter()
router.register("", UserViewSet, basename="users")


urlpatterns = router.urls

app_name = "users"
