# Generated by Django 4.2.5 on 2023-10-02 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
