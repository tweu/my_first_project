# Generated by Django 3.2.4 on 2021-06-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_course_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
