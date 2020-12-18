from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserModel(AbstractUser):
    first_name = None
    last_name = None
    last_login = None
    is_staff = None
    is_superuser = None
    name = models.CharField(max_length=255, verbose_name='真实姓名', null=True, blank=True)
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    roles = models.ManyToManyField('RoleModel', related_name='user', verbose_name='角色', blank=True)

    class Meta:
        db_table = 'system_user'
        verbose_name = '用户表'


class Permission(models.Model):
    insert_time = models.DateTimeField(auto_now_add=True, verbose_name='插入时间')
    method = models.CharField(max_length=20, verbose_name='请求方法', null=True, blank=True)
    url = models.CharField(max_length=255, verbose_name='请求路由', null=True, blank=True)
    params = models.CharField(max_length=255, verbose_name='参数', null=True, blank=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'system_permission'
        verbose_name = '权限表'


class RoleModel(models.Model):
    insert_time = models.DateTimeField(auto_now_add=True, verbose_name='插入时间')
    name = models.CharField(max_length=255, verbose_name='角色名称', null=True, blank=True)
    info = models.TextField(verbose_name='角色描述', null=True, blank=True)
    key = models.IntegerField(verbose_name='唯一标识', null=True, blank=True)
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    permissions = models.ManyToManyField('Permission', related_name='role', verbose_name='权限', blank=True)

    class Meta:
        db_table = 'system_role'
        verbose_name = '角色表'
