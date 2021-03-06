# Generated by Django 2.2.6 on 2020-12-21 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_permission_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='插入时间')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='菜单名称')),
                ('path', models.CharField(blank=True, max_length=255, null=True, verbose_name='前端路由')),
                ('info', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='system.MenuModel')),
            ],
            options={
                'verbose_name': '菜单表',
                'db_table': 'system_menu',
            },
        ),
        migrations.AddField(
            model_name='rolemodel',
            name='menus',
            field=models.ManyToManyField(blank=True, related_name='role', to='system.MenuModel', verbose_name='菜单'),
        ),
    ]
