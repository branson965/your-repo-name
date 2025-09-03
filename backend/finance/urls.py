from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet,
    TransactionViewSet,
    GoalViewSet,
    SessionLogViewSet
)

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'sessionlogs', SessionLogViewSet)

urlpatterns = router.urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]