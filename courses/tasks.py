from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from courses.models import Subscription, Course
from users.models import User


@shared_task
def send_update_notification(course_pk, label):
    required_date = datetime.utcnow() - timedelta(hours=4)
    lessons = Course.objects.get(pk=course_pk).lesson_set.filter(updated_at__gt=required_date).count()

    if (label == "lesson" and lessons <= 1) or (label == "course" and lessons == 0):

        users = Subscription.objects.values("user_id").filter(course_id=course_pk)
        emails = User.objects.values("email").filter(pk__in=users)

        course_name = Course.objects.get(pk=course_pk).name

        send_mail(
            subject=f"Обновлен курс {course_name}",
            message=f"Мы обновили курс {course_name}! Скорее заходи к нам, чтобы посмотреть, что изменилось!",
            recipient_list=[email["email"] for email in emails],
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False
        )


@shared_task
def check_user():
    required_date = datetime.utcnow() - timedelta(days=30.5)
    users = User.objects.filter(last_login__lt=required_date).filter(is_active=True)

    for user in users:
        user.is_active = False
        user.save()
