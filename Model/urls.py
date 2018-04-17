# -*- coding: utf-8 -*-
from django.conf.urls import url
from Model.views import *

urlpatterns = [
#基础信息
    #课程信息
    url(r'^course_information', course_information),
    url(r'^courseModify', courseModify),
    url(r'^courseDelete', courseDelete),
    url(r'^courseAdd', courseAdd),
    url(r'^subject', subject),
    url(r'^subMod', subMod),
    url(r'^subDel', subDel),
    url(r'^subAdd', subAdd),
    url(r'^spe_sub', spe_sub),
    url(r'^speAdd', speAdd),
    url(r'^speMod', speMod),
    url(r'^speDel', spebDel),

    #课程模块
    url(r'^courseModule/', courseModule),
    url(r'^courseModuleAdd/', courseModuleAdd),
    url(r'^courseModuleModify/', courseModuleModify),
    url(r'^courseModuleDelete/', courseModuleDelete),
    #课程种类
    url(r'^courseCategory', courseCategory),
    url(r'^courseCategoryAdd', courseCategoryAdd),
    url(r'^course_dis', course_dis),
    url(r'^cdAdd', cdAdd),
    url(r'^cdMod', cdMod),
    url(r'^cdDel', cdDel),
    url(r'^spec_course', spec_course),
    url(r'^scAdd', scAdd),
    url(r'^scMod', scMod),
    url(r'^scDel', scDel),
    url(r'^elec_course', elec_course),
    url(r'^ecAdd', ecAdd),
    url(r'^ecMod', ecMod),
    url(r'^ecDel', ecDel),
    url(r'^e_course', e_course),
    url(r'^eecAdd', eecAdd),
    url(r'^eecMod', eecMod),
    url(r'^eecDel', eecDel),
    url(r'^courseCategory/', courseCategory),
    url(r'^courseCategoryAdd/', courseCategoryAdd),
    url(r'^courseCategoryModify/', courseCategoryModify),
    url(r'^courseCategoryDelete/', courseCategoryDelete),
    #课程
    url(r'^courses/', courses),
    url(r'^coursesAdd/', coursesAdd),
    url(r'^coursesModify/', coursesModify),
    url(r'^coursesDelete/', coursesDelete),
    #先行课
    url(r'^coursePrevious/', coursePrevious),
    url(r'^coursePreviousAdd/', coursePreviousAdd),
    url(r'^coursePreviousModify/', coursePreviousModify),
    url(r'^coursePreviousDelete/', coursePreviousDelete),

#培养方案
    #版本
    url(r'^educationOverview/', educationOverview),
    url(r'^educationOverviewAdd/', educationOverviewAdd),
    url(r'^educationOverviewModify/', educationOverviewModify),
    url(r'^educationOverviewDelete/', educationOverviewDelete),
    #专业
    url(r'^educationMajor/', educationMajor),
    url(r'^educationMajorAdd/', educationMajorAdd),
    url(r'^educationMajorModify/', educationMajorModify),
    url(r'^educationMajorDelete/', educationMajorDelete),
]