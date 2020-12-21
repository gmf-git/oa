from django.db.models import Q

from system.models import MenuModel


def jwt_response_payload_handler(token, user=None, request=None):
    first_menus = MenuModel.objects.filter(Q(child__role__user=user) | Q(child__child__role__user=user),
                                           parent__isnull=True).distinct()

    def get_menus(menus):
        data = []
        if not menus:
            return data
        for menu in menus:
            data.append(
                {
                    'name': menu.name,
                    'path': menu.path,
                    'children': get_menus(menu.child.filter(Q(role__user=user) | Q(child__role__user=user)).distinct())
                }
            )
        return data

    meuns = get_menus(first_menus)
    return {
        'token': token,
        'meuns': meuns
    }
