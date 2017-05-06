from django.http import HttpResponse

import datetime


def hello(request):
	return HttpResponse("Hello Baa_!")



def current_datetime(request):
	now = datetime.datetime.now()
	html = "It i now %s." % now
	return HttpResponse(html)




from django.http import Http404, HttpResponse
# import datetime

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be  %s." % (offset, dt)
    return HttpResponse(html)