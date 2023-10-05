from rest_framework.fields import IntegerField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from courses.models import Course, Lesson, Payment


class CourseSerializer(ModelSerializer):
    lessons_count = IntegerField(source='lesson_set.all.count')

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons(self, instance):
        return [item.name for item in Lesson.objects.filter(course_id=instance.pk)]


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"
