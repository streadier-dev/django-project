from django.http import HttpResponse

from datetime import datetime

def hello_world(request):
    now = datetime.now()
    return HttpResponse(' la hora del servidor es {now}'.format(now =str(now)))