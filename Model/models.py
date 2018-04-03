from django.db import models

class Course(models.Model):
    courseId = models.CharField(max_length=20)
    courseName = models.CharField(max_length=45)
    courseAttribute = models.CharField(max_length=20)
    courseModule = models.CharField(max_length=45)
    courseType = models.CharField(max_length=45)
    credit = models.FloatField(max_length=12)
    creditHour = models.FloatField(max_length=12)
    introduction = models.CharField(max_length=180)
    pCourseId = models.CharField(max_length=20)
    boundCourseId = models.CharField(max_length=20)


class Major(models.Model):
    majorId = models.CharField(max_length=20)
    majorName = models.CharField(max_length=45)
    introduction = models.CharField(max_length=45)


class Teacher(models.Model):
    teacherId = models.CharField(max_length=20)
    teacherName = models.CharField(max_length=45)
    majorId = models.CharField(max_length=20)


class SyllabusOverview(models.Model):
    syllabusOverviewId = models.CharField(max_length=20)
    majorId = models.CharField(max_length=20)
    grade = models.CharField(max_length=45)
    publishDate = models.DateField(max_length=10)
    eduSystem = models.CharField(max_length=45)
    totalCredit = models.FloatField(max_length=12)
    degree = models.CharField(max_length=45)
    courseModule = models.CharField(max_length=45)
    courseType = models.CharField(max_length=45)
    status = models.CharField(max_length=20)
