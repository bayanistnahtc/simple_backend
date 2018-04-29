from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def download(request, file):
    file_path = os.path.join(settings.STATIC_ROOT, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    # raise Http404

