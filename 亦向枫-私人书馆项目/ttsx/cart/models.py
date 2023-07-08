from django.db import models
from goods.models import GoodsInfo

"""
不写主键，django会自动创建一个名为id字段的主键，并自动增长
"""


class OrderInfo(models.Model):
    """订单信息模型"""
    status = (
        (1, '代付款'),
        (2, '代付款'),
        (3, '代付款'),
        (4, '代付款'),
    )
    # 订单编号
    order_id = models.CharField( max_length=100)
    # 收货地址
    order_addr = models.CharField("收货地址", max_length=100)
    # 收货人
    order_recv = models.CharField("收货人", max_length=50)
    # 联系电话
    order_tele = models.CharField("联系电话", max_length=11)
    # 运费
    order_fee = models.IntegerField("运费", default=10)
    # 订单备注
    order_extra = models.CharField("订单备注", max_length=200)
    # 订单状态
    order_status = models.IntegerField("订单状态", default=1, choices=status)

    class Meta:
        db_table = "cart_orderinfo"
        verbose_name = "浏览订单信息表"
        verbose_name_plural = "订单信息管理"


class OrderGoods(models.Model):
    """订单商品模型"""
    # 所属商品
    # goods_info = models.ForeignKey('goods.GoodsInfo',on_delete=models.CASCADE)
    goods_info = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="所属商品")
    # 商品数量
    goods_num = models.IntegerField("商品数量")
    # 商品所属订单
    goods_order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="商品所属订单")

    class Meta:
        db_table = "cart_ordergoods"
        verbose_name = "浏览订单商品表"
        verbose_name_plural = "订单商品管理"
