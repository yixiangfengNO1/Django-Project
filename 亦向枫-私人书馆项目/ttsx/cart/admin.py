from django.contrib import admin
from .models import *


# Register your models here.
class OrderInfoManager(admin.ModelAdmin):
    list_display = ["order_id", "order_addr", "order_recv", "order_tele", "order_fee", "order_extra",
                    "order_status"]  # 控制列表页要显示的字段
    search_fields = ["order_id", "order_recv", "order_tele"]  # 模糊查询
    list_filter = ["order_recv"]  # 列表页过滤条件
    list_editable = ["order_addr", "order_recv", "order_tele", "order_fee", "order_extra",
                     "order_status"]  # 指定哪些字段可以直接在列表页编辑
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True

    # 是否显示列表页数据数量([选中了n个中的m个])
    actions_selection_counter = True


class OrderGoodsManager(admin.ModelAdmin):
    list_display = ["goods_info", "goods_num", "goods_order"]  # 控制列表页要显示的字段
    search_fields = ["goods_info", "goods_order"]  # 模糊查询
    list_filter = ["goods_info"]  # 列表页过滤条件
    list_editable = ["goods_num"]  # 指定哪些字段可以直接在列表页编辑
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True

    # 是否显示列表页数据数量([选中了n个中的m个])
    actions_selection_counter = True


admin.site.register(OrderInfo, OrderInfoManager)
admin.site.register(OrderGoods, OrderGoodsManager)
