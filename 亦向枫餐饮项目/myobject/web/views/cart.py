# 购物车信息管理视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def add(request, pid):
    '''添加购物车'''
    # 从session中的菜品列表productlist中获取要添加购物车中的菜品信息
    product = request.session['productlist'][pid]
    product['num'] = 1  # 追加一个购买数量，默认为1
    # 从session中获取购物车cartlist信息，若没有默认为空字典{}
    cartlist = request.session.get("cartlist", {})
    # 判断购物车中是否已存在要购买的商品
    if pid in cartlist:
        cartlist[pid]['num'] += product['num']  # 累加购买量
    else:
        cartlist[pid] = product  # 将菜品放入购物车中
    # 将购物车中的商品信息放回到session中
    request.session['cartlist'] = cartlist
    # 跳转查看购物车
    return redirect(reverse('web_index'))


def delete(request, pid):
    '''删除购物车中的商品'''
    # 尝试从session中获取名字为cartlist的购物车信息，若没有返回{}
    cartlist = request.session['cartlist']
    del cartlist[pid]
    # 将cartlist购物车信息放入session中
    request.session['cartlist'] = cartlist
    # 跳转到订餐首页
    return redirect(reverse('web_index'))


def clear(request):
    '''清空购物车'''
    request.session['cartlist'] = {}
    return redirect(reverse('web_index'))


def change(request):
    '''购物车信息修改'''
    cartlist = request.session['cartlist']
    shopid = request.GET.get("pid", 0)
    num = int(request.GET.get('num', 1))
    if num < 1:
        num = 1
    cartlist[shopid]['num'] = num
    request.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))
