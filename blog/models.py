#coding=utf-8
from django.db import models
from  users.models import User
from  django.urls import reverse
from django.utils.html import strip_tags
import markdown
from  ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name='分类名称')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='分类'
        verbose_name_plural='分类'

class Tag(models.Model):
    name=models.CharField(max_length=100,verbose_name='标签名称')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='标签'
        verbose_name_plural='标签'
class Article(models.Model):
    title=models.CharField(max_length=200,verbose_name='文章标题')
    content=RichTextUploadingField('内容')
    create_time=models.DateTimeField(verbose_name="创建时间")
    modified_time=models.DateTimeField(verbose_name='修改时间')
    excerpt=models.CharField(max_length=500,verbose_name='摘要',blank=True)
    category=models.ForeignKey(Category,verbose_name='分类')
    tags=models.ManyToManyField(Tag,verbose_name='标签')
    author=models.ForeignKey(User,verbose_name='用户')#继承系统自带的user
    visiter=models.PositiveIntegerField(verbose_name='浏览量',default=0)
    def __str__(self):
        return self.title
    def get_absolute_url(self):#获取文章的绝对路径路径
        return reverse('blog:details',kwargs={'article_id':self.pk})#pk=id
    #增加访问量
    def add_view(self):
        self.visiter+=1
        self.save(update_fields=['visiter'])
    def save(self,*args,**kwargs):
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.content))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Article, self).save()
    class Meta:
        ordering=['-create_time','title']
        verbose_name='文章'
        verbose_name_plural='文章'