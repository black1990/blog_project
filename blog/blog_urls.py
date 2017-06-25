from  django.conf.urls import url
from . import views
urlpatterns=[
    # url(r'^$',views.index,name='index'),
    url(r'^$',views.IndexView.as_view(),name='index'),#使用系统自带的通用视图
    #url(r'^(?P<article_id>[0-9]+)/article $',views.details,name='details'),
    #url(r'^article/(\d+)$',views.details,name='details'),
    url(r'^article/(?P<article_id>[0-9]+)/$',views.details,name='details'),
    url(r'^achive_list/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.achives,name='achives'),
    url(r'^category_list/(?P<category_id>[0-9]+)/$',views.categorys,name='categorys'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$',views.TagView.as_view(),name='tag'),
    url(r'^search/$',views.search,name='search')
]