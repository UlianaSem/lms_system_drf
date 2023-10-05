from rest_framework.generics import UpdateAPIView, RetrieveAPIView

from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
