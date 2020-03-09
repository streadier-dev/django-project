from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth , %T - %H:%M hrs')
    return HttpResponse(' la hora del servidor es {now}'.format(now=str(now)))
    

def hi(request):
    numbers_string = request.GET['numbers'].split(',')
    print(numbers_string)
    numbers_string2 = request.GET['numbers']
    print(numbers_string2)
    numbers_integer = list(map(int, numbers_string))
    numbers_integer.sort()
    return JsonResponse(numbers_integer, safe =False)