from django.db import models

from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

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

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

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
    amount = models.PositiveIntegerField(verbose_name="сумма оплаты")
    method = models.CharField(max_length=10, choices=METHOD_CHOICES, verbose_name="способ оплаты")

    def __str__(self):
        if self.course:
            return f"Платеж от {self.user} за {self.course} на сумму {self.amount}"

        return f"Платеж от {self.user} за {self.lesson} на сумму {self.amount}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
