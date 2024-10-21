from core.apps.users.models import User
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
