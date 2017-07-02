from django.db import models
from  django.contrib.auth.models import AbstractUser
# Create your models here.
#继承系统自带的AbstructUser
class User(AbstractUser):
    nick_name=models.CharField(max_length=100,verbose_name='昵称',blank=True)
    sign=models.CharField(max_length=60,verbose_name='签名',blank=True)
    phone=models.CharField(max_length=15,verbose_name='手机',blank=True)
    qq = models.CharField(max_length=20, blank=True, verbose_name='QQ号码')
    class Meta(AbstractUser.Meta):
        verbose_name='用户扩展信息'
        verbose_name_plural = verbose_name

