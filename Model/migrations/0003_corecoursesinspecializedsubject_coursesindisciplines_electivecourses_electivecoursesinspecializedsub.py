# Generated by Django 2.0.4 on 2018-04-16 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0002_specializedsubject'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreCoursesInSpecializedSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_sub', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesInDisciplines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ElectiveCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ElectiveCoursesInSpecializedSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_sub', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]
