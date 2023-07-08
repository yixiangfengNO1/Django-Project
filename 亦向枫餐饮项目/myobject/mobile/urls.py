# 移动端子路由文件
from django.urls import path

from mobile.views import index, cart
from mobile.views import member

urlpatterns = [
    path('', index.index, name="mobile_index"),  # 移动端首页

    # 会员注册/登录
    path('register', index.register, name="mobile_register"),  # 移动端会员注册/登录表单页
    path('doregister', index.doRegister, name="mobile_doregister"),  # 执行注册或登录
    # 店铺选择
    path('shop', index.shop, name="mobile_shop"),  # 移动端店铺选择页
    path('shop/select', index.selectShop, name="mobile_selectshop"),  # 执行移动端店铺选择
    # 订单处理
    path('orders/add', index.addOrders, name="mobile_addorders"),  # 加载移动端订单页
    path('orders/doadd', index.doAddOrders, name="mobile_doaddorders"),  # 执行移动端下单操作
    # 购物车信息管理路由配置
    path('cart/add', cart.add, name="mobile_cart_add"),
    path('cart/del', cart.delete, name="mobile_cart_del"),
    path('cart/clear', cart.clear, name="mobile_cart_clear"),
    path('cart/change', cart.change, name="mobile_cart_change"),
    # 会员中心
    path('member', member.index, name="mobile_member_index"),  # 会员中心首页
    path('member/orders', member.orders, name="mobile_member_orders"),  # 加载会员中心订单页
    path('member/detail', member.detail, name="mobile_member_detail"),  # 加载会员订单详情页
    path('member/logout', member.logout, name="mobile_member_logout"),  # 执行退出
]
