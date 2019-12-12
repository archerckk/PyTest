from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import Question as q
from .models import Choice,Article,Comment,User
from django.utils import timezone
from .form import Resgister_form
from django.template import RequestContext
# Create your views here.

def hello(request):

    return HttpResponse('hello world!!!')

def hello2(request,name):

    return HttpResponse('hello {}!!!'.format(name))

# def question_list(request):
#     questions=q.objects.order_by('-id').all()
#     print(questions)
#     return render(request,'list.html',{'questions':questions})

#注册
def register(request):

    if request.method=='GET':
        print('执行get')
        register_form=Resgister_form()
        print('执行表单')
        return render(request,'register.html',{'register_form':register_form})
        # return render(request,'register.html')
    else:
        print('执行post')
        register_form = Resgister_form(request.POST)

        if register_form.user_name.isspace() or len(register_form.user_name)==0:
            return render(request, 'register.html', {'register_form':register_form,
                                                     'error':'你的账号为空，请输入！'})

        elif register_form.password.isspace() or len(register_form.password)==0:
            return render(request, 'register.html', {'register_form':register_form,
                                                     'error': '你的密码为空，请输入！'})

        elif register_form.password_repeat.isspace() or len(register_form.password_repeat)==0:
            return render(request, 'register.html', {'register_form':register_form,
                                                     'error': '你的确认密码为空，请输入！'})

        elif register_form.password_repeat!=register_form.password:
            return render(request, 'register.html', {'register_form':register_form,
                                                     'error': '你两次输入的密码不一致，清重新输入'})
        elif register_form.is_valid():
            user = User()
            user.user_name=register_form.cleaned_data['user_name']
            user.password=register_form.cleaned_data['password']
            user.save()
            return HttpResponseRedirect(reverse("index:alist"), kwargs={"user_name": register_form.user_name})
        return render(request,'register.html',{'register_form':register_form})






    #HTML表单代码
    # if request.method=='POST':
    #     user_name=request.POST.get('user_name').strip()
    #     password=request.POST.get('password')
    #     password_repeat=request.POST.get('password2')
    #
    #     if user_name.isspace() or len(user_name)==0:
    #         return render(request, 'register.html', {'error':'你的账号为空，请输入！'})
    #
    #     elif password.isspace() or len(password)==0:
    #         return render(request, 'register.html', {'error': '你的密码为空，请输入！'})
    #
    #     elif password_repeat.isspace() or len(password_repeat)==0:
    #         return render(request, 'register.html', {'error': '你的确认密码为空，请输入！'})
    #
    #     elif password_repeat!=password:
    #         return render(request, 'register.html', {'error': '你两次输入的密码不一致，清重新输入'})
    #
    #     else:
    #         user=User()
    #         user.user_name=user_name
    #         user.password=password
    #         user.save()
    #         return HttpResponseRedirect(reverse("index:alist"),kwargs={"user_name":user_name})
    #
    # return render(request,'register.html')


def article(request):
    # print('测试代码：', request.method)
    if request.method=='GET':
        print('get method')
        return render(request, 'article.html', {'method': request.method})

    if request.method == "POST":
        print('测试代码：',request.method)
        title=request.POST.get('title')
        content=request.POST.get('content')

        print(title,content)

        a=Article(title=title,content=content)
        a.save()
        return HttpResponseRedirect(reverse("index:alist"))
        # return render(request,'alist.html')


def article_detail(request,article_id):
    print(article_id)
    article = get_object_or_404(Article, pk=article_id)

    comments=Comment.objects.filter(article_id_id=article_id).order_by('-id').all()
    print(len(comments))
    return render(request,'adetail.html',{'article':article,'comments':comments})
    # return render(request,'adetail.html',{'article':article})

def article_list(request):
    a=Article.objects.order_by('-id').all()
    print(a)
    return render(request,'alist.html',{'articles':a})

#评论添加
def comment_add(request):

    if request.method=='POST':
        article_id=request.POST.get('article_id')
        content=request.POST.get('com_content')
        print(content)
        if content==''or content==None or len(content)==0:
            return JsonResponse({'status': '10001', 'message': 'comment is none'})
        else:
            comment=Comment()
            #外键约束的新增正确方式
            comment.article_id=Article(id=article_id)
            comment.content=content
            comment.save()
            return HttpResponseRedirect(reverse("index:adetail",args=article_id,))


def add(request):
    print(request.method)
    if request.method=='POST':
        print(request.method)
        title=request.POST.get('title',None)
        question_text=request.POST.get('question_text',None)
        print(title)
        print(question_text)

        qustion=q(title=title,question_text=question_text,pub_date=timezone.now())
        qustion.save()
        return HttpResponseRedirect('/index/list')

    return render(request,'add.html')




#投票
# def index(request):
#     latest_question_list = q.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'index.html', context)
# # #详情
# def detail(request, question_id):
#     question = get_object_or_404(q, pk=question_id)
#     return render(request, 'detail.html', {'question': question})
# #结果
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
# #投票2
# def vote(request, question_id):
#     question = get_object_or_404(q, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('index:results', args=(question.id,)))