# Generated by Django 2.2.6 on 2020-12-21 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20201218_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='info',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='功能详情'),
        ),
    ]
