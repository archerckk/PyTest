from django.urls import path,re_path,include
from . import views

app_name='index'
urlpatterns = [
    # re_path(r'index_(?P<name>.+)/$', views.hello2),

    # path('index/', views.index),
    # path('add/', views.add,name='add'),
    # path('list/',views.question_list,name='list'),

    #添加文章
    path('<int:user_id>/add_article/', views.add_article, name='article'),
    #显示文章列表
    path('<int:user_id>/alist/', views.article_list, name='alist'),
    #进入文章详情
    path('<int:user_id>/article/<int:article_id>/', views.article_detail, name='adetail'),
    #添加评论
    path('comment/',views.comment_add,name='comment'),
    #注册
    path('register/',views.register,name='register'),
    #登录
    path('login/',views.login,name='login')

    #投票地址
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]