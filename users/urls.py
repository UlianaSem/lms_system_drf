from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateView, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
