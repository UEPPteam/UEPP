# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Model.models import *
import json


def hello(request):
    context = {}
    context['hello'] = 'hello django!'
    return render(request, 'hello.html', context)


def base(request):
    return render(request, 'base.html')

#课程信息
@csrf_exempt
def course_information(request):
    if request.method == 'GET':
        #username = req.session['username']
        data={}
        course = Course.objects.all()
        courselist = []
        for c in course:
            courseInfo={}
            courseInfo['id']=c.id
            courseInfo['courseId']= c.courseId
            courseInfo['courseName']=c.courseName
            courseInfo['courseAttribute']=c.courseAttribute
            courseInfo['courseModule']=c.courseModule
            courseInfo['courseType']=c.courseType
            courseInfo['credit']=c.credit
            courseInfo['creditHour']=c.creditHour
            courseInfo['introduction']=c.introduction
            courseInfo['pCourseId']=c.pCourseId
            courseInfo['boundCourseId']=c.boundCourseId
            courselist.append(courseInfo)
        data['courselist'] = courselist
        return render(request, 'course.html', data)


# 课程信息-增加课程
@csrf_exempt
def courseAdd(request):
    if request.method == "POST":
        courseName = request.POST.get('courseName')
        courseAttribute = request.POST.get('courseAttribute')
        courseModule = request.POST.get('courseModule')
        courseType = request.POST.get('courseType')
        credit = request.POST.get('credit')
        creditHour = request.POST.get('creditHour')
        introduction = request.POST.get('introduction')
        pCourseId = request.POST.get('pCourseId')
        boundCourseId = request.POST.get('boundCourseId')

        courselist = Course(courseName=courseName, courseAttribute=courseAttribute, courseModule=courseModule, courseType=courseType,
                            credit=credit, creditHour=creditHour, introduction=introduction, pCourseId=pCourseId, boundCourseId=boundCourseId)
        courselist.save();

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


#课程信息-修改
@csrf_exempt
def courseModify(request):
    if request.method == 'POST':
        print("keyixiugai")
        courseName = request.POST.get('courseName')
        courseAttribute = request.POST.get('courseAttribute')
        courseModule = request.POST.get('courseModule')
        courseType = request.POST.get('courseType')
        credit = request.POST.get('credit')
        creditHour = request.POST.get('creditHour')
        introduction = request.POST.get('introduction')
        pCourseId = request.POST.get('pCourseId')
        boundCourseId = request.POST.get('boundCourseId')
        id = request.POST.get('id')
        Course.objects.filter(id=id).update(courseName=courseName, courseAttribute=courseAttribute, courseModule=courseModule, courseType=courseType,
                                            credit=credit,creditHour=creditHour,introduction=introduction,pCourseId=pCourseId,boundCourseId=boundCourseId)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


#课程信息-删除
@csrf_exempt
def courseDelete(req):
    if req.method == 'POST':
        print("keyi shanchu")
        id = req.POST.get('id')
        Course.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')

#专业信息
@csrf_exempt
def major_information(request):
    if request.method == 'GET':
        #username = req.session['username']
        data={}
        major = Major.objects.all()
        majorlist = []
        for m in major:
            majorInfo={}
            majorInfo['id']=m.id
            majorInfo['majorId']=m.majorId
            majorInfo['majorName']=m.majorName
            majorInfo['introduction']=m.introduction
            majorlist.append(majorInfo)
        data['majorlist'] = majorlist
        return render(request, 'major.html', data)


#教师信息
@csrf_exempt
def teacher_information(request):
    if request.method == 'GET':
        #username = req.session['username']
        data={}
        teacher = Teacher.objects.all()
        teacherlist = []
        for t in teacher:
            teacherInfo={}
            teacherInfo['id']=t.id
            teacherInfo['teacherId']=t.teacherId
            teacherInfo['teacherName']=t.teacherName
            teacherInfo['majorId']=t.majorId
            teacherlist.append(teacherInfo)
        data['teacherlist'] = teacherlist
        return render(request, 'teacher.html', data)
