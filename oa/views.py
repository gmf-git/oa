import os
import time

import pypinyin
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


class FileUpload(APIView):

    def post(self, request, *args, **kwargs):
        model = kwargs.get('model')
        user = request.user.name
        print(user)
        file = request.data.get('file')
        txt = os.path.splitext(str(file))[1].strip('"')
        file_name = ''.join(pypinyin.lazy_pinyin(user)) + str(time.time().as_integer_ratio()[0]) + txt
        file_url = f'{settings.MEDIA_URL}{model}/{file_name}'
        file_local = os.path.join(settings.STATIC_ROOT, model)
        if not os.path.exists(file_local):
            os.makedirs(file_local)
        path = file_local + '/' + file_name
        with open(path, 'wb') as f:
            f.write(file.read())
        return Response({'url': file_url, 'path': path})
