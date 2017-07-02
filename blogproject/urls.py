"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import settings
from blog.feeds import ArticleRssFeed
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blog.blog_urls',namespace='blog')),
    url(r'',include('comments.comment_urls',namespace='comments')),
    url(r'',include('ckeditor_uploader.urls')),
    url(r'all/rss/$',ArticleRssFeed(),name='rss'),
    url(r'^',include('django.contrib.auth.urls')),#django自带的登录 注销 修改密码等功能
    url(r'users/',include('users.regist_url',namespace='users'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
