# Generated by Django 2.2 on 2021-01-12 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KhachHang', '0009_auto_20210104_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KhachHang.label'),
        ),
    ]