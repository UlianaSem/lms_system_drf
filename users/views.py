from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer, UserDetailSerializer, OtherUserDetailSerializer
from drf_yasg import openapi


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


class CustomTokenObtainPairView(TokenObtainPairView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            title="TokenObtainPair",
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, title="email"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, title="password"),
            }
        ),
        responses={200: openapi.Schema(
            title="TokenObtainPair",
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, title="refresh"),
                'access': openapi.Schema(type=openapi.TYPE_STRING, title="access"),
            }
        )
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
