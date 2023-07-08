# 创建时间：2023/6/29
# 创建目的：学习python
# 自定义中间件类
from django.shortcuts import redirect
from django.urls import reverse

import re


class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Shopmiddleware")

    def __call__(self, request):
        path = request.path
        print("url:", path)
        # 判断管理后台是否登录
        urllist = ['/myadmin/login', '/myadmin/loginout', '/myadmin/dologin', '/myadmin/verify']
        # 判断当前请求url地址是否以/myadmin开头,并且不再urllist中，才做是否登录判断
        if re.match(r'^/myadmin', path) and (path not in urllist):
            # 判断是否登录（key名为adminuser是否存在于session中）
            if 'adminuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse("myadmin_login"))

        # 判断当前请求是否是访问网站前台
        if re.match(r"^/web", path):
            # 判断当前用户是否没有登录
            if "webuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('web_login'))

        # 移动端请求路由判断
        # 定义网站移动端不用登录也可访问的路由url
        urllist = ['/mobile/register', '/mobile/doregister']
        # 判断当前请求是否是请求移动端,并且path不在urllist中
        if re.match(r"^/mobile", path) and (path not in urllist):
            # 判断当前用户是否没有登录移动端
            if "mobileuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('mobile_register'))
        # Code to be executed for each request/response after
        # the view is called.
        response = self.get_response(request)
        return response
