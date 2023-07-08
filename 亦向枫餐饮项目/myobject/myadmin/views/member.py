# 创建时间：
# 创建目的：
# 会员信息视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from myadmin.models import Member


# ==============后台会员信息管理======================
# 浏览会员信息
def index(request, pIndex=1):
    mod = Member.objects

    list = mod.filter(status__lt=9)
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list, 5)  # 以5条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表

    # 封装信息加载模板输出
    context = {"memberlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages}
    return render(request, "myadmin/member/index.html", context)
