# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context={}
    context['hello']='hello django!'
    return render(request, 'hello.html', context)
