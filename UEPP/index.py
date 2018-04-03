# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

#表单
def index(request):
    return render_to_response('dashboard.html')