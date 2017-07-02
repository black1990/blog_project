from django.shortcuts import render,redirect
from  .forms import RegisterForm
# Create your views here.
def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    #当请求为post 表示用户注册了信息
    if request.method =='POST':
        #实例化一个Form
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        auth_forms=RegisterForm(request.POST)
         # 验证数据的合法性
        if auth_forms.is_valid():
                # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
                auth_forms.save()

                # 注册成功，返回成功界面
                #return redirect(reverse('users:success'))
                return redirect(redirect_to)
    # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
    else:
            auth_forms = RegisterForm()
            # 渲染模板
            # 如果不是 POST 请求，则渲染的是一个空的表单
            # 如果用户通过表单提交数据，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'users/register.html', {'auth_forms': auth_forms,'next':redirect_to})