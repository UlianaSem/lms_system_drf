from datetime import datetime

from django.core.management import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask


class Command(BaseCommand):

    def handle(self, *args, **options):

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS
        )

        PeriodicTask.objects.create(
            interval=schedule,
            name="check_user",
            task="courses.tasks.check_user",
            start_time=datetime.utcnow()
        )
