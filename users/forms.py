from  django.contrib.auth.forms import UserCreationForm
from users.models import User
#自定义用户的form
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields = ("username","email",)
