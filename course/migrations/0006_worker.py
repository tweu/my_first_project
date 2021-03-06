# Generated by Django 3.2.4 on 2021-06-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_student_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('managers', models.CharField(choices=[('Anas', 'Anas'), ('Kairat', 'Kairat')], max_length=8)),
            ],
            options={
                'verbose_name': 'worker',
                'verbose_name_plural': 'workers',
            },
        ),
    ]
