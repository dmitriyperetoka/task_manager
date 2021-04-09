from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('signup', views.SignUpViewSet, basename='signup')
router_v1.register('tasks/own', views.OwnTaskViewSet, basename='tasks')
router_v1.register('tasks', views.TaskViewSet, basename='tasks')

urlpatterns = [
    path('v1/token', TokenObtainPairView.as_view(), name='token_obtain'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/', include(router_v1.urls)),
]
