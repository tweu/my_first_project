# Generated by Django 3.2.4 on 2021-06-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20210616_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='groups/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='students/'),
        ),
    ]
