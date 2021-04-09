from rest_framework import mixins, permissions, viewsets

from .permissions import IsAuthorPermission
from .serializers import CustomUserSerializer, TaskSerializer
from tasks.models import Task


class SignUpViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class TaskViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
):
    """Display list of all tasks. Create/update/delete single task."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class OwnTaskViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Display list of tasks of a certain author."""

    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
