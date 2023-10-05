from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from courses.models import Payment
from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'avatar', 'telephone', 'city']


class UserDetailSerializer(ModelSerializer):
    payments = SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'avatar', 'telephone', 'city', 'payments']

    def get_payments(self, instance):
        return [{"date": item.date, "amount": item.amount, "method": item.method}
                for item in Payment.objects.filter(user_id=instance.pk)]
