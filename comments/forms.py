#coding=utf-8
from django import  forms
from .models import Comment
class CommentsForm(forms.ModelForm):
      class Meta:
        model=Comment#设置表单对应的模型是comment
        fields=['name', 'email', 'text']#表单显示的字段
        widgets={
            # 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
            # 例如 name 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">
            'name':forms.TextInput(attrs={
                'class': 'form-control',
                'size':'22',
                'placeholder': "请输入昵称",
                'maxlength':'15',
                'autocomplete':'off',
                'tabindex':'1',
                'aria-describedby': "sizing-addon1",
            }),
            'email':forms.TextInput(attrs={
                'class': 'form-control',
                'size':'22',
                'placeholder': "请输入邮箱",
                'maxlength':'58',
                'autocomplete':'off',
                'tabindex':'2',
                'aria-describedby': "sizing-addon1",
            }),
            'text':forms.Textarea(attrs={
                'placeholder': "我来评两句~",
                'name': "comment-textarea",
                'id': "comment-textarea",
                'cols': "100%",
                'rows': "3",
                'tabindex': "3"

            }),
        }