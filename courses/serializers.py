from drf_yasg.utils import swagger_serializer_method
from rest_framework.fields import IntegerField
from rest_framework.serializers import (ModelSerializer, CharField, SerializerMethodField,
                                        BooleanField, ListField)

from courses.models import Course, Lesson, Payment, Subscription
from courses.services import create_payment_data, retrieve_payment_data
from courses.validators import NameAndDescriptionValidator
from django.core.exceptions import ObjectDoesNotExist


class CourseSerializer(ModelSerializer):
    name = CharField(validators=[NameAndDescriptionValidator()])
    description = CharField(validators=[NameAndDescriptionValidator()], required=False)

    subscription_sign = SerializerMethodField()
    lessons_count = IntegerField(source='lesson_set.all.count', read_only=True)

    class Meta:
        model = Course
        fields = ("name", "preview", "description", "lessons_count", 'subscription_sign', )

    @swagger_serializer_method(serializer_or_field=BooleanField)
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

    @swagger_serializer_method(serializer_or_field=ListField)
    def get_lessons(self, instance):
        return [item.name for item in Lesson.objects.filter(course_id=instance.pk)]


class LessonSerializer(ModelSerializer):
    name = CharField(validators=[NameAndDescriptionValidator()])
    description = CharField(validators=[NameAndDescriptionValidator()], required=False)

    class Meta:
        model = Lesson
        fields = "__all__"


class PaymentListSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class PaymentCreateSerializer(ModelSerializer):
    payment_data = SerializerMethodField()
    amount = IntegerField(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"

    def get_payment_data(self, instance):
        if instance.method == "non-cash":
            pay = create_payment_data(instance.amount)
            instance.stripe_id = pay["id"]
            instance.status = pay["status"]
            instance.save()

            return pay
        elif instance.method == "cash":
            return ["Payment by cash"]


class PaymentSerializer(ModelSerializer):
    payment_data = SerializerMethodField()

    class Meta:
        model = Payment
        fields = "__all__"

    def get_payment_data(self, instance):
        if instance.stripe_id is not None:
            return retrieve_payment_data(instance.stripe_id)
        else:
            return ["Payment by cash"]


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"
