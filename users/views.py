from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer, UserDetailSerializer, OtherUserDetailSerializer


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]


class UserDetailView(RetrieveAPIView):
    serializers = {
        "my": UserDetailSerializer,
        "other": OtherUserDetailSerializer
    }
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user == self.get_object():
            return self.serializers.get('my')

        return self.serializers.get('other')
