# Generated by Django 2.2 on 2021-01-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KhachHang', '0008_orderitem_trade_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cart',
        ),
        migrations.AlterField(
            model_name='report',
            name='create_day',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]