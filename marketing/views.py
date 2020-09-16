import json
from django.shortcuts import render, HttpResponse, Http404
from django.utils import timezone
import datetime

# Create your views here.
def dismiss_marketing_message(request):
    print(timezone.now())
    print('chima ')
    print(timezone.now() + datetime.timedelta(seconds=8))
    if request.is_ajax():
        data = {"success": True}
        print(data)
        json_data = json.dumps(data)
        request.session['dismiss_message_for'] = str(timezone.now() + datetime.timedelta(seconds=8))
        print(json_data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        raise Http404

