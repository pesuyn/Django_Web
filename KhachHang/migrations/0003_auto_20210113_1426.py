# Generated by Django 2.2 on 2021-01-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KhachHang', '0002_auto_20210113_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
