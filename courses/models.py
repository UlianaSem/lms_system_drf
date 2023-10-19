from django.db import models

from config import settings
from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name="цена", default=10000)

    students = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="студенты", related_name='courses',
                                      **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    video = models.URLField(**NULLABLE)
    price = models.PositiveIntegerField(verbose_name="цена", default=1000)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="студенты", related_name='lessons',
                                      **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Payment(models.Model):
    NON_CASH = "non-cash"
    CASH = "cash"

    METHOD_CHOICES = [
        (NON_CASH, "non-cash"),
        (CASH, "cash"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс", **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="урок", **NULLABLE)

    date = models.DateField(verbose_name="дата оплаты", auto_now_add=True)
    amount = models.PositiveIntegerField(verbose_name="сумма оплаты", **NULLABLE)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES, verbose_name="способ оплаты")

    stripe_id = models.CharField(max_length=100, unique=True, **NULLABLE)
    status = models.CharField(max_length=150, verbose_name="статус", **NULLABLE)

    def __str__(self):
        if self.course:
            return f"Платеж от {self.user} за {self.course} на сумму {self.amount}"

        return f"Платеж от {self.user} за {self.lesson} на сумму {self.amount}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь",
                             **NULLABLE)

    subscription_sign = models.BooleanField(default=True, verbose_name="подписан")

    def __str__(self):
        if self.subscription_sign:
            return f"Пользователь {self.user} подписан на курс {self.course}"

        return f"Пользователь {self.user} не подписан на курс {self.course}"

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
