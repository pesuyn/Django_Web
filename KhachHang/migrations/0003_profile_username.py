# Generated by Django 2.2 on 2020-12-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KhachHang', '0002_auto_20201227_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
