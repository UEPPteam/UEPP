# -*- coding:utf-8 -*-

from django.shortcuts import render

# 接收post请求数据
from django.template.context_processors import csrf


def search_post(request):
    ctx={}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt']=request.POST['q']
        return render(request, "post.html", ctx)