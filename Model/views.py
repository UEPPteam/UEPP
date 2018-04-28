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


# 课程信息
@csrf_exempt
def course_information(request):
    if request.method == 'GET':
        # username = req.session['username']
        data = {}
        course = Course.objects.all()
        courselist = []
        for c in course:
            courseInfo = {}
            courseInfo['id'] = c.id
            courseInfo['courseId'] = c.courseId
            courseInfo['courseName'] = c.courseName
            courseInfo['courseAttribute'] = c.courseAttribute
            courseInfo['courseModule'] = c.courseModule
            courseInfo['courseType'] = c.courseType
            courseInfo['credit'] = c.credit
            courseInfo['creditHour'] = c.creditHour
            courseInfo['introduction'] = c.introduction
            courseInfo['pCourseId'] = c.pCourseId
            courseInfo['boundCourseId'] = c.boundCourseId
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

        courselist = Course(courseName=courseName, courseAttribute=courseAttribute, courseModule=courseModule,
                            courseType=courseType,
                            credit=credit, creditHour=creditHour, introduction=introduction, pCourseId=pCourseId,
                            boundCourseId=boundCourseId)
        courselist.save();

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 课程信息-修改
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
        Course.objects.filter(id=id).update(courseName=courseName, courseAttribute=courseAttribute,
                                            courseModule=courseModule, courseType=courseType,
                                            credit=credit, creditHour=creditHour, introduction=introduction,
                                            pCourseId=pCourseId, boundCourseId=boundCourseId)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 课程信息-删除
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
        i = 1
        for c in subject:
            subInfo = {}
            subInfo['count'] = i
            subInfo['id'] = c.id
            subInfo['subid'] = c.subjectId
            subInfo['name'] = c.subjectName
            subInfo['desc'] = c.subjectDes
            subjectlist.append(subInfo)
            i = i + 1
        data['list'] = subjectlist
        return render(request, 'subject.html', data)


# 学科信息-修改
@csrf_exempt
def subMod(request):
    if request.method == 'POST':
        print("adfa")
        subjectName = request.POST.get('subjectName')
        subjectDesc = request.POST.get('subjectDesc')
        subjectId = request.POST.get('subId')
        id = request.POST.get('id')
        Disciplines.objects.filter(id=id).update(subjectId=subjectId, subjectName=subjectName, subjectDes=subjectDesc)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def subAdd(request):
    if request.method == "POST":
        subjectName = request.POST.get('subjectName')
        subjectDesc = request.POST.get('subjectDesc')
        subjectId = request.POST.get('subjectId')
        cl = []
        courses = Courses.objects.all()
        for c in courses:
            cl.append(c.courseId)
        courselist = Disciplines(subjectId=subjectId, subjectName=subjectName,
                                 subjectDes=subjectDesc, courseList=' '.join(cl))
        courselist.save()
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 学科信息-删除
@csrf_exempt
def subDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        data = {}
        d = Disciplines.objects.filter(id=id)[0].courseList.strip().split(' ')
        courses = Courses.objects.all()
        if len(d) != len(courses):
            data['result'] = 'false'
            return HttpResponse(json.dumps(data), content_type='application/json')
        Disciplines.objects.filter(id=id).delete()
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
        i = 1
        for c in spe_sub:
            subInfo = {}
            subInfo['count'] = i
            subInfo['id'] = c.id
            subInfo['speid'] = c.specId
            subInfo['spec_sub'] = c.spec_sub
            subInfo['subject'] = c.subject
            subInfo['desc'] = c.desc
            spe_sublist.append(subInfo)
            i = i + 1
        data['list'] = spe_sublist
        subjects = Disciplines.objects.all()
        sublist = []
        for s in subjects:
            sublist.append(s.subjectName)
        data['subject'] = sublist
        return render(request, 'specializedsubject.html', data)


# zhuanye信息-修改
@csrf_exempt
def speMod(request):
    if request.method == 'POST':
        subjectName = request.POST.get('subjectName')
        desc = request.POST.get('desc')
        id = request.POST.get('id')
        speid = request.POST.get('speid')
        speName = request.POST.get('speName')
        print(speName)
        SpecializedSubject.objects.filter(id=id).update(specId=speid, subject=subjectName, desc=desc, spec_sub=speName)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def speAdd(request):
    if request.method == "POST":
        subjectName = request.POST.get('subjectName')
        speDesc = request.POST.get('speDesc')
        speId = request.POST.get('speId')
        speName = request.POST.get('speName')

        cl = []
        # courses = Courses.objects.all()
        d = Disciplines.objects.filter(subjectName=subjectName)[0].courseList.strip().split(' ')
        for c in d:
            cl.append(c)

        spelist = SpecializedSubject(specId=speId, subject=subjectName, desc=speDesc,
                                     spec_sub=speName, courseList=' '.join(cl))
        spelist.save()

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# zhuanye信息-删除
@csrf_exempt
def spebDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        spe = SpecializedSubject.objects.filter(id=id)[0].spec_sub
        cs = CoreCoursesInSpecializedSubject.objects.filter(spec_sub=spe)
        data = {}
        data['result'] = 'post_success'
        if len(cs) > 0:
            data['result'] = 'false'
        es = ElectiveCoursesInSpecializedSubject.objects.filter(spec_sub=spe)
        if len(es) > 0:
            data['result'] = 'false'
        if data['result'] == 'false':
            return HttpResponse(json.dumps(data), content_type='application/json')
        SpecializedSubject.objects.filter(id=id).delete()
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


# 课程模块信息
@csrf_exempt
def courseModule(request):
    if request.method == 'GET':
        # username = req.session['username']
        data = {}
        count = 0
        courseModule = CourseModule.objects.all()
        courseModuleList = []
        for cm in courseModule:
            courseModuleInfo = {}
            count += 1
            courseModuleInfo['count'] = count
            courseModuleInfo['id'] = cm.id
            courseModuleInfo['courseModule'] = cm.courseModule
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


# 课程模块-编辑
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


# 课程模块-删除
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
        # username = req.session['username']
        data = {}
        count = 0
        courseCategory = CourseCategory.objects.all()
        courseCategoryList = []
        for c in courseCategory:
            courseInfo = {}
            count += 1
            courseInfo['count'] = count
            courseInfo['id'] = c.id
            courseInfo['courseCategory'] = c.courseCategory
            courseInfo['description'] = c.description
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


# 课程类别-编辑
@csrf_exempt
def courseCategoryModify(request):
    if request.method == 'POST':
        courseCategory = request.POST.get('courseCategory')
        description = request.POST.get('description')
        id = request.POST.get('id')
        CourseCategory.objects.filter(id=id).update(courseCategory=courseCategory, description=description)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 课程类别-删除
@csrf_exempt
def courseCategoryDelete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        CourseCategory.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


# 课程
@csrf_exempt
def courses(request):
    if request.method == 'GET':
        # username = req.session['username']
        data = {}
        count = 0
        courses = Courses.objects.all()
        coursesList = []
        for c in courses:
            coursesInfo = {}
            count += 1
            coursesInfo['count'] = count
            coursesInfo['id']=c.id
            coursesInfo['courseId']= c.courseId
            coursesInfo['courseName']=c.courseName
            coursesInfo['courseEngName']=c.courseEngName
            coursesInfo['credit']=c.credit
            coursesInfo['creditHour']=c.creditHour
            coursesInfo['theoryCreditHour']=c.theoryCreditHour
            coursesInfo['experimentCreditHour']=c.experimentCreditHour
            coursesInfo['practiceCreditHour']=c.practiceCreditHour
            coursesInfo['courseModule']=c.courseModule
            coursesInfo['courseCategory']=c.courseCategory
            coursesInfo['courseAttribution']=c.courseAttribution
            coursesInfo['isSchoolCourse']=c.isSchoolCourse
            coursesInfo['isCollegeCourse'] = c.isCollegeCourse
            coursesInfo['courseType'] = c.courseType
            coursesList.append(coursesInfo)

        courseModuleList = CourseModule.objects.all()
        courseCategoryList = CourseCategory.objects.all()

        data['coursesList'] = coursesList
        data['courseModuleList'] = courseModuleList
        data['courseCategoryList'] = courseCategoryList

        return render(request, 'courses.html', data)
    elif request.method == 'POST':
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 增加
'''
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
        courseAttribution = request.POST.get('courseAttribution')
        isSchoolCourse = request.POST.get('isSchoolCourse')
        isCollegeCourse = request.POST.get('isCollegeCourse')


        coursesList = Courses(courseId=courseId, courseName=courseName, courseEngName=courseEngName, credit=credit,
                              creditHour=creditHour,
                              theoryCreditHour=theoryCreditHour, experimentCreditHour=experimentCreditHour,
                              practiceCreditHour=practiceCreditHour, 
                              courseCategory=courseCategory, courseAttribution=courseAttribution,
                              isSchoolCourse=isSchoolCourse,
                              isCollegeCourse=isCollegeCourse)
        coursesList.save()

        ss = SpecializedSubject.objects.all()
        for s in ss:
            # t = SpecializedSubject.objects.filter(id=s.id)[0]
            ll = s.courseList.split(' ')
            ll.append(courseId)
            SpecializedSubject.objects.filter(id=s.id).update(courseList=' '.join(ll))

        sb = Disciplines.objects.all()
        for ssb in sb:
            lll = ssb.courseList.split(' ')
            lll.append(courseId)
            Disciplines.objects.filter(id=ssb.id).update(courseList=' '.join(lll))
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')
'''


# 修改
@csrf_exempt
def coursesModify(request):
    if request.method == 'POST':
        courseId = request.POST.get('courseId')
        courseName = request.POST.get('courseName')
        courseEngName = request.POST.get('courseEngName')
        credit = request.POST.get('credit')
        creditHour = request.POST.get('creditHour')
        theoryCreditHour = request.POST.get('theoryCreditHour')
        theoryCreditHour  = request.POST.get('theoryCreditHour')
        experimentCreditHour = request.POST.get('experimentCreditHour')
        practiceCreditHour = request.POST.get('practiceCreditHour')
        courseModule = request.POST.get('courseModule')
        courseCategory = request.POST.get('courseCategory')
        isSchoolCourse = request.POST.get('isSchoolCourse')
        isCollegeCourse = request.POST.get('isCollegeCourse')

        id = request.POST.get('id')
        Courses.objects.filter(id=id).update(courseId=courseId, courseName=courseName, courseEngName=courseEngName,
                                             credit=credit, creditHour=creditHour,
                                             theoryCreditHour=theoryCreditHour, practiceCreditHour=practiceCreditHour,
                                             courseModule=courseModule,
                                             courseCategory=courseCategory, isSchoolCourse=isSchoolCourse,
                                             isCollegeCourse=isCollegeCourse)

        Courses.objects.filter(id=id).update(courseId=courseId, courseName=courseName, courseEngName=courseEngName, credit=credit, creditHour=creditHour,
                            theoryCreditHour=theoryCreditHour, experimentCreditHour=experimentCreditHour, practiceCreditHour=practiceCreditHour,
                            courseModule=courseModule, courseCategory=courseCategory, isSchoolCourse=isSchoolCourse, isCollegeCourse=isCollegeCourse)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 删除
@csrf_exempt
def coursesDelete(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        iid = Courses.objects.filter(id=id)[0].courseId
        # leezhen add
        ss = SpecializedSubject.objects.all()
        flag = 1
        for s in ss:
            t = SpecializedSubject.objects.filter(id=s.id)[0]
            ll = t.courseList.split(' ')
            if iid in ll:
                ll.remove(iid)
            else:
                flag = 0
                break
            SpecializedSubject.objects.filter(id=s.id).update(courseList=' '.join(ll))
        d = Disciplines.objects.all()
        f = 1
        for i in d:
            ll = i.courseList.strip().split(' ')
            if iid in ll:
                ll.remove(iid)
            else:
                f = 0
                break
            Disciplines.objects.filter(id=i.id).update(courseList=' '.join(ll))
        # leezhen add
        data = {}
        if flag == 1 and f == 1:
            Courses.objects.filter(id=id).delete()
            data['result'] = 'post_success'
            data['id'] = id
        else:
            data['result'] = 'false'
        # leezhen modified
        return HttpResponse(json.dumps(data), content_type='application/json')


# 先修课
@csrf_exempt
def coursePrevious(request):
    if request.method == 'GET':
        data = {}
        count = 0
        coursePrevious = CoursePrevious.objects.all()
        data={}
        courseName = request.GET.get('courseName')
        coursePrevious = CoursePrevious.objects.filter(courseName=courseName).all()
        #coursePrevious = CoursePrevious.objects.all()
        coursePreviousList = []
        for c in coursePrevious:
            coursePreInfo = {}
            count += 1
            coursePreInfo['count'] = count
            coursePreInfo['id'] = c.id
            coursePreInfo['courseName'] = c.courseName
            coursePreInfo['pCourseName'] = c.pCourseName
            coursePreviousList.append(coursePreInfo)

        courseList = Courses.objects.all()

        data['courseName'] = courseName
        data['coursePreviousList'] = coursePreviousList
        data['courseList'] = courseList
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
        data = {}
        eduOverview = EducationOverview.objects.all()
        eduOverviewList = []
        count = 0
        for eo in eduOverview:
            eduOverviewInfo = {}
            count += 1
            eduOverviewInfo['count'] = count
            eduOverviewInfo['id'] = eo.id
            eduOverviewInfo['year'] = eo.year
            eduOverviewInfo['desc'] = eo.desc
            eduOverviewInfo['status'] = eo.status

            eduOverviewList.append(eduOverviewInfo)
        data['eduOverviewList'] = eduOverviewList
        return render(request, 'educationoverview.html', data)
    elif request.method == 'POST':
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def educationOverviewAdd(request):
    if request.method == "POST":
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        # if(status == "None" or status == ""):
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

@csrf_exempt
def educationOverviewPizhun(request):
    if request.method == 'POST':
        status = "已批准"
        id = request.POST.get('id')
        year = request.POST.get('year')
        eduCoursesList = EducationCourses.objects.filter(year=year).all()
        for ecl in eduCoursesList:
            eduPlanCoursesList = EducationPlanCourses(year=year, majorName=ecl.majorName, courseName=ecl.courseName, semester=ecl.semester)
            eduPlanCoursesList.save()
        EducationOverview.objects.filter(id=id).update(status=status)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def educationOverviewChexiao(request):
    if request.method == 'POST':
        status = "未批准"
        id = request.POST.get('id')
        year = request.POST.get('year')
        eduCoursesList = EducationCourses.objects.filter(year=year).all()
        for ecl in eduCoursesList:
            EducationPlanCourses.objects.filter(year=year, majorName=ecl.majorName, courseName=ecl.courseName,
                                                semester=ecl.semester).all().delete()
        EducationOverview.objects.filter(id=id).update(status=status)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 培养方案->版本->专业
@csrf_exempt
def educationMajor(request):
    if request.method == 'GET':
        data = {}
        eduMajor = EducationMajor.objects.all()
        data={}
        count = 0
        year = request.GET.get('year')
        eduMajor = EducationMajor.objects.filter(year=year).all()
        eduMajorList = []
        for em in eduMajor:
            eduMajorInfo = {}
            count += 1
            eduMajorInfo['count']=count
            eduMajorInfo['id'] = em.id
            eduMajorInfo['year'] = em.year
            eduMajorInfo['majorName'] = em.majorName

            eduMajorList.append(eduMajorInfo)
        specSubList = SpecializedSubject.objects.all()
        spec_subList = []
        for spec in specSubList:
            spec_subList.append(spec.spec_sub)

        data['spec_subList'] = spec_subList
        data['eduMajorList'] = eduMajorList
        data['year'] = year
        return render(request, 'educationmajor.html', data)
    elif request.method == 'POST':
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


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

@csrf_exempt
def educationMajorImportMajors(request):
    if request.method == "POST":
        year = request.POST.get('year')

        spe_sub = SpecializedSubject.objects.all()
        educationMajorList = EducationMajor.objects.filter(year=year).all()
        educationMajorSet = set('')
        for ecl in educationMajorList:
            educationMajorSet.add(ecl.majorName)
        for ss in spe_sub:
            if ss.spec_sub in educationMajorSet:
                continue
            else:
                list = EducationMajor(year=year, majorName=ss.spec_sub)
                list.save()

        result = 'post_success'

        return HttpResponse(json.dumps(result), content_type='application/json')


#
@csrf_exempt
def course_dis(request):
    if request.method == 'GET':
        data = {}
        cd = CoursesInDisciplines.objects.all()
        cdlist = []
        i = 1
        for c in cd:
            subInfo = {}
            subInfo['id'] = i
            subInfo['courseId'] = c.courseId
            subInfo['subject'] = c.subject
            subInfo['course'] = c.course
            cdlist.append(subInfo)
            i = i+1
        data['list'] = cdlist
        subjects = Disciplines.objects.all()
        slist = {}
        sublist = []
        for s in subjects:
            sublist.append(s.subjectName)
            slist[s.subjectName] = s.courseList.strip().split(' ')
        data['subject'] = sublist
        # t = "F"
        courses = Courses.objects.all()
        # clist = []
        cdic = {}
        for c in courses:
            # print(c)
            # clist.append({"name": c.courseName, "id": c.courseId})
            cdic[c.courseName] = c.courseId
            cdic[c.courseId] = c.courseName
        # data['course'] = clist
        data['slist'] = json.dumps(slist)
        data['jcourse'] = json.dumps(cdic)
        return render(request, 'course_dis.html', data)


# pingtaike信息-修改
@csrf_exempt
def cdMod(request):
    if request.method == 'POST':
        subject = request.POST.get('subName')
        cdId = request.POST.get('id')
        courseName = request.POST.get('courseName')
        orisub = request.POST.get('orisub')
        # CoursesInDisciplines.objects.filter(id=cdId).update(subject=subject, course=courseName)
        c = Courses.objects.filter(courseName=courseName)[0]
        sub = Disciplines.objects.filter(subjectName=subject)[0].courseList.strip().split(' ')
        if c.courseId in sub:
            sub.remove(c.courseId)
            Disciplines.objects.filter(subjectName=subject).update(courseList=' '.join(sub))
            ssa = SpecializedSubject.objects.filter(subject=subject)
            for sa in ssa:
                cl = sa.courseList.strip().split(' ')
                cl.remove(c.courseId)
                SpecializedSubject.objects.filter(id=sa.id).update(courseList=' '.join(cl))
        else:
            result = 'false'
            return HttpResponse(json.dumps(result), content_type='application/json')
        sub = Disciplines.objects.all()
        # for ssub in sub:
        #     cl = ssub.courseList.strip().split(' ')
        #     if c.courseId in cl:
        #         cl.remove(c.courseId)
        #     Disciplines.objects.filter(id=ssub.id).update(courseList=' '.join(cl))
        CoursesInDisciplines.objects.filter(courseId=cdId).filter(subject=subject).delete()
        #

        cd = CoursesInDisciplines(courseId=c.courseId, subject=subject, course=courseName)
        cd.save()

        cc = Courses.objects.filter(courseId=cdId)[0].courseType.strip().split(' ')
        cc.remove("ptk")
        Courses.objects.filter(courseId=cdId).update(courseType=' '.join(cc))

        # Courses.objects.filter(courseName=courseName).update(courseType="ptk")

        # sub = Disciplines.objects.filter(subjectName=orisub)[0].courseList.split(' ')
        # sub.append(cdId)
        # Disciplines.objects.filter(subjectName=orisub).update(courseList=' '.join(sub))
        ssa = SpecializedSubject.objects.filter(subject=orisub)
        for sa in ssa:
            cl = sa.courseList.strip().split(' ')
            cl.append(cdId)
            SpecializedSubject.objects.filter(id=sa.id).update(courseList=' '.join(cl))

        subs = Disciplines.objects.all()
        for sub in subs:
            cl = sub.courseList.strip().split(' ')
            cl.append(cdId)
            Disciplines.objects.filter(id=sub.id).update(courseList=' '.join(cl))

        for sub in subs:
            ss = SpecializedSubject.objects.filter(subject=sub.subjectName)
            for s in ss:
                if cdId not in s.courseList.strip().split(' '):
                    cl = Disciplines.objects.filter(id=sub.id)[0].courseList.strip().split(' ')
                    cl.remove(cdId)
                    Disciplines.objects.filter(id=sub.id).update(courseList=' '.join(cl))
                    break

        cc = Courses.objects.filter(courseName=courseName)[0].courseType.strip().split(' ')
        cc.append("ptk")
        Courses.objects.filter(courseName=courseName).update(courseType=' '.join(cc))

        # ss = SpecializedSubject.objects.all()
        # for s in ss:
        #     t = SpecializedSubject.objects.filter(id=s.id)[0]
        #     ll = t.courseList.split(' ')
        #     ll.append(cdId)
        #     ll.remove(c.courseId)
        #     SpecializedSubject.objects.filter(id=s.id).update(courseList=' '.join(ll))

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def cdAdd(request):
    if request.method == "POST":
        subName = request.POST.get('subName')
        cdId = request.POST.get('cdId')
        courseName = request.POST.get('courseName')
        cdlist = CoursesInDisciplines(courseId=cdId, subject=subName, course=courseName)
        # Courses.objects.filter(courseId=cdId).update(courseType="ptk")
        cct = Courses.objects.filter(courseId=cdId)[0].courseType.strip().split(' ')
        cct.append("ptk")
        Courses.objects.filter(courseId=cdId).update(courseType=' '.join(cct))
        # sb = Disciplines.objects.all()
        # for ssb in sb:
        #     cl = ssb.courseList.strip().split(' ')
        #     if cdId in cl:
        #         cl.remove(cdId)
        #     Disciplines.objects.filter(id=ssb.id).update(courseList=' '.join(cl))
        dis = Disciplines.objects.filter(subjectName=subName)[0].courseList.strip().split(' ')
        if cdId in dis:
            dis.remove(cdId)
        Disciplines.objects.filter(subjectName=subName).update(courseList=' '.join(dis))
        ss = SpecializedSubject.objects.filter(subject=subName)
        for s in ss:
            # t = SpecializedSubject.objects.filter(id=s.id)[0]
            ll = s.courseList.strip().split(' ')
            ll.remove(cdId)
            SpecializedSubject.objects.filter(id=s.id).update(courseList=' '.join(ll))
        cdlist.save()
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# pingtaike信息-删除
@csrf_exempt
def cdDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        sub = req.POST.get('sub')
        CoursesInDisciplines.objects.filter(courseId=id).delete()
        # Courses.objects.filter(courseId=id).update(courseType="F")
        ct = Courses.objects.filter(courseId=id)[0].courseType.strip().split(' ')
        print(ct)
        ct.remove("ptk")
        Courses.objects.filter(courseId=id).update(courseType=' '.join(ct))

        # sb = Disciplines.objects.filter(subjectName=sub)[0].courseList.split(' ')
        # sb.append(id)
        # Disciplines.objects.filter(subjectName=sub).update(courseList=' '.join(sb))
        # d = Disciplines.objects.all()
        # for di in d:
        #     cl = di.courseList.strip().split(' ')
        #     cl.append(id)
        #     Disciplines.objects.filter(id=di.id).update(courseList=' '.join(cl))
        d = Disciplines.objects.filter(subjectName=sub)[0].courseList.strip().split(' ')
        d.append(id)
        Disciplines.objects.filter(subjectName=sub).update(courseList=' '.join(d))
        ss = SpecializedSubject.objects.filter(subject=sub)
        for s in ss:
            # t = SpecializedSubject.objects.filter(id=s.id)[0]
            ll = s.courseList.strip().split(' ')
            ll.append(id)
            SpecializedSubject.objects.filter(id=s.id).update(courseList=' '.join(ll))
        d = Disciplines.objects.all()
        for di in d:
            ss = SpecializedSubject.objects.filter(subject=di.subjectName)
            for s in ss:
                if id not in s.courseList.strip().split(' '):
                    cl = Disciplines.objects.filter(id=di.id)[0].courseList.strip().split(' ')
                    cl.remove(id)
                    Disciplines.objects.filter(id=di.id).update(courseList=' '.join(cl))
                    break

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
        i = 1
        for c in sc:
            subInfo = {}
            subInfo['id'] = i
            subInfo['courseId'] = c.courseId
            subInfo['spec'] = c.spec_sub
            subInfo['course'] = c.course
            sclist.append(subInfo)
            i = i+1
        data['list'] = sclist
        spe_subs = SpecializedSubject.objects.all()
        spelist = []
        for s in spe_subs:
            spelist.append(s.spec_sub)
        data['spe'] = spelist
        # t = "F"
        courses = Courses.objects.all()
        # clist = []
        cdic = {}
        for c in courses:
            # print(c)
            # clist.append({"name": c.courseName, "id": c.courseId})
            cdic[c.courseName] = c.courseId
            cdic[c.courseId] = c.courseName
        # data['course'] = clist
        ss = SpecializedSubject.objects.all()
        sslist = {}
        for s in ss:
            l = s.courseList.split(' ')
            sslist[s.spec_sub] = l
        data['sslist'] = json.dumps(sslist)
        data['jcourse'] = json.dumps(cdic)
        return render(request, 'spec_course.html', data)


# hexinke信息-修改
@csrf_exempt
def scMod(request):
    if request.method == 'POST':
        spe = request.POST.get('speName')
        scId = request.POST.get('id')
        courseName = request.POST.get('courseName')
        orispe = request.POST.get('orispe')
        # CoreCoursesInSpecializedSubject.objects.filter(id=scId).update(spec_sub=spe, course=courseName)
        CoreCoursesInSpecializedSubject.objects.filter(courseId=scId).delete()
        c = Courses.objects.filter(courseName=courseName)[0]
        sc = CoreCoursesInSpecializedSubject(courseId=c.courseId, spec_sub=spe, course=courseName)
        sc.save()
        # Courses.objects.filter(courseId=scId).update(courseType="F")
        # Courses.objects.filter(courseName=courseName).update(courseType="hxk")
        ct = Courses.objects.filter(courseId=scId)[0].courseType.split(' ')
        ct.remove("hxk")
        # if len(ct) == 0:
        #     ct.append("F")
        Courses.objects.filter(courseId=scId).update(courseType=' '.join(ct))
        ct = Courses.objects.filter(courseName=courseName)[0].courseType.split(' ')
        # if ct[0] == "F":
        #     ct[0] = "hxk"
        # else:
        #     ct.append("hxk")
        ct.append("hxk")
        Courses.objects.filter(courseId=scId).update(courseType=' '.join(ct))
        # ss = SpecializedSubject.objects.filter(spec_sub=spe)[0]
        # cl = ss.courseList.split(' ')
        # cl.append(scId)
        # cl.remove(c.courseId)
        if spe == orispe:
            print("e")
            ss = SpecializedSubject.objects.filter(spec_sub=spe)[0]
            cl = ss.courseList.split(' ')
            cl.append(scId)
            cl.remove(c.courseId)
            SpecializedSubject.objects.filter(spec_sub=spe).update(courseList=' '.join(cl))

            sab = SpecializedSubject.objects.filter(spec_sub=spe)[0].subject
            subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
            if c.courseId in subcl:
                subcl.remove(c.courseId)
            subcl.append(scId)
            subs = SpecializedSubject.objects.filter(subject=sab)
            for sub in subs:
                if scId not in sub.courseList.split(' '):
                    subcl.remove(scId)
                    # Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))
                    break

            if scId in subcl:
                ct = Courses.objects.filter(courseId=scId)[0].courseType.split(' ')
                if "ptk" in ct:
                    subcl.remove(scId)

            Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))

        else:
            print("!e")
            ss = SpecializedSubject.objects.filter(spec_sub=orispe)[0]
            cl = ss.courseList.split(' ')
            cl.append(scId)
            SpecializedSubject.objects.filter(spec_sub=orispe).update(courseList=' '.join(cl))

            sab = SpecializedSubject.objects.filter(spec_sub=orispe)[0].subject
            subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
            subcl.append(scId)
            subs = SpecializedSubject.objects.filter(subject=sab)
            for sub in subs:
                if scId not in sub.courseList.split(' '):
                    subcl.remove(scId)
                    # Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))
                    break

            if scId in subcl:
                ct = Courses.objects.filter(courseId=scId)[0].courseType.split(' ')
                if "ptk" in ct:
                    subcl.remove(scId)

            Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))

            ss1 = SpecializedSubject.objects.filter(spec_sub=spe)[0]
            cl1 = ss1.courseList.split(' ')
            cl1.remove(c.courseId)
            SpecializedSubject.objects.filter(spec_sub=spe).update(courseList=' '.join(cl1))

            sab = SpecializedSubject.objects.filter(spec_sub=spe)[0].subject
            subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
            if c.courseId in subcl:
                subcl.remove(c.courseId)
            Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def scAdd(request):
    if request.method == "POST":
        speName = request.POST.get('speName')
        scId = request.POST.get('scId')
        courseName = request.POST.get('courseName')
        sclist = CoreCoursesInSpecializedSubject(courseId=scId, spec_sub=speName, course=courseName)
        sclist.save()
        # Courses.objects.filter(courseId=scId).update(courseType="hxk")
        ct = Courses.objects.filter(courseId=scId)[0].courseType.split(' ')
        # if ct[0] == "F":
        #     ct[0] = "hxk"
        # else:
        #     ct.append("hxk")
        ct.append("hxk")
        Courses.objects.filter(courseId=scId).update(courseType=' '.join(ct))
        print(ct)
        ss = SpecializedSubject.objects.filter(spec_sub=speName)[0]
        cl = ss.courseList.split(' ')
        cl.remove(scId)
        SpecializedSubject.objects.filter(spec_sub=speName).update(courseList=' '.join(cl))

        sab = SpecializedSubject.objects.filter(spec_sub=speName)[0].subject
        subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
        if scId in subcl:
            subcl.remove(scId)
        Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 信息-删除
@csrf_exempt
def scDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        CoreCoursesInSpecializedSubject.objects.filter(courseId=id).delete()
        # Courses.objects.filter(courseId=id).update(courseType="F")
        ct = Courses.objects.filter(courseId=id)[0].courseType.split(' ')
        print(ct)
        ct.remove("hxk")
        if len(ct) == 0:
            ct.append("F")
        Courses.objects.filter(courseId=id).update(courseType=' '.join(ct))

        spe = req.POST.get('spe')
        ss = SpecializedSubject.objects.filter(spec_sub=spe)[0]
        cl = ss.courseList.split(' ')
        cl.append(id)
        SpecializedSubject.objects.filter(spec_sub=spe).update(courseList=' '.join(cl))

        sab = SpecializedSubject.objects.filter(spec_sub=spe)[0].subject
        subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
        subcl.append(id)
        subs = SpecializedSubject.objects.filter(subject=sab)
        for sub in subs:
            if id not in sub.courseList.split(' '):
                subcl.remove(id)
                # Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))
                break

        if id in subcl:
            ct = Courses.objects.filter(courseId=id)[0].courseType.split(' ')
            if "ptk" in ct:
                subcl.remove(id)

        Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))

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
        i= 1
        for c in sc:
            subInfo = {}
            subInfo['id'] = i
            subInfo['courseId'] = c.courseId
            subInfo['spec'] = c.spec_sub
            subInfo['course'] = c.course
            sclist.append(subInfo)
            i = i+1
        data['list'] = sclist
        spe_subs = SpecializedSubject.objects.all()
        spelist = []
        for s in spe_subs:
            spelist.append(s.spec_sub)
        data['spe'] = spelist
        # t = "F"
        courses = Courses.objects.all()
        # clist = []
        cdic = {}
        for c in courses:
            # print(c)
            # clist.append({"name": c.courseName, "id": c.courseId})
            cdic[c.courseName] = c.courseId
            cdic[c.courseId] = c.courseName
        # data['course'] = clist
        ss = SpecializedSubject.objects.all()
        sslist = {}
        for s in ss:
            l = s.courseList.split(' ')
            sslist[s.spec_sub] = l
        data['sslist'] = json.dumps(sslist)
        data['jcourse'] = json.dumps(cdic)
        return render(request, 'elec_course.html', data)


# 信息-修改
@csrf_exempt
def ecMod(request):
    if request.method == 'POST':
        spe = request.POST.get('subName')
        scId = request.POST.get('id')
        courseName = request.POST.get('courseName')
        orispe = request.POST.get('orispe')
        # ElectiveCoursesInSpecializedSubject.objects.filter(id=scId).update(spec_sub=spe, course=courseName)
        ElectiveCoursesInSpecializedSubject.objects.filter(courseId=scId).filter(spec_sub=spe).delete()
        c = Courses.objects.filter(courseName=courseName)[0]
        ec = ElectiveCoursesInSpecializedSubject(courseId=c.courseId, spec_sub=spe, course=courseName)
        ec.save()
        # Courses.objects.filter(courseId=scId).update(courseType="F")
        # Courses.objects.filter(courseName=courseName).update(courseType="zxk")
        ct = Courses.objects.filter(courseId=scId)[0].courseType.split(' ')
        ct.remove("zxk")
        # if len(ct) == 0:
        #     ct.append("F")
        Courses.objects.filter(courseId=scId).update(courseType=' '.join(ct))
        ct = Courses.objects.filter(courseName=courseName)[0].courseType.split(' ')
        # if ct[0] == "F":
        #     ct[0] = "zxk"
        # else:
        #     ct.append("zxk")
        ct.append("zxk")
        Courses.objects.filter(courseId=scId).update(courseType=' '.join(ct))
        # ss = SpecializedSubject.objects.filter(spec_sub=spe)[0]
        # cl = ss.courseList.split(' ')
        # cl.append(scId)
        # cl.remove(c.courseId)
        if spe == orispe:
            print("e")
            ss = SpecializedSubject.objects.filter(spec_sub=spe)[0]
            cl = ss.courseList.split(' ')
            cl.append(scId)
            cl.remove(c.courseId)
            print(scId)
            print(c.courseId)
            SpecializedSubject.objects.filter(spec_sub=spe).update(courseList=' '.join(cl))

            sab = SpecializedSubject.objects.filter(spec_sub=spe)[0].subject
            subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
            if c.courseId in subcl:
                subcl.remove(c.courseId)
            subcl.append(scId)
            subs = SpecializedSubject.objects.filter(subject=sab)
            for sub in subs:
                if scId not in sub.courseList.split(' '):
                    subcl.remove(scId)
                    # Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))
                    break

            if scId in subcl:
                ct = Courses.objects.filter(courseId=scId)[0].courseType.split(' ')
                if "ptk" in ct:
                    subcl.remove(scId)

            Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))
        else:
            print("!e")
            ss = SpecializedSubject.objects.filter(spec_sub=spe)[0]
            cl = ss.courseList.split(' ')
            cl.append(scId)
            SpecializedSubject.objects.filter(spec_sub=spe).update(courseList=' '.join(cl))

            sab = SpecializedSubject.objects.filter(spec_sub=orispe)[0].subject
            subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
            subcl.append(scId)
            subs = SpecializedSubject.objects.filter(subject=sab)
            for sub in subs:
                if scId not in sub.courseList.split(' '):
                    subcl.remove(scId)
                    # Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))
                    break

            if scId in subcl:
                ct = Courses.objects.filter(courseId=scId)[0].courseType.split(' ')
                if "ptk" in ct:
                    subcl.remove(scId)

            Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))

            ss1 = SpecializedSubject.objects.filter(spec_sub=orispe)[0]
            cl1 = ss1.courseList.split(' ')
            cl1.remove(c.courseId)
            SpecializedSubject.objects.filter(spec_sub=orispe).update(courseList=' '.join(cl1))

            sab = SpecializedSubject.objects.filter(spec_sub=spe)[0].subject
            subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
            if c.courseId in subcl:
                subcl.remove(c.courseId)
            Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def ecAdd(request):
    if request.method == "POST":
        speName = request.POST.get('subName')
        scId = request.POST.get('cdId')
        courseName = request.POST.get('courseName')

        sclist = ElectiveCoursesInSpecializedSubject(courseId=scId, spec_sub=speName, course=courseName)
        sclist.save()
        # Courses.objects.filter(courseId=scId).update(courseType="zxk")
        ct = Courses.objects.filter(courseId=scId)[0].courseType.split(' ')
        # if ct[0] == "F":
        #     ct[0] = "zxk"
        # else:
        #     ct.append("zxk")
        ct.append("zxk")
        Courses.objects.filter(courseId=scId).update(courseType=' '.join(ct))
        ss = SpecializedSubject.objects.filter(spec_sub=speName)[0]
        cl = ss.courseList.split(' ')
        cl.remove(scId)
        SpecializedSubject.objects.filter(spec_sub=speName).update(courseList=' '.join(cl))

        sab = SpecializedSubject.objects.filter(spec_sub=speName)[0].subject
        subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
        if scId in subcl:
            subcl.remove(scId)
        Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))

        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# pingtaike信息-删除
@csrf_exempt
def ecDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        spe = req.POST.get('spe')
        ElectiveCoursesInSpecializedSubject.objects.filter(courseId=id).filter(spec_sub=spe).delete()
        # Courses.objects.filter(courseId=id).update(courseType="F")
        ct = Courses.objects.filter(courseId=id)[0].courseType.split(' ')
        ct.remove("zxk")
        if len(ct) == 0:
            ct.append("F")
        Courses.objects.filter(courseId=id).update(courseType=' '.join(ct))

        ss = SpecializedSubject.objects.filter(spec_sub=spe)[0]
        cl = ss.courseList.split(' ')
        cl.append(id)
        SpecializedSubject.objects.filter(spec_sub=spe).update(courseList=' '.join(cl))

        sab = SpecializedSubject.objects.filter(spec_sub=spe)[0].subject
        subcl = Disciplines.objects.filter(subjectName=sab)[0].courseList.split(' ')
        subcl.append(id)
        subs = SpecializedSubject.objects.filter(subject=sab)
        for sub in subs:
            if id not in sub.courseList.split(' '):
                subcl.remove(id)
                # Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))
                break

        if id in subcl:
            ct = Courses.objects.filter(courseId=id)[0].courseType.split(' ')
            if "ptk" in ct:
                subcl.remove(id)

        Disciplines.objects.filter(subjectName=sab).update(courseList=' '.join(subcl))

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
        i = 1
        for c in sc:
            subInfo = {}
            subInfo['id'] = i
            subInfo['courseId'] = c.courseId
            subInfo['course'] = c.course
            sclist.append(subInfo)
        data['list'] = sclist

        # t = "F"
        courses = Courses.objects.filter(courseType="")
        clist = []
        cdic = {}
        for c in courses:
            # print(c)
            clist.append({"name": c.courseName, "id": c.courseId})
            cdic[c.courseName] = c.courseId
            cdic[c.courseId] = c.courseName
        data['course'] = clist
        data['jcourse'] = json.dumps(cdic)
        return render(request, 'e_course.html', data)


# 信息-修改
@csrf_exempt
def eecMod(request):
    if request.method == 'POST':
        scId = request.POST.get('id')
        courseName = request.POST.get('courseName')
        ElectiveCourses.objects.filter(courseId=scId).delete()
        c = Courses.objects.filter(courseName=courseName)[0]
        ec = ElectiveCourses(id=c.courseId, course=c.courseName)
        ec.save()
        Courses.objects.filter(courseId=scId).update(courseType="F")
        Courses.objects.filter(courseName=courseName).update(courseType="rxk")
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def eecAdd(request):
    if request.method == "POST":
        scId = request.POST.get('cdId')
        courseName = request.POST.get('courseName')

        sclist = ElectiveCourses(courseId=scId, course=courseName)
        sclist.save()
        Courses.objects.filter(courseId=scId).update(courseType="rxk")
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


# 信息-删除
@csrf_exempt
def eecDel(req):
    if req.method == 'POST':
        id = req.POST.get('id')
        ElectiveCourses.objects.filter(courseId=id).delete()
        Courses.objects.filter(courseId=id).update(courseType="F")
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


# graph
@csrf_exempt
def educationCoursesGraph(request):
    if request.method == 'GET':
        year = request.GET.get('year')
        majorName = request.GET.get('majorName')
        data = {}
        course_p = {}
        course_n = {}
        eduCourses = EducationCourses.objects.filter(year=year, majorName=majorName)
        eduCoursesList = []
        for c in eduCourses:
            eduCoursesInfo = {}
            eduCoursesInfo['courseName'] = c.courseName
            eduCoursesInfo['semester'] = semesterToInt(c.semester)
            course_p[c.courseName] = []
            course_n[c.courseName] = []
            eduCoursesList.append(eduCoursesInfo)

        course_pre = CoursePrevious.objects.all()
        for cp in course_pre:
            if cp.courseName not in course_p.keys():
                course_p[cp.courseName] = []
            course_p[cp.courseName].append(cp.pCourseName)

            if cp.pCourseName not in course_n.keys():
                course_n[cp.pCourseName] = []
            course_n[cp.pCourseName].append(cp.courseName)

        data['ecl'] = eduCoursesList
        data['cp'] = course_p
        data['cn'] = course_n
        data['year'] = year
        data['major'] = majorName
        return render(request, 'visual.html', data)
    if request.method == 'POST':
        cl = request.POST.get("cl")
        cl = json.loads(cl)
        year = request.POST.get("year")
        major = request.POST.get("major")
        for c in cl:
            name = c["courseName"]
            EducationCourses.objects.filter(year=year, majorName=major, courseName=name).update(semester=semesterToStr(str(c["semester"])))
        result = "post_success"
        return HttpResponse(json.dumps(result), content_type='application/json')

#培养方案 -> 版本 -> 专业 -> 培养方案表格
@csrf_exempt
def educationCourses(request):
    if request.method == 'GET':
        #username = req.session['username']
        year = request.GET.get('year')
        majorName = request.GET.get('majorName')
        data={}
        count = 0
        eduCourses = EducationCourses.objects.filter(year=year, majorName=majorName).all()
        #eduCourses = EducationCourses.objects.all()
        eduCoursesList = []
        for c in eduCourses:
            eduCoursesInfo={}
            count += 1
            eduCoursesInfo['id']=c.id
            eduCoursesInfo['count']=count
            eduCoursesInfo['year'] = c.year
            eduCoursesInfo['majorName'] = c.majorName
            eduCoursesInfo['courseId']= c.courseId
            eduCoursesInfo['courseName'] = c.courseName
            eduCoursesInfo['credit'] = c.credit
            eduCoursesInfo['creditHour'] = c.creditHour
            eduCoursesInfo['semester'] = c.semester
            eduCoursesInfo['courseAttribution'] = c.courseAttribution

            eduCoursesList.append(eduCoursesInfo)

        courseList = Courses.objects.all()
        coursesList = []
        for c in courseList:
            coursesInfo = {}
            count += 1
            coursesInfo['count'] = count
            coursesInfo['id'] = c.id
            coursesInfo['courseId'] = c.courseId
            coursesInfo['courseName'] = c.courseName
            coursesInfo['courseEngName'] = c.courseEngName
            coursesInfo['credit'] = c.credit
            coursesInfo['creditHour'] = c.creditHour
            coursesInfo['theoryCreditHour'] = c.theoryCreditHour
            coursesInfo['experimentCreditHour'] = c.experimentCreditHour
            coursesInfo['practiceCreditHour'] = c.practiceCreditHour
            coursesInfo['courseModule'] = c.courseModule
            coursesInfo['courseCategory'] = c.courseCategory
            coursesInfo['courseAttribution'] = c.courseAttribution
            coursesInfo['isSchoolCourse'] = c.isSchoolCourse
            coursesInfo['isCollegeCourse'] = c.isCollegeCourse
            coursesInfo['courseType'] = c.courseType
            coursesList.append(coursesInfo)

        courseModuleList = CourseModule.objects.all()
        courseCategoryList = CourseCategory.objects.all()

        data['eduCoursesList'] = eduCoursesList
        data['year'] = year
        data['majorName'] = majorName
        data['courseList'] = courseList
        data['courseModuleList'] = courseModuleList
        data['courseCategoryList'] = courseCategoryList
        data['list'] = json.dumps(coursesList)

        return render(request, 'educationcourses.html', data)




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
        courseAttribution = request.POST.get('courseAttribution')
        isSchoolCourse = request.POST.get('isSchoolCourse')
        isCollegeCourse = request.POST.get('isCollegeCourse')

        coursesList = Courses(courseId=courseId, courseName=courseName, courseEngName=courseEngName, credit=credit, creditHour=creditHour,
                            theoryCreditHour=theoryCreditHour, experimentCreditHour=experimentCreditHour, practiceCreditHour=practiceCreditHour, courseModule=courseModule,
                            courseCategory=courseCategory, courseAttribution=courseAttribution, isSchoolCourse=isSchoolCourse, isCollegeCourse=isCollegeCourse)
        coursesList.save()
        ss = SpecializedSubject.objects.all()
        for s in ss:
            t = SpecializedSubject.objects.filter(id=s.id)[0]
            ll = t.courseList.split(' ')
            ll.append(courseId)
            SpecializedSubject.objects.filter(id=s.id).update(courseList=' '.join(ll))

        sb = Disciplines.objects.all()
        for ssb in sb:
            lll = ssb.courseList.split(' ')
            lll.append(courseId)
            Disciplines.objects.filter(id=ssb.id).update(courseList=' '.join(lll))
            
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
        experimentCreditHour = request.POST.get('experimentCreditHour')
        practiceCreditHour = request.POST.get('practiceCreditHour')
        courseModule = request.POST.get('courseModule')
        courseCategory = request.POST.get('courseCategory')
        isSchoolCourse = request.POST.get('isSchoolCourse')
        isCollegeCourse = request.POST.get('isCollegeCourse')

        id = request.POST.get('id')
        Courses.objects.filter(id=id).update(courseId=courseId, courseName=courseName, courseEngName=courseEngName, credit=credit, creditHour=creditHour,
                            theoryCreditHour=theoryCreditHour, experimentCreditHour=experimentCreditHour, practiceCreditHour=practiceCreditHour,
                            courseModule=courseModule, courseCategory=courseCategory, isSchoolCourse=isSchoolCourse, isCollegeCourse=isCollegeCourse)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


#删除
@csrf_exempt
def educationCoursesDelete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        EducationCourses.objects.filter(id=id).delete()
        data = {}
        data['result'] = 'post_success'
        data['id'] = id
        return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def educationCoursesAdd(request):
    if request.method == "POST":
        year = request.POST.get('year')
        majorName = request.POST.get('majorName')
        courseName = request.POST.get('courseName')
        semester = request.POST.get('semester')

        courseList = Courses.objects.filter(courseName=courseName).all()
        for c in courseList:
            courseId = c.courseId
            credit = c.credit
            creditHour = c.creditHour
            courseAttribution = c.courseAttribution


        '''
        # 检查该年度该专业该学期是否有这门课，查重
        educList = EducationCourses.objects.filter(year=year, majorName=majorName).all()
        for e in educList:
            if e.courseName==courseName:
                result = "sorry,不能添加该课程。\n该课程已存在于该年度该专业中！"
                return HttpResponse(json.dumps(result), content_type='application/json')

        # 检查该课程是否学科平台课，若是，检查该专业是否在该学科下
        courseSubjectList = CoursesInDisciplines.objects.filter(course=courseName).all()
        courseSpecialSubjectList = CoreCoursesInSpecializedSubject.objects.filter(course=courseName).all()


        for cs in courseSubjectList:
            if cs.course==courseName:
                subject = cs.subject
                subjectSpecialList = SpecializedSubject.objects.filter(subject=subject).all()
                for ssl in subjectSpecialList:
                    if ssl.spec_sub==majorName:
                        break
                    else:
                        result = "SORRY，不能添加该课。\n该课程为其他学科学科平台课，本专业不具有修改该课程的权限。"
                        return HttpResponse(json.dumps(result), content_type='application/json')
            else: #  检查是否为专业核心课
                for css in courseSpecialSubjectList:
                    if css.course==courseName:
                        specSub = css.spec_sub
                        if majorName==specSub:
                            break
                        else:
                            result = "SORRY，不能添加该课。\n该课程为其他专业专业核心课，本专业不具有修改该课程的权限。"
                            return HttpResponse(json.dumps(result), content_type='application/json')

        for css in courseSpecialSubjectList:
            if css.course == courseName:
                specSub = css.spec_sub
                if majorName == specSub:
                    break
                else:
                    result = "SORRY，不能添加该课。\n该课程为其他专业专业核心课，本专业不具有修改该课程的权限。"
                    return HttpResponse(json.dumps(result), content_type='application/json')

        # 剩下检查是否为该专业课程
        elecoursList = ElectiveCoursesInSpecializedSubject.objects.filter(course=courseName).all()
        for ec in elecoursList:
            if ec.spec_sub==majorName:
                break
            else:
                result = "SORRY，不能添加该课。\n该课程不是本专业专业选修课，本专业不具有修改该课程的权限。"
                return HttpResponse(json.dumps(result), content_type='application/json')

        # 检查是否为任意选修课,好像没啥用这个判断
        eleList = ElectiveCourses.objects.filter(course=courseName).all()
        for el in eleList:
            if courseName==el.course:
                break
            else:
                result = "SORRY，不能添加该课。\n该课程既不是本专业专业核心课和专业选修课，也不是该专业学科的学科平台课，也不是任意选修课，本专业不具有修改该课程的权限。"
                return HttpResponse(json.dumps(result), content_type='application/json')
        '''

        result = checkAddAuthority(year, courseName, majorName)
        if result == 'post_success':
            result = checkAddPrevious(year, courseName, semester)
            if result == 'post_success':
                eduCourseList = EducationCourses(year=year, majorName=majorName, courseId=courseId, courseName=courseName, semester=semester,
                                         credit=credit, creditHour=creditHour, courseAttribution=courseAttribution)
                eduCourseList.save()

        # result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')

# 约束检查函数:检查是否有权限添加该课
@csrf_exempt
def checkAddAuthority(year, courseName, majorName):
    # 检查该年度该专业该学期是否有这门课，查重
    educList = EducationCourses.objects.filter(year=year, majorName=majorName).all()
    for e in educList:
        if e.courseName == courseName:
            result = "sorry,不能添加该课程。\n该课程已存在于该年度该专业中！"
            return result

    # 检查该课程是否学科平台课，若是，检查该专业是否在该学科下
    courseSubjectList = CoursesInDisciplines.objects.filter(course=courseName).all()
    courseSpecialSubjectList = CoreCoursesInSpecializedSubject.objects.filter(course=courseName).all()

    for cs in courseSubjectList:
        if cs.course == courseName:
            subject = cs.subject
            subjectSpecialList = SpecializedSubject.objects.filter(subject=subject).all()
            for ssl in subjectSpecialList:
                if ssl.spec_sub == majorName:
                    break
                else:
                    result = "SORRY，不能添加该课。\n该课程为其他学科学科平台课，本专业不具有修改该课程的权限。"
                    return result
        else:  # 检查是否为专业核心课
            for css in courseSpecialSubjectList:
                if css.course == courseName:
                    specSub = css.spec_sub
                    if majorName == specSub:
                        break
                    else:
                        result = "SORRY，不能添加该课。\n该课程为其他专业专业核心课，本专业不具有修改该课程的权限。"
                        return result

    for css in courseSpecialSubjectList:
        if css.course == courseName:
            specSub = css.spec_sub
            if majorName == specSub:
                break
            else:
                result = "SORRY，不能添加该课。\n该课程为其他专业专业核心课，本专业不具有修改该课程的权限。"
                return result

    # 剩下检查是否为该专业课程
    elecoursList = ElectiveCoursesInSpecializedSubject.objects.filter(course=courseName).all()
    for ec in elecoursList:
        if ec.spec_sub == majorName:
            break
        else:
            result = "SORRY，不能添加该课。\n该课程不是本专业专业选修课，本专业不具有修改该课程的权限。"
            return result

    return 'post_success'

# 约束检查函数:检查先修课约束
@csrf_exempt
def checkAddPrevious(year, courseName, semester):
    coursePreviousList = CoursePrevious.objects.filter(courseName=courseName).all()
    for cpl in coursePreviousList:
        pCoursesList = EducationCourses.objects.filter(year=year, courseName=cpl.pCourseName).all()
        for pcl in pCoursesList:
            pclSemester = semesterToInt(pcl.semester)
            if pclSemester > semesterToInt(semester):
                result = "sorry，不能添加该课。\n该课程有先修课在此课添加学期前，请先修改先修课：" + cpl.courseName + " 上课学期再添加该课。"
                return result

    return 'post_success'


@csrf_exempt
def semesterToInt(str):
    if str == "一":
        return 1
    elif str == "二":
        return 2
    elif str == "三":
        return 3
    elif str == "四":
        return 4
    elif str == "五":
        return 5
    elif str == "六":
        return 6
    elif str == "七":
        return 7
    elif str == "八":
        return 8


def semesterToStr(str):
    if str == "1":
        return "一"
    elif str == "2":
        return "二"
    elif str == "3":
        return "三"
    elif str == "4":
        return "四"
    elif str == "5":
        return "五"
    elif str == "6":
        return "六"
    elif str == "7":
        return "七"
    elif str == "8":
        return "八"


# 教学计划
@csrf_exempt
def educationPlan(request):
    if request.method == 'GET':
        data = {}
        status = "已批准"
        eduOverview = EducationOverview.objects.filter(status = status).all()
        eduOverviewList = []
        count = 0
        for eo in eduOverview:
            eduOverviewInfo = {}
            count += 1
            eduOverviewInfo['id'] = eo.id
            eduOverviewInfo['count'] = count
            eduOverviewInfo['year'] = eo.year
            eduOverviewInfo['desc'] = eo.desc
            eduOverviewInfo['status'] = eo.status

            eduOverviewList.append(eduOverviewInfo)
        data['eduOverviewList'] = eduOverviewList
        return render(request, 'educationplan.html', data)
    elif request.method == 'POST':
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def educationPlanDetail(request):
    if request.method == 'GET':
        data = {}
        data={}
        count = 0
        year = request.GET.get('year')
        eduPlanCourses = EducationPlanCourses.objects.filter(year=year).all()
        eduPlanDetailList = []
        flagSet = set('')
        for epc in eduPlanCourses:
            eduPlanCoursesInfo = {}
            count += 1
            if epc.majorName in flagSet:
                continue
            else:
                eduPlanCourses = EducationPlanCourses.objects.filter(year=year, majorName=epc.majorName)
                eduPlanCoursesDict = {}
                eduPlanCoursesDict['finished'] = 0
                eduPlanCoursesDict['started'] = 0
                eduPlanCoursesDict['unstarted'] = 0
                for e in eduPlanCourses:
                    if e.status == "已结束":
                        eduPlanCoursesDict['finished'] += 1
                    elif e.status == "正进行":
                        eduPlanCoursesDict['started'] += 1
                    elif e.status == "未开始":
                        eduPlanCoursesDict['unstarted'] += 1

                flagSet.add(epc.majorName)
                eduPlanCoursesInfo['count'] = count
                eduPlanCoursesInfo['id'] = epc.id
                eduPlanCoursesInfo['year'] = epc.year
                eduPlanCoursesInfo['educationPlanId'] = epc.educationPlanId
                eduPlanCoursesInfo['majorName'] = epc.majorName
                eduPlanCoursesInfo['finished'] = eduPlanCoursesDict['finished']
                eduPlanCoursesInfo['started'] = eduPlanCoursesDict['started']
                eduPlanCoursesInfo['unstarted'] = eduPlanCoursesDict['unstarted']

            eduPlanDetailList.append(eduPlanCoursesInfo)
        specSubList = SpecializedSubject.objects.all()
        spec_subList = []
        for spec in specSubList:
            spec_subList.append(spec.spec_sub)

        data['spec_subList'] = spec_subList
        data['eduPlanDetailList'] = eduPlanDetailList
        data['year'] = year
        return render(request, 'educationplandetail.html', data)
    elif request.method == 'POST':
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def educationPlanDetailAdd(request):
    if request.method == "POST":
        year = request.POST.get('year')
        majorName = request.POST.get('majorName')
        educationPlanId = request.POST.get('educationPlanId')
        print(educationPlanId)

        list = EducationPlanCourses(year=year, majorName=majorName, educationPlanId=educationPlanId)
        list.save()

        result = 'post_success'

        return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def educationPlanDetailModify(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        majorName = request.POST.get('majorName')
        educationPlanId = request.POST.get('educationPlanId')
        id = request.POST.get('id')
        EducationPlanCourses.objects.filter(id=id).update(year=year, majorName=majorName, educationPlanId=educationPlanId)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def educationPlanGraph(request):
    if request.method == 'GET':
        year = request.GET.get('year')
        majorName = request.GET.get('majorName')
        educationPlanId = request.GET.get('educationPlanId')
        data = {}
        eduPlanCourses = EducationPlanCourses.objects.filter(year=year, majorName=majorName,
                                                             educationPlanId=educationPlanId).all()
        eduPlanCoursesList = []
        for epc in eduPlanCourses:
            c = {}
            c['courseName'] = epc.courseName
            c['semester'] = semesterToInt(epc.semester)
            c['status'] = status2int(epc.status.strip())
            eduPlanCoursesList.append(c)
        data['cl'] = eduPlanCoursesList

        return render(request, 'visual_plan.html', data)


def status2int(status):
    if status == '未开始':
        return 0;
    elif status == '正进行':
        return 1;
    elif status == '已结束':
        return 2;
    else:
        return 3;


@csrf_exempt
def educationPlanCourses(request):
    if request.method == 'GET':
        data = {}
        eduMajor = EducationMajor.objects.all()
        data={}
        count = 0
        year = request.GET.get('year')
        majorName = request.GET.get('majorName')
        educationPlanId = request.GET.get('educationPlanId')
        eduPlanCourses = EducationPlanCourses.objects.filter(year=year, majorName=majorName, educationPlanId=educationPlanId).all()
        eduPlanCoursesList = []

        for epc in eduPlanCourses:
            eduPlanCoursesInfo = {}
            count += 1
            eduPlanCoursesInfo['count']=count
            eduPlanCoursesInfo['id'] = epc.id
            eduPlanCoursesInfo['year'] = epc.year
            eduPlanCoursesInfo['educationPlanId'] = epc.educationPlanId
            eduPlanCoursesInfo['majorName'] = epc.majorName
            eduPlanCoursesInfo['courseName'] = epc.courseName
            eduPlanCoursesInfo['semester'] = epc.semester
            eduPlanCoursesInfo['status'] = epc.status
            courses = Courses.objects.filter(courseName=epc.courseName).all()
            for c in courses:
                eduPlanCoursesInfo['courseId'] = c.courseId
                eduPlanCoursesInfo['courseName'] = c.courseName
                eduPlanCoursesInfo['courseEngName'] = c.courseEngName
                eduPlanCoursesInfo['credit'] = c.credit
                eduPlanCoursesInfo['creditHour'] = c.creditHour
                eduPlanCoursesInfo['theoryCreditHour'] = c.theoryCreditHour
                eduPlanCoursesInfo['experimentCreditHour'] = c.experimentCreditHour
                eduPlanCoursesInfo['practiceCreditHour'] = c.practiceCreditHour
                eduPlanCoursesInfo['courseModule'] = c.courseModule
                eduPlanCoursesInfo['courseCategory'] = c.courseCategory
                eduPlanCoursesInfo['courseAttribution'] = c.courseAttribution

            eduPlanCoursesList.append(eduPlanCoursesInfo)

        data['eduPlanCoursesList'] = eduPlanCoursesList
        return render(request, 'educationplancourses.html', data)
    elif request.method == 'POST':
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def educationPlanCoursesModify(request):
    if request.method == 'POST':
        courseName = request.POST.get('courseName')
        status = request.POST.get('status')
        id = request.POST.get('id')
        EducationPlanCourses.objects.filter(id=id).update(courseName=courseName, status=status)
        result = 'post_success'
        return HttpResponse(json.dumps(result), content_type='application/json')
