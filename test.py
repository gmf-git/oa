import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oa.settings')
django.setup()
# 测试环境
if __name__ == '__main__':
    from system import models as system_models
    from utils.email import send_mail

    users = system_models.UserModel.objects.all()
    permissions = system_models.Permission.objects.all()
    roles = system_models.RoleModel.objects.all()
    menus = system_models.MenuModel.objects.all()
    print(users)
    print(permissions)
    print(roles)
    print(menus)
