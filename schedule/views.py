from django.shortcuts import render
# from django.http import JsonResponse
import json
from django.http import HttpResponse

def schedule_list(request):
    return render(request, 'schedule/schedule_list.html', {})

def group_schedule(request, pk):

    data = json.load(open('schedule/result.json'))

    dump = json.dumps(data[pk])
    return HttpResponse(dump, content_type='application/json')
