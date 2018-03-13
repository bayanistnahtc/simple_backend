from django.shortcuts import render
# from django.http import JsonResponse	
import logging
import json
from django.http import HttpResponse

# Get an instance of a logger
logger = logging.getLogger(__name__)

def schedule_list(request):
    return render(request, 'schedule/schedule_list.html', {})

def group_schedule(request, fac, pk):

    data = ''
    dump = json.dumps({'error': 'error'})
    try:
        data = json.load(open('static/'+fac+'.json'))
    except:
    	logger.error(fac + ' No such faculty!')

    if data != '':
    	try:
    	    dump = json.dumps(data[pk])
    	    return HttpResponse(dump, content_type='application/json')
    	except:
    		logger.error(pk + ' No such group!')
    return HttpResponse(dump, content_type='application/json')
