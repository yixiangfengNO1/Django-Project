# 前台大堂点餐端子路由文件
from django.urls import path, include

from web.views import index, cart, orders

urlpatterns = [
    path('', index.index, name="index"),  # 前台大堂点餐首页

    # 前台管理员路由
    path('login', index.login, name="web_login"),
    path('dologin', index.dologin, name="web_dologin"),
    path('logout', index.logout, name="web_logout"),
    path('verify', index.verify, name="web_verify"),  # 验证码
    #为url路由添加请求前缀web/,凡是带此前缀的url地址必须登录后才可访问
    path('web/', include([
        path('', index.webIndex, name="web_index"),  # 前台大堂点餐首页
        # 购物车信息管理路由配置
        path('cart/add/<str:pid>', cart.add, name="web_cart_add"),  # 购物车添加
        path('cart/del/<str:pid>', cart.delete, name="web_cart_del"),  # 购物车删除
        path('cart/clear', cart.clear, name="web_cart_clear"),  # 购物车清空
        path('cart/change', cart.change, name="web_cart_change"),  # 购物车更改
        # 订单处理
        path('orders/<int:pIndex>', orders.index, name="web_orders_index"), #浏览订单
        path('orders/insert', orders.insert, name='web_orders_insert'),  # 执行订单添加操作
        path('orders/detail', orders.detail,name='web_orders_detail'), #订单的详情信息
        path('orders/status', orders.status,name='web_orders_status'), #修改订单状态
    ]))
]
