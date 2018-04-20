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
    courseList = models.CharField(max_length=512)


class SpecializedSubject(models.Model):
    specId = models.CharField(max_length=20)
    spec_sub = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    desc = models.CharField(max_length=512)
    courseList = models.CharField(max_length=512)

class CoursesInDisciplines(models.Model):
    subject = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    courseId = models.CharField(max_length=20)


class CourseModule(models.Model):
    courseModule = models.CharField(max_length=45)
    description = models.CharField(max_length=180)


class CourseCategory(models.Model):
    courseCategory = models.CharField(max_length=45)
    description = models.CharField(max_length=180)


class CoreCoursesInSpecializedSubject(models.Model):
    spec_sub = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    courseId = models.CharField(max_length=20)


class ElectiveCoursesInSpecializedSubject(models.Model):
    spec_sub = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    courseId = models.CharField(max_length=20)

class ElectiveCourses(models.Model):
    course = models.CharField(max_length=20)
    courseId = models.CharField(max_length=20)


class Courses(models.Model):
    courseId = models.CharField(max_length=10)
    courseName = models.CharField(max_length=128)
    courseEngName = models.CharField(max_length=128)
    credit = models.FloatField(max_length=12)
    creditHour = models.IntegerField()
    theoryCreditHour = models.IntegerField()
    experimentCreditHour = models.IntegerField()
    practiceCreditHour = models.IntegerField()
    #courseModule = models.ForeignKey('CourseModule', on_delete=models.CASCADE)
    #courseCategory = models.ForeignKey('CourseCategory', on_delete=models.CASCADE)
    courseModule = models.CharField(max_length=45)
    courseCategory = models.CharField(max_length=45)
    courseAttribution = models.CharField(max_length=45)
    isSchoolCourse = models.CharField(max_length=10)
    isCollegeCourse = models.CharField(max_length=10)
    courseType = models.CharField(max_length=512, default="")


class CoursePrevious(models.Model):
    courseName = models.CharField(max_length=128)
    pCourseName = models.CharField(max_length=128)

class EducationOverview(models.Model):
    year = models.IntegerField()
    desc = models.CharField(max_length=180)
    status = models.CharField(max_length=45)

class EducationMajor(models.Model):
    year = models.IntegerField()
    majorName = models.CharField(max_length=128)

class EducationCourses(models.Model):
    year = models.IntegerField()
    majorName = models.CharField(max_length=128)
    courseId = models.CharField(max_length=45)
    courseName = models.CharField(max_length=128)
    credit = models.FloatField(max_length=12)
    creditHour = models.IntegerField()
    semester = models.CharField(max_length=45)
    courseAttribution = models.CharField(max_length=45)

