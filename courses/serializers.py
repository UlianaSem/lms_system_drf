from rest_framework.fields import IntegerField, SerializerMethodField
from rest_framework.serializers import ModelSerializer, CharField, UniqueTogetherValidator, SerializerMethodField

from courses.models import Course, Lesson, Payment, Subscription
from courses.validators import NameAndDescriptionValidator
from django.core.exceptions import ObjectDoesNotExist


class CourseSerializer(ModelSerializer):
    name = CharField(validators=[NameAndDescriptionValidator()])
    description = CharField(validators=[NameAndDescriptionValidator()], required=False)

    subscription_sign = SerializerMethodField()
    lessons_count = IntegerField(source='lesson_set.all.count')

    class Meta:
        model = Course
        fields = ("name", "preview", "description", "lessons_count", 'subscription_sign', )

    def get_subscription_sign(self, instance):
        try:
            subscription = Subscription.objects.get(
                course_id=instance.pk,
                user_id=self.context['request'].user.pk)

        except ObjectDoesNotExist:
            return False

        else:
            return subscription.subscription_sign


class CourseDetailSerializer(ModelSerializer):
    lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons(self, instance):
        return [item.name for item in Lesson.objects.filter(course_id=instance.pk)]


class LessonSerializer(ModelSerializer):
    name = CharField(validators=[NameAndDescriptionValidator()])
    description = CharField(validators=[NameAndDescriptionValidator()], required=False)

    class Meta:
        model = Lesson
        fields = "__all__"


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"
        validators = [UniqueTogetherValidator(queryset=Subscription.objects.all(), fields=["course"])]
