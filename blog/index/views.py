from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):

    return HttpResponse('hello world!!!')

def hello2(request,name):

    return HttpResponse('hello {}!!!'.format(name))