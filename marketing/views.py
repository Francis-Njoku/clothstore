import json
from django.shortcuts import render, HttpResponse, Http404
from django.utils import timezone
from django.http import HttpResponseBadRequest
import datetime
from accounts.models import EmailMarketingSignUp

from .forms import EmailForm

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

def email_signup(request):
    if request.method == "POST":
        form = EmailForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.session['email_added_marketing'] = True
            new_signup = EmailMarketingSignUp.objects.create(email=email)
            print(form.cleaned_data['email'])
            return HttpResponse('Success')
        if form.errors:
            print(form.errors)
            json_data = json.dumps(form.errors)    
            return HttpResponseBadRequest(json_data, content_type='application/json')
    else:
        raise Http404        