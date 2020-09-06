import datetime
from .models import MarketingMessage
from django.http import HttpResponse

class DisplayMarketing(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(datetime.datetime.now())
        try:
            request.session['marketing_message'] = MarketingMessage.objects.all()[0].message
        except:
            request.session['marketing_message'] = False
        print(request.session['marketing_message'])
        return self.get_response(request)

    def process_request(self, request):
       print('chima')
       try:
            request.session['marketing_message'] = MarketingMessage.objects.all()[0].message
       except:
            request.session['marketing_message'] = False
    