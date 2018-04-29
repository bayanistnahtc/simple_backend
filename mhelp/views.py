from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper

def download(request, file):
    file_path = "static/" + file
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404

