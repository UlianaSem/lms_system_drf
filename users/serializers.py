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
        fields = ['email', "password", "first_name", "last_name", 'avatar', 'telephone', 'city', 'payments']

    def get_payments(self, instance):
        return [{"date": item.date, "amount": item.amount, "method": item.method}
                for item in Payment.objects.filter(user_id=instance.pk)]


class OtherUserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['email', "first_name", 'avatar', 'telephone', 'city']


"""При этом при просмотре чужого профиля должна быть доступна только общая информация, 
в которую не входят: пароль, фамилия, история платежей."""