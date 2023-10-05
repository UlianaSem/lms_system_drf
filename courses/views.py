from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from courses.models import Course, Lesson, Payment
from courses.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, PaymentSerializer


class CourseViewSet(ModelViewSet):
    default_serializer = CourseSerializer
    queryset = Course.objects.all()
    serializers = {
        'retrieve': CourseDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class PaymentListView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('course', 'lesson', 'method', )
    ordering_fields = ('date', )
