from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
def demo(request):
    now=datetime.now()
    return render(request,'datetime.html',{'current_date':now})

