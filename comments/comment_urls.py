from  django.conf.urls import url
from . import views
urlpatterns=[
    url(r'comment/(?P<article_id>[0-9]+)/$',views.article_comment,name='article_comment'),
]