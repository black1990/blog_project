#coding=utf-8
from  ..models import Article,Category,Tag
from django import  template
from  django.db.models import Count
#获取最新文章模板标签
register=template.Library()
@register.simple_tag
def get_recent_article():
    return Article.objects.order_by('-create_time')[:5]

#归档模板标签
'''
这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，
且是 Python 的 date 对象，精确到月份，降序排列。接受的三个参数值表明了这些含义，
一个是 created_time ，即 Post 的创建时间，month 是精度，order='DESC'
 表明降序排列（即离当前越近的时间越排在前面）。例如我们写了 3 篇文章，
 分别发布于 2017 年 2 月 21 日、2017 年 3 月 25 日、2017 年 3 月 28 日，
 那么 dates 函数将返回 2017 年 3 月 和 2017 年 2 月这样一个时间列表，且降序排列，
 从而帮助我们实现按月归档的目的。
'''
@register.simple_tag
def achives():
    return Article.objects.dates('create_time','month',order='DESC')

#定义分类模板
@register.simple_tag
def get_categorys():
    #return Category.objects.all()
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    #这里 annotate 不仅从数据库获取了全部分类，相当于使用了 all 方法，
    # 它还帮我们为每一个分类添加了一个category_article_count  属性，其值为该分类下的文章数，这样我们在模板中就可以调用这个属性
    return  Category.objects.annotate(category_article_count=Count('article')).filter(category_article_count__gt=0)
#定义标签分类模板
@register.simple_tag
def get_tags():
    return  Tag.objects.annotate(tag_article_count=Count('article')).filter(tag_article_count__gt=0)



