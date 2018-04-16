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
]