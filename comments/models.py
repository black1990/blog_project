from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100,verbose_name='评论名')
    email = models.EmailField(max_length=255,)
    url = models.URLField(blank=True)
    text = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    artilce = models.ForeignKey('blog.Article')

    def __str__(self):
        return self.text[:20]
    class Meta:
        verbose_name_plural='评论'
        verbose_name='评论'
        ordering=['-created_time']