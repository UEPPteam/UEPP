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
    url(r'^speDel', spebDel)
]