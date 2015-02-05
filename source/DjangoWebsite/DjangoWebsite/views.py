from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
def home(request):
    return render_to_response('home.html')
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    assert False
    return HttpResponse(html)
