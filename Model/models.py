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


class Disciplines(models.Model):
    subjectName = models.CharField(max_length=20)
    subjectDes = models.CharField(max_length=512)


class SpecializedSubject(models.Model):
    spec_sub = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    desc = models.CharField(max_length=512)


class CoursesInDisciplines(models.Model):
    subject = models.CharField(max_length=20)
<<<<<<< Updated upstream
    course = models.CharField(max_length=20)


class CourseModule(models.Model):
    courseModule = models.CharField(max_length=45)
    description = models.CharField(max_length=180)


class CourseCategory(models.Model):
    courseCategory = models.CharField(max_length=45)
    description = models.CharField(max_length=180)
||||||| merged common ancestors
    course = models.CharField(max_length=20)
=======
    course = models.CharField(max_length=20)


class CoreCoursesInSpecializedSubject(models.Model):
    spec_sub = models.CharField(max_length=20)
    course = models.CharField(max_length=20)


class ElectiveCoursesInSpecializedSubject(models.Model):
    spec_sub = models.CharField(max_length=20)
    course = models.CharField(max_length=20)


class ElectiveCourses(models.Model):
    course = models.CharField(max_length=20)
>>>>>>> Stashed changes
