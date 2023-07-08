# 订单信息管理视图文件
from django.core.paginator import Paginator
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
from myadmin.models import Orders, OrderDetail, Payment, User


def index(request, pIndex=1):
    '''浏览信息'''
    umod = Orders.objects
    # 获取当前店铺id号
    sid = request.session['shopinfo']['id']  # 获取当前店铺id号
    ulist = umod.filter(shop_id=sid)
    mywhere = []
    # 获取、判断并封装状态status搜索条件(未做可以后序自己完成)
    status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status=" + status)
    ulist = ulist.order_by("id")  # 对id排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 10)  # 以每页10条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息
    for vo in list2:
        if vo.user_id == 0:
            vo.nickname = "无"
        else:
            user = User.objects.only("nickname").get(id=vo.user_id)
            vo.nickname = user.nickname
    context = {"orderslist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpage': maxpages, 'mywhere': mywhere}
    return render(request, "web/list.html", context)


def insert(request, pIndex=1):
    '''执行订单添加'''
    '''大堂执行订单添加操作'''
    try:
        # 执行订单信息添加操作
        od = Orders()
        od.shop_id = request.session['shopinfo']['id']  # 店铺id号
        od.member_id = 0  # 会员id
        od.user_id = request.session['webuser']['id']  # 操作员id
        od.money = request.session['total_money']
        od.status = 1  # 订单状态:1过行中/2无效/3已完成
        od.payment_status = 2  # 支付状态:1未支付/2已支付/3已退款
        od.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.save()

        # 执行支付信息添加
        op = Payment()
        op.order_id = od.id  # 订单id号
        op.member_id = 0  # 会员id号
        op.money = request.session['total_money']  # 支付款
        op.type = 2  # 付款方式：1会员付款/2收银收款
        op.bank = request.GET.get("bank", 3)  # 收款银行渠道:1微信/2余额/3现金/4支付宝
        op.status = 2  # 支付状态:1未支付/2已支付/3已退款
        op.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.save()

        # 执行订单详情添加
        cartlist = request.session.get('cartlist', {})
        # 遍历购物车中的菜品并添加到订单详情中
        for shop in cartlist.values():
            ov = OrderDetail()
            ov.order_id = od.id
            ov.product_id = shop['id']
            ov.product_name = shop['name']
            ov.price = shop['price']
            ov.quantity = shop['num']
            ov.status = 1
            ov.save()
        del request.session['cartlist']
        del request.session['total_money']
        return HttpResponse("Y")
    except Exception as err:
        print(err)
        context = {"info": "订单添加失败，请稍后再试！"}
        return HttpResponse("N")


def get_order_statistics(shop_id):
    # 使用原生SQL语句查询数据库来完成订单和销售额的统计
    # 查询当前店铺的订单数量和销售额
    query = '''
        SELECT COUNT(*) AS order_count, SUM(money) AS total_sales
        FROM orders
        WHERE shop_id = %s AND status = 1
    '''
    with connection.cursor() as cursor:
        cursor.execute(query, [shop_id])
        result = cursor.fetchone()

    if result:
        order_count = result[0]
        total_sales = result[1]
    else:
        order_count = 0
        total_sales = 0.0

    return order_count, total_sales


def detail(request):
    '''加载订单信息'''
    oid = request.GET.get("oid")
    shop_id = request.GET.get("shop_id")

    # 加载订单详情
    dlist = OrderDetail.objects.filter(order_id=oid)

    # 计算订单数量
    order_count = dlist.count()

    # 计算销售额
    total_sales = 0
    for item in dlist:
        total_sales += item.price * item.quantity

    context = {
        'detaillist': dlist,
        'order_count': order_count,
        'total_sales': total_sales
    }

    return render(request, "web/detail.html", context)


def status(request):
    ''' 修改订单状态 '''
    try:
        oid = request.GET.get("oid", '0')
        ob = Orders.objects.get(id=oid)
        ob.status = request.GET['status']
        ob.save()
        return HttpResponse("Y")
    except Exception as err:
        print(err)
        return HttpResponse("N")
