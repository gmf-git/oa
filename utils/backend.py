from django.db.models import Q

from system.models import UserModel


def check_password(user, password):
    if user.password == password:
        return True


class AuthorBackend:
    """用户认证"""

    @staticmethod
    def authenticate(request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username=username) | Q(email=username))
            if check_password(user, password):
                return user
        except Exception as f:
            print(f)
            return
