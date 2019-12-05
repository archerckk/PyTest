from django.http import HttpResponse

def demo(request,name):
    return HttpResponse('Hello,{}!!!'.format(name))
