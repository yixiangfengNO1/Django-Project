from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import GoodsInfo, GoodsCategory
from django.core.paginator import Paginator


@csrf_exempt
def index2(request):
    """首页页面"""
    categories = GoodsCategory.objects.all()  # 查询商品分类
    # categories 为各个商品分类信息  QuerySet类型
    for cag in categories:
        # 从每个分类中获取最后四个商品，作为最新商品数据
        # order_by 是排序 这里是根据id反向排序  从大到小  [:4]切片是获取结果集中的前4个
        # 一对多关系，查询多的一方 会在一的一方有一个属性 多的一方 模型类名小写_set
        # cag 会商品分类对象
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]

    # 读取购物车商品列表
    cart_goods_list = []
    # 商品总数
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        # 商品ID都为数字, 非数字的cookie过滤掉
        if not goods_id.isdigit():
            continue
        # 具体的商品
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 购买数量
        cart_goods.goods_num = goods_num
        # 显示
        cart_goods_list.append(cart_goods)
        # 累加购物车商品总数
        cart_goods_count = cart_goods_count + int(goods_num)
    return render(request, 'index.html', {'categories': categories,
                                          'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count})


def detail(request):
    """商品详情页面"""
    # request.GET 是一个QueryDict
    goods_id = request.GET.get('id', '')  # 获得产品ID
    goods_data = GoodsInfo.objects.get(id=goods_id)  # 查询该商品
    categories = GoodsCategory.objects.all()  # 查询商品分类

    cart_goods_list = []  # 读取购物车商品列表
    cart_goods_count = 0  # 商品总数
    for goods_id, goods_num in request.COOKIES.items():
        # 商品ID都为数字, 非数字的cookie过滤掉
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
        # 累加购物车商品总数
        cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'detail.html', {'categories': categories,
                                           'goods_data': goods_data,
                                           'cart_goods_list': cart_goods_list,
                                           'cart_goods_count': cart_goods_count})


def goods(request):
    """商品展示页面"""
    cag_id = request.GET.get('cag', 1)    # 获得当前分类
    page_id = request.GET.get('page', 1)  # 获得当前页码
    # 查询所有数据
    goods_data = GoodsInfo.objects.filter(goods_cag_id=cag_id)
    paginator = Paginator(goods_data, 12)     # 数据分页

    page_data = paginator.page(page_id)       # 获得当前页码数据
    categories = GoodsCategory.objects.all()  # 查询商品分类
    current_cag = GoodsCategory.objects.get(id=cag_id)  # 查询当前商品分类
    cart_goods_list = []  # 读取购物车商品列表
    cart_goods_count = 0  # 商品总数
    for goods_id, goods_num in request.COOKIES.items():
        # 商品ID都为数字, 非数字的cookie过滤掉
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
        # 累加购物车商品总数
        cart_goods_count = cart_goods_count + int(goods_num)
    return render(request, 'goods.html', {'page_data': page_data,
                                          'categories': categories,
                                          'current_cag': current_cag,
                                          'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count,
                                          'paginator': paginator,
                                          'cag_id': cag_id})


# from goods.models import *
# cag = GoodsCategory.objects.get(id=1)
# goods_list = GoodsInfo.objects.filter(goods_cag=cag)
# goods_list.count()


# from goods.models import *
# cag = GoodsCategory.objects.get(id=1)
# goods_list = GoodsInfo.objects.filter(goods_cag = cag)
# goods_list.count()  99
