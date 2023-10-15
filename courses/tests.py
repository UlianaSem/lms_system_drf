from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(name="Python")

        self.user = User.objects.create(email='test', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(name="DRF", course=self.course)
        self.lesson.students.add(self.user)

    def test_create(self):
        response = self.client.post(
            reverse("courses:lesson-create"),
            data={"name": "Django", "course": "1"}
        )

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(response.json(), {
            "id": 2,
            "name": "Django",
            "description": None,
            "preview": None,
            "video": None,
            "course": 1,
            "students": []
        })

    def test_update(self):
        response = self.client.patch(
            reverse("courses:lesson-update", args=[self.lesson.pk]),
            data={"name": "Django new"}
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(), {
            "id": self.lesson.pk,
            "name": "Django new",
            "description": self.lesson.description,
            "preview": None,
            "video": self.lesson.video,
            "course": self.lesson.course.pk,
            "students": [student.pk for student in self.lesson.students.all()]
        })

    def test_delete(self):
        response = self.client.delete(
            reverse("courses:lesson-delete", args=[self.lesson.pk])
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_detail(self):
        response = self.client.get(
            reverse("courses:lesson-detail", args=[self.lesson.pk])
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(), {
            "id": self.lesson.pk,
            "name": self.lesson.name,
            "description": self.lesson.description,
            "preview": None,
            "video": self.lesson.video,
            "course": self.lesson.course.pk,
            "students": [student.pk for student in self.lesson.students.all()]
        })

    def test_list(self):
        response = self.client.get(
            reverse("courses:lesson-list")
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "preview": None,
                    "video": self.lesson.video,
                    "course": self.lesson.course.pk,
                    "students": [student.pk for student in self.lesson.students.all()]
                }
            ]
        })


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(name="Python")

        self.user = User.objects.create(email='test', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.course.students.add(self.user)

    def test_create(self):
        response = self.client.post(
            reverse("courses:subscription-create"),
            data={"course": self.course.pk, "subscription_sign": True}
        )

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(response.json(), {
            "id": 1,
            "subscription_sign": True,
            "course": self.course.pk,
            "user": self.user.pk
        })

    def test_delete(self):
        subscription = Subscription.objects.create(course=self.course)

        response = self.client.delete(
            reverse("courses:subscription-delete", args=[subscription.pk])
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
