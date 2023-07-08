from django.contrib import admin
from .models import GoodsInfo,GoodsCategory


# Register your models here.
class GoodsInfoManager(admin.ModelAdmin):
    list_display = ["goods_name", "goods_price", "goods_desc", "goods_img", "goods_cag"]  # 控制列表页要显示的字段
    search_fields = ["goods_name"]  # 模糊查询
    list_filter = ["goods_name"]  # 列表页过滤条件
    list_editable = ["goods_price", "goods_desc"]  # 指定哪些字段可以直接在列表页编辑
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True

    # 是否显示列表页数据数量([选中了n个中的m个])
    actions_selection_counter = True


class GoodsCategoryManager(admin.ModelAdmin):
    list_display = ["cag_name", "cag_css", "cag_img"]  # 控制列表页要显示的字段
    search_fields = ["cag_name"]  # 模糊查询
    list_filter = ["cag_name"]  # 列表页过滤条件
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True

    # 是否显示列表页数据数量([选中了n个中的m个])
    actions_selection_counter = True


admin.site.register(GoodsInfo, GoodsInfoManager)
admin.site.register(GoodsCategory, GoodsCategoryManager)
