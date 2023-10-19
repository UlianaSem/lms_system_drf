from django.urls import path
from rest_framework.routers import SimpleRouter

from courses.apps import CoursesConfig
from courses.views import (CourseViewSet, LessonListView, LessonCreateView, LessonDeleteView, LessonDetailView,
                           LessonUpdateView, PaymentListView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView,
                           PaymentCreateView, PaymentDetailView)

app_name = CoursesConfig.name

router = SimpleRouter()
router.register('course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/list/', LessonListView.as_view(), name='lesson-list'),
    path('create_lesson/', LessonCreateView.as_view(), name='lesson-create'),
    path('<int:pk>/delete_lesson/', LessonDeleteView.as_view(), name='lesson-delete'),
    path('<int:pk>/lesson/', LessonDetailView.as_view(), name='lesson-detail'),
    path('<int:pk>/update_lesson/', LessonUpdateView.as_view(), name='lesson-update'),

    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('create_payment/', PaymentCreateView.as_view(), name='payment-create'),
    path('<int:pk>/payment/', PaymentDetailView.as_view(), name='payment-detail'),

    path('subscription/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
    path('subscription/<int:pk>', SubscriptionDestroyAPIView.as_view(), name='subscription-delete'),
] + router.urls
