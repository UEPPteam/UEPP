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


# 学科
@csrf_exempt
def subject(request):
    if request.method == 'GET':
        data = {}
        subject = Disciplines.objects.all()
        subjectlist = []
        for c in subject:
            subInfo = {}
            subInfo['id'] = c.id
            subInfo['name'] = c.subjectName
            subInfo['desc'] = c.subjectDes
            subjectlist.append(subInfo)
        data['list'] = subjectlist
        return render(request, 'subject.html', data)


# 学科信息-修改
@csrf_exempt
def subMod(request):
    if request.method == 'POST':
        print("adfa")
        subjectName = request.POST.get('subjectName')
        subjectDesc = request.POST.get('subjectDesc')
        subid = request.POST.get('id')
        Disciplines.objects.filter(id=subid).update(subjectName=subjectName, subjectDes=subjectDesc)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def subAdd(request):
    if request.method == "POST":
        subjectName = request.POST.get('subjectName')
        subjectDesc = request.POST.get('subjectDesc')
        subjectId = request.POST.get('subjectId')

        courselist = Disciplines(id=subjectId, subjectName=subjectName, subjectDes=subjectDesc)
        courselist.save()
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 学科信息-删除
@csrf_exempt
def subDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        Disciplines.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


# 专业
@csrf_exempt
def spe_sub(request):
    if request.method == 'GET':
        data = {}
        spe_sub = SpecializedSubject.objects.all()
        spe_sublist = []
        for c in spe_sub:
            subInfo = {}
            subInfo['id'] = c.id
            subInfo['spec_sub'] = c.spec_sub
            subInfo['subject'] = c.subject
            subInfo['desc'] = c.desc
            spe_sublist.append(subInfo)
        data['list'] = spe_sublist
        return render(request, 'specializedsubject.html', data)


# zhuanye信息-修改
@csrf_exempt
def speMod(request):
    if request.method == 'POST':
        subjectName = request.POST.get('subjectName')
        desc = request.POST.get('desc')
        speId = request.POST.get('id')
        speName = request.POST.get('speName')
        print(desc)
        print(speId)
        SpecializedSubject.objects.filter(id=speId).update(subject=subjectName, desc=desc, spec_sub=speName)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def speAdd(request):
    if request.method == "POST":
        subjectName = request.POST.get('subjectName')
        speDesc = request.POST.get('speDesc')
        speId = request.POST.get('speId')
        speName = request.POST.get('speName')

        spelist = SpecializedSubject(id=speId, subject=subjectName, desc=speDesc, spec_sub=speName)
        spelist.save()
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# zhuanye信息-删除
@csrf_exempt
def spebDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        SpecializedSubject.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')
