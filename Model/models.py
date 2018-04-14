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
