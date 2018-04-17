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


#课程模块信息
@csrf_exempt
def courseModule(request):
    if request.method == 'GET':
        #username = req.session['username']
        data={}
        courseModule = CourseModule.objects.all()
        courseModuleList = []
        for cm in courseModule:
            courseModuleInfo={}
            courseModuleInfo['id']=cm.id
            courseModuleInfo['courseModule']= cm.courseModule
            courseModuleInfo['description'] = cm.description

            courseModuleList.append(courseModuleInfo)
        data['courseModuleList'] = courseModuleList
        return render(request, 'coursemodule.html', data)

# 课程模块-新增
@csrf_exempt
def courseModuleAdd(request):
    if request.method == "POST":
        courseModule = request.POST.get('courseModule')
        description = request.POST.get('description')

        coursemodulelist = CourseModule(courseModule=courseModule, description=description)
        coursemodulelist.save()

        result = 'post_success'

        return HttpResponse(json.dumps(result), content_type='application/json')


#课程模块-编辑
@csrf_exempt
def courseModuleModify(request):
    if request.method == 'POST':
        print("keyixiugai")
        courseModule = request.POST.get('courseModule')
        description = request.POST.get('description')
        id = request.POST.get('id')
        CourseModule.objects.filter(id=id).update(courseModule=courseModule, description=description)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


#课程模块-删除
@csrf_exempt
def courseModuleDelete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        CourseModule.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


# 课程类别
@csrf_exempt
def courseCategory(request):
    if request.method == 'GET':
        #username = req.session['username']
        data={}
        courseCategory = CourseCategory.objects.all()
        courseCategoryList = []
        for c in courseCategory:
            courseInfo={}
            courseInfo['id']=c.id
            courseInfo['courseCategory']= c.courseCategory
            courseInfo['description']=c.description
            courseCategoryList.append(courseInfo)
        data['courseCategoryList'] = courseCategoryList
        return render(request, 'courseCategory.html', data)

# 课程类别-增加
@csrf_exempt
def courseCategoryAdd(request):
    if request.method == "POST":
        courseCategory = request.POST.get('courseCategory')
        description = request.POST.get('description')

        list = CourseCategory(courseCategory=courseCategory, description=description)
        list.save()

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')

#课程类别-编辑
@csrf_exempt
def courseCategoryModify(request):
    if request.method == 'POST':
        courseCategory = request.POST.get('courseCategory')
        description = request.POST.get('description')
        id = request.POST.get('id')
        CourseCategory.objects.filter(id=id).update(courseCategory=courseCategory, description=description)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


#课程类别-删除
@csrf_exempt
def courseCategoryDelete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        CourseCategory.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')

#课程
@csrf_exempt
def courses(request):
    if request.method == 'GET':
        #username = req.session['username']
        data={}
        courses = Courses.objects.all()
        coursesList = []
        for c in courses:
            coursesInfo={}
            coursesInfo['id']=c.id
            coursesInfo['courseId']= c.courseId
            coursesInfo['courseName']=c.courseName
            coursesInfo['courseEngName']=c.courseEngName
            coursesInfo['credit']=c.credit
            coursesInfo['creditHour']=c.creditHour
            coursesInfo['theoryCreditHour']=c.theoryCreditHour
            coursesInfo['practiceCreditHour']=c.practiceCreditHour
            coursesInfo['courseModule']=c.courseModule
            coursesInfo['courseCategory']=c.courseCategory
            coursesInfo['isSchoolCourse']=c.isSchoolCourse
            coursesInfo['isCollegeCourse'] = c.isCollegeCourse
            coursesList.append(coursesInfo)

        courseModuleList = CourseModule.objects.all()
        courseCategoryList = CourseCategory.objects.all()

        data['coursesList'] = coursesList
        data['courseModuleList'] = courseModuleList
        data['courseCategoryList'] = courseCategoryList

        return render(request, 'courses.html', data)


# 增加
@csrf_exempt
def coursesAdd(request):
    if request.method == "POST":
        courseId = request.POST.get('courseId')
        courseName = request.POST.get('courseName')
        courseEngName = request.POST.get('courseEngName')
        credit = request.POST.get('credit')
        creditHour = request.POST.get('creditHour')
        theoryCreditHour = request.POST.get('theoryCreditHour')
        experimentCreditHour = request.POST.get('experimentCreditHour')
        practiceCreditHour = request.POST.get('practiceCreditHour')
        courseModule = request.POST.get('courseModule')
        courseCategory = request.POST.get('courseCategory')
        isSchoolCourse = request.POST.get('isSchoolCourse')
        isCollegeCourse = request.POST.get('isCollegeCourse')

        coursesList = Courses(courseId=courseId, courseName=courseName, courseEngName=courseEngName, credit=credit, creditHour=creditHour,
                            theoryCreditHour=theoryCreditHour, experimentCreditHour=experimentCreditHour, practiceCreditHour=practiceCreditHour, courseModule=courseModule,
                            courseCategory=courseCategory, isSchoolCourse=isSchoolCourse, isCollegeCourse=isCollegeCourse)
        coursesList.save()

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


#修改
@csrf_exempt
def coursesModify(request):
    if request.method == 'POST':
        courseId = request.POST.get('courseId')
        courseName = request.POST.get('courseName')
        courseEngName = request.POST.get('courseEngName')
        credit = request.POST.get('credit')
        creditHour = request.POST.get('creditHour')
        theoryCreditHour  = request.POST.get('theoryCreditHour')
        practiceCreditHour = request.POST.get('practiceCreditHour')
        courseModule = request.POST.get('courseModule')
        courseCategory = request.POST.get('courseCategory')
        isSchoolCourse = request.POST.get('isSchoolCourse')
        isCollegeCourse = request.POST.get('isCollegeCourse')
        id = request.POST.get('id')
        Courses.objects.filter(id=id).update(courseId=courseId, courseName=courseName, courseEngName=courseEngName, credit=credit, creditHour=creditHour,
                            theoryCreditHour=theoryCreditHour, practiceCreditHour=practiceCreditHour, courseModule=courseModule,
                            courseCategory=courseCategory, isSchoolCourse=isSchoolCourse, isCollegeCourse=isCollegeCourse)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


#删除
@csrf_exempt
def coursesDelete(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        Courses.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')

# 先修课
@csrf_exempt
def coursePrevious(request):
    if request.method == 'GET':
        data={}
        coursePrevious = CoursePrevious.objects.all()
        coursePreviousList = []
        for c in coursePrevious:
            coursePreInfo={}
            coursePreInfo['id']=c.id
            coursePreInfo['courseName']= c.courseName
            coursePreInfo['pCourseName']=c.pCourseName
            coursePreviousList.append(coursePreInfo)
        data['coursePreviousList'] = coursePreviousList
        return render(request, 'courseprevious.html', data)

# 先行课-增加
@csrf_exempt
def coursePreviousAdd(request):
    if request.method == "POST":
        courseName = request.POST.get('courseName')
        pCourseName = request.POST.get('pCourseName')

        list = CoursePrevious(courseName=courseName, pCourseName=pCourseName)
        list.save()

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')

# 先行课-编辑
@csrf_exempt
def coursePreviousModify(request):
    if request.method == 'POST':
        courseName = request.POST.get('courseName')
        pCourseName = request.POST.get('pCourseName')
        id = request.POST.get('id')
        CoursePrevious.objects.filter(id=id).update(courseName=courseName, pCourseName=pCourseName)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 先行课-删除
@csrf_exempt
def coursePreviousDelete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        CoursePrevious.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')

# 培养方案版本
@csrf_exempt
def educationOverview(request):
    if request.method == 'GET':
        data={}
        eduOverview = EducationOverview.objects.all()
        eduOverviewList = []
        for eo in eduOverview:
            eduOverviewInfo={}
            eduOverviewInfo['id']=eo.id
            eduOverviewInfo['year']= eo.year
            eduOverviewInfo['desc'] = eo.desc
            eduOverviewInfo['status'] = eo.status

            eduOverviewList.append(eduOverviewInfo)
        data['eduOverviewList'] = eduOverviewList
        return render(request, 'educationoverview.html', data)


@csrf_exempt
def educationOverviewAdd(request):
    if request.method == "POST":
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        #if(status == "None" or status == ""):
        #    status = "未审核"

        list = EducationOverview(year=year, desc=desc, status=status)
        list.save()

        result = 'post_success'

        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def educationOverviewModify(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        id = request.POST.get('id')
        EducationOverview.objects.filter(id=id).update(year=year, desc=desc, status=status)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def educationOverviewDelete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        EducationOverview.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')

# 培养方案->版本->专业
@csrf_exempt
def educationMajor(request):
    if request.method == 'GET':
        data={}
        eduMajor = EducationMajor.objects.all()
        eduMajorList = []
        for em in eduMajor:
            eduMajorInfo={}
            eduMajorInfo['id']=em.id
            eduMajorInfo['year']= em.year
            eduMajorInfo['majorName'] = em.majorName

            eduMajorList.append(eduMajorInfo)
        data['eduMajorList'] = eduMajorList
        return render(request, 'educationmajor.html', data)


@csrf_exempt
def educationMajorAdd(request):
    if request.method == "POST":
        year = request.POST.get('year')
        majorName = request.POST.get('majorName')

        list = EducationMajor(year=year, majorName=majorName)
        list.save()

        result = 'post_success'

        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def educationMajorModify(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        majorName = request.POST.get('majorName')
        id = request.POST.get('id')
        EducationMajor.objects.filter(id=id).update(year=year, majorName=majorName)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def educationMajorDelete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        EducationMajor.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


#
@csrf_exempt
def course_dis(request):
    if request.method == 'GET':
        data = {}
        cd = CoursesInDisciplines.objects.all()
        cdlist = []
        for c in cd:
            subInfo = {}
            subInfo['id'] = c.id
            subInfo['subject'] = c.subject
            subInfo['course'] = c.course
            cdlist.append(subInfo)
        data['list'] = cdlist
        return render(request, 'course_dis.html', data)


# pingtaike信息-修改
@csrf_exempt
def cdMod(request):
    if request.method == 'POST':
        subject = request.POST.get('subName')
        cdId = request.POST.get('id')
        courseName = request.POST.get('courseName')
        CoursesInDisciplines.objects.filter(id=cdId).update(subject=subject, course=courseName)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def cdAdd(request):
    if request.method == "POST":
        subName = request.POST.get('subName')
        cdId = request.POST.get('cdId')
        courseName = request.POST.get('courseName')

        cdlist = CoursesInDisciplines(id=cdId, subject=subName, course=courseName)
        cdlist.save()
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# pingtaike信息-删除
@csrf_exempt
def cdDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        CoursesInDisciplines.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


#
@csrf_exempt
def spec_course(request):
    if request.method == 'GET':
        data = {}
        sc = CoreCoursesInSpecializedSubject.objects.all()
        sclist = []
        for c in sc:
            subInfo = {}
            subInfo['id'] = c.id
            subInfo['spec'] = c.spec_sub
            subInfo['course'] = c.course
            sclist.append(subInfo)
        data['list'] = sclist
        return render(request, 'spec_course.html', data)


# pingtaike信息-修改
@csrf_exempt
def scMod(request):
    if request.method == 'POST':
        spe = request.POST.get('speName')
        scId = request.POST.get('id')
        courseName = request.POST.get('courseName')
        CoreCoursesInSpecializedSubject.objects.filter(id=scId).update(spec_sub=spe, course=courseName)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def scAdd(request):
    if request.method == "POST":
        speName = request.POST.get('speName')
        scId = request.POST.get('scId')
        courseName = request.POST.get('courseName')

        sclist = CoreCoursesInSpecializedSubject(id=scId, spec_sub=speName, course=courseName)
        sclist.save()
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# pingtaike信息-删除
@csrf_exempt
def scDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        CoreCoursesInSpecializedSubject.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


#
@csrf_exempt
def elec_course(request):
    if request.method == 'GET':
        data = {}
        print("saf")
        sc = ElectiveCoursesInSpecializedSubject.objects.all()
        sclist = []
        for c in sc:
            subInfo = {}
            subInfo['id'] = c.id
            subInfo['spec'] = c.spec_sub
            subInfo['course'] = c.course
            sclist.append(subInfo)
        data['list'] = sclist
        return render(request, 'elec_course.html', data)


# 信息-修改
@csrf_exempt
def ecMod(request):
    if request.method == 'POST':
        spe = request.POST.get('subName')
        scId = request.POST.get('id')
        courseName = request.POST.get('courseName')
        ElectiveCoursesInSpecializedSubject.objects.filter(id=scId).update(spec_sub=spe, course=courseName)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def ecAdd(request):
    if request.method == "POST":
        speName = request.POST.get('subName')
        scId = request.POST.get('cdId')
        courseName = request.POST.get('courseName')

        sclist = ElectiveCoursesInSpecializedSubject(id=scId, spec_sub=speName, course=courseName)
        sclist.save()
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# pingtaike信息-删除
@csrf_exempt
def ecDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        ElectiveCoursesInSpecializedSubject.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


#
@csrf_exempt
def e_course(request):
    if request.method == 'GET':
        data = {}
        print("saf")
        sc = ElectiveCourses.objects.all()
        sclist = []
        for c in sc:
            subInfo = {}
            subInfo['id'] = c.id
            subInfo['course'] = c.course
            sclist.append(subInfo)
        data['list'] = sclist
        return render(request, 'e_course.html', data)


# 信息-修改
@csrf_exempt
def eecMod(request):
    if request.method == 'POST':
        scId = request.POST.get('id')
        courseName = request.POST.get('courseName')
        ElectiveCourses.objects.filter(id=scId).update(course=courseName)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def eecAdd(request):
    if request.method == "POST":
        scId = request.POST.get('cdId')
        courseName = request.POST.get('courseName')

        sclist = ElectiveCourses(id=scId, course=courseName)
        sclist.save()
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 信息-删除
@csrf_exempt
def eecDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        ElectiveCourses.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')
