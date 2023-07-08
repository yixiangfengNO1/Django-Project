from django.contrib import admin
from .models import *

admin.site.site_header = "私人书馆后台管理"


# Register your models here.
class UserManager(admin.ModelAdmin):
    list_display = ["username", "password", "email"]  # 控制列表页要显示的字段
    search_fields = ["username"]  # 模糊查询
    list_filter = ["username"]  # 列表页过滤条件
    list_editable = ["email"]  # 指定哪些字段可以直接在列表页编辑
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True

    # 是否显示列表页数据数量([选中了n个中的m个])
    actions_selection_counter = True


admin.site.register(User, UserManager)
