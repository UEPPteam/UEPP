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

    url(r'^major_information', major_information),
    url(r'^teacher_information', teacher_information),


]