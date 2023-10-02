from rest_framework.generics import UpdateAPIView

from users.models import User
from users.serializers import UserSerializer


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
