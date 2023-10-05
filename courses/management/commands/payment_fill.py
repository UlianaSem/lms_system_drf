import random

from django.core.management import BaseCommand

from courses.models import Course, Lesson, Payment
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        method = [item[1] for item in Payment.METHOD_CHOICES]
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        if users:
            for user in users:
                course = random.choice(courses)

                if course:
                    Payment.objects.create(
                        user=user,
                        course=course,
                        amount=random.randint(7000, 150000),
                        method=random.choice(method)
                    )

                lesson = random.choice(lessons)

                if lesson:
                    Payment.objects.create(
                        user=user,
                        lesson=lesson,
                        amount=random.randint(2000, 10000),
                        method=random.choice(method)
                    )
