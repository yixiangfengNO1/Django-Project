from django.db import models


class User(models.Model):
    username = models.CharField("用户账号", max_length=100, unique=True)
    password = models.CharField("密码", max_length=32, unique=False)
    email = models.EmailField("邮箱")

    class Meta:
        db_table = "user"
        verbose_name = "浏览用户信息"
        verbose_name_plural = "用户信息管理"
