from django.db import models

from users.models import NULLABLE


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
