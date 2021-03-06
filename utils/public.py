from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class DefineViewSet(ModelViewSet):
    """自定义序列化器"""
    list_serializer = None
    create_serializer = None

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.list_serializer
        return self.create_serializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete = True
        instance.save()
        return Response('删除成功', status=status.HTTP_204_NO_CONTENT)


def get_keywords(params, fields_map):
    """
    获取keywords
    :param params: 拼接参数
    :param fields_map: 字段映射字典
    :return:
    """
    data = {}
    for k, v in fields_map.items():
        middle = params.get(v)
        if middle:
            data.setdefault(k, middle)
    return data
