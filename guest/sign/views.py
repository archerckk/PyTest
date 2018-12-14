from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import  Event

# Create your views here.
# def index(request):
#     return HttpResponse('Hello Django!!!')

def index(request):
    return render(request,'index.html')

#登陆动作
def login_action(request):
    if request.method=='POST':
        '通过request.POST获取POST请求，通过.get()方法获取username属性，如果为空则返回空字符串'
        username=request.POST.get('username','')

        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            response = HttpResponseRedirect('/event_manage')
            response.set_cookie('user',username,3600)#添加浏览器cookie
            return response
        # if username=='123' and password=='123':
        #     # return HttpResponse('登陆成功！')
        #     # return HttpResponseRedirect('/event_manage/')
        #     response=HttpResponseRedirect('/event_manage')
        #     # response.set_cookie('user',username,3600)#添加浏览器cookie
        #     request.session['user']=username#将session信息记录到浏览器
        #     return response
        else:
            return render(request,'index.html',{'error':'用户名或者密码错误！'})
#
#发布会管理
@login_required
def event_manage(request):
    # username=request.COOKIES.get('user','')#读取浏览器cookie
    # # username=request.session.get('user','')#读取浏览器session
    # return render(request,'event_manage.html',{'user':username})

    event_list=Event.objects.all()
    username=request.session.get('user','')
    return render(request,'event_manage.html',{'user':username,
                                               'events':event_list})

