from django.urls import path,re_path,include
from . import views

app_name='index'
urlpatterns = [
    # re_path(r'index_(?P<name>.+)/$', views.hello2),

    # path('index/', views.index),
    # path('add/', views.add,name='add'),
    # path('list/',views.question_list,name='list'),

    #文章
    path('article/', views.article, name='article'),
    path('alist/', views.article_list, name='alist'),
    path('article/<int:article_id>/', views.article_detail, name='adetail'),
    path('comment/',views.comment_add,name='comment')
    #投票地址
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]