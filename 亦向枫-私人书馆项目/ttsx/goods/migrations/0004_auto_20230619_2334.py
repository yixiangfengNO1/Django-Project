# Generated by Django 2.2 on 2023-06-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20230612_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='goods_price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
