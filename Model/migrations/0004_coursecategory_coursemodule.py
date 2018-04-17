# Generated by Django 2.0.4 on 2018-04-17 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0003_corecoursesinspecializedsubject_coursesindisciplines_electivecourses_electivecoursesinspecializedsub'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCategory', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=180)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CourseModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseModule', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=180)),
            ],
        ),
    ]
